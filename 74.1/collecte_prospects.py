#!/usr/bin/env python3
"""Outil d'identification des prospects doo! (agents dooer) : collecte OpenStreetMap,
dédoublonnage, rapprochement avec l'annuaire doo!, qualification par règles.
N'envoie rien, ne contacte personne : produit un CSV que des humains valident.
Usage : python3 collecte_prospects.py Bouaké 7.6900 -5.0300 3000 sortie.csv
"""
import csv, json, math, sys, time, urllib.parse, urllib.request, datetime as dt

OVERPASS = "https://overpass-api.de/api/interpreter"
UA = "doo-prospects-outil/1.0 (usage interne, collecte manuelle hebdomadaire)"
ANNUAIRE = "/home/node/.hermes/profiles/kouassi/work/out/doo_network.json"  # annuaire doo.africa/agences

# Règles de qualification (points PROPOSÉS, à valider par la direction)
CIBLES_FORTES = {"money_transfer": "Point Mobile Money", "mobile_phone": "Boutique téléphonie"}
CIBLES = {"internet_cafe": "Cyber", "copyshop": "Photocopie", "stationery": "Papeterie",
          "computer": "Informatique", "convenience": "Supérette", "kiosk": "Kiosque"}
REGLES = [
    ("R1", "Activité de guichet déjà en place (Mobile Money, téléphonie)", 40),
    ("R2", "Activité de service au comptoir (cyber, photocopie, papeterie, informatique, supérette, kiosque)", 25),
    ("R3", "Aucun agent dooer à moins de 500 m (annuaire doo!)", 25),
    ("R4", "Horaires publiés jusqu'à 18 h ou plus tard", 10),
    ("R5", "Téléphone d'entreprise publié sur la fiche", 10),
    ("R6", "Agent dooer à moins de 50 m (même point probable)", -100),
]
SEUIL_CORRESPOND, SEUIL_VERIFIER = 60, 35
GENERIQUES = {"orange money", "mobile money", "point orange money", "moov", "mtn", "orange", "wave", "kiosque",
              "boutique", "supérette", "superette", "photocopie", "cyber", "ciber cafe", "flooz, mobile money",
              "orange et mtn money", "orange et flooz money", "flooz, mtn mobile money", "orange, mtn, flooz"}


def km(a, b):
    R = 6371.0
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def overpass(lat, lng, rayon):
    tags = "|".join(list(CIBLES_FORTES) + list(CIBLES))
    q = (f'[out:json][timeout:90];(nwr(around:{rayon},{lat},{lng})[amenity~"^({tags})$"];'
         f'nwr(around:{rayon},{lat},{lng})[shop~"^({tags})$"];);out center tags;')
    import hashlib, os
    cache = f"cache_osm_{hashlib.md5(q.encode()).hexdigest()[:10]}.json"   # une collecte par jour et par zone
    if os.path.exists(cache) and time.time() - os.path.getmtime(cache) < 86400:
        return json.load(open(cache))["elements"]
    for essai in range(4):                                                   # service public partagé : on patiente
        try:
            req = urllib.request.Request(OVERPASS, data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": UA})
            d = json.load(urllib.request.urlopen(req, timeout=120)); json.dump(d, open(cache, "w")); return d["elements"]
        except Exception as ex:
            print(f"Overpass indisponible ({ex}), nouvel essai dans {30*(essai+1)} s", file=sys.stderr); time.sleep(30 * (essai + 1))
    raise SystemExit("Overpass indisponible : collecte reportée, aucune ligne inventée.")


def annuaire():
    d = json.load(open(ANNUAIRE)); pts = {}
    for _, (ville, liste) in d.items():
        for p in liste:
            try:
                la, lo = [float(x) for x in p["location"].split(",")]
            except Exception:
                continue
            pts[p["id"]] = (p["name"], la, lo, bool(p["services"]))
    return list(pts.values())


def heure_fin(h):
    import re
    m = re.findall(r"(\d{1,2}):\d{2}", h or "")
    return int(m[-1]) if m else None


def main(ville, lat, lng, rayon, sortie):
    jour = dt.date.today().isoformat()
    agents = annuaire()
    lignes, vus = [], {}
    for e in overpass(lat, lng, rayon):
        t = e.get("tags", {}); nom = (t.get("name") or "").strip()
        if not nom:
            continue
        typ = t.get("shop") if t.get("shop") in {**CIBLES_FORTES, **CIBLES} else t.get("amenity")
        if t.get("amenity") == "fuel" and typ == "kiosk":
            typ = "kiosk"  # boutique de station-service
        la = e.get("lat") or e["center"]["lat"]; lo = e.get("lon") or e["center"]["lon"]
        # Dédoublonnage : même nom (casse ignorée) à moins de 100 m = doublon probable, SIGNALÉ, jamais fusionné seul
        double = next((l for l in lignes if l["Raison sociale"].lower() == nom.lower() and nom.lower() not in GENERIQUES
                       and km((la, lo), (l["Latitude"], l["Longitude"])) < 0.1), None)
        dmin, proche = min((km((la, lo), (a[1], a[2])), a[0]) for a in agents)
        crit, note = [], 0
        if typ in CIBLES_FORTES: crit.append("R1"); note += 40
        elif typ in CIBLES: crit.append("R2"); note += 25
        if dmin > 0.5: crit.append("R3"); note += 25
        hf = heure_fin(t.get("opening_hours"))
        if hf and hf >= 18: crit.append("R4"); note += 10
        tel = t.get("phone") or t.get("contact:phone") or ""
        if tel: crit.append("R5"); note += 10
        connu = "nouveau"
        if dmin < 0.05: crit.append("R6"); note -= 100; connu = f"agent dooer probable ({proche})"
        note = max(0, min(100, note))
        niveau = "correspond" if note >= SEUIL_CORRESPOND else "à vérifier" if note >= SEUIL_VERIFIER else "hors cible"
        generique = nom.lower().strip(" .") in GENERIQUES
        if generique and niveau == "correspond":
            niveau = "à vérifier"  # enseigne inconnue : on ne sait pas qui est le commerce, relevé sur place
        ligne = {"ID": "OSM-" + e["type"][0] + str(e["id"]), "Raison sociale": nom,
                 "Activité": ("Boutique de station-service" if t.get("amenity") == "fuel" else CIBLES_FORTES.get(typ) or CIBLES.get(typ) or typ),
                 "Commune et quartier": ville + (", " + t["addr:street"] if t.get("addr:street") else ""),
                 "Latitude": round(la, 6), "Longitude": round(lo, 6),
                 "Standard ou contact d'entreprise": tel, "Interlocuteur public": "",
                 "Source": f"OpenStreetMap (ODbL) {e['type']}/{e['id']}", "Date de collecte": jour,
                 "Critères remplis": " ".join(crit), "Note": note, "Niveau": niveau,
                 "Agent dooer le plus proche": f"{proche} à {round(dmin*1000)} m",
                 "Déjà connu": connu, "Nom générique": "oui, enseigne à relever" if generique else "", "Doublon signalé": ("probable : " + double["ID"]) if double else "", "Décision humaine": "", "Opposition": "non"}
        lignes.append(ligne)
    lignes.sort(key=lambda x: -x["Note"])
    with open(sortie, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0])); w.writeheader(); w.writerows(lignes)
    print(f"{ville} : {len(lignes)} lignes, " + ", ".join(
        f"{n} {sum(1 for l in lignes if l['Niveau']==n)}" for n in ("correspond", "à vérifier", "hors cible")))


if __name__ == "__main__":
    v, la, lo, r, s = sys.argv[1:6]
    main(v, float(la), float(lo), int(r), s)
