# Danaya : modèle de devis pour la vérification d'identité et de conformité

_Modèle à remplir pour une institution financière, avec exemple FICTIF chiffré, délégation de remise et message d'envoi_

> **FICTIF :** Document d'entraînement. Danaya ne publie aucun prix : toutes ses formules sont « sur devis » (danaya.africa/tarifs, lu le 15/10/2026). La grille de prix et la délégation de remise validées n'ayant pas été fournies, les prix, plafonds de remise, délais, validité et conditions de paiement de ce modèle sont laissés ⟦à renseigner⟧. Seuls l'exemple de la section 7 et la grille de travail de l'annexe A (prix et délégation de remise proposés à la direction, non en vigueur) portent des montants, tous FICTIFS, choisis pour tester les calculs : ce ne sont pas des prix de Danaya et ils ne doivent jamais être cités à un client. Le prospect de l'exemple (Finasud Microfinance SA, volume de 600 vérifications par mois) est inventé, repris des tests 10.1 et 14.1.


## Mode d'emploi du modèle (à supprimer avant envoi)

- **Ce qui est publié par Danaya** : quatre formules (On the Go, Basic, Croissance, Entreprise), toutes « sur devis selon votre volume ». Les paliers : Basic 1 à 500 vérifications par mois, Croissance 500 à 1 000, Entreprise plus de 1 000 (danaya.africa/tarifs). Le site ne publie aucun prix : un simulateur est annoncé « prochainement ».
- **Ce que le modèle exige avant envoi** : une grille de prix datée et une délégation de remise validées par la direction. Aucun prix ne sort sans elles. Un prix absent reste ⟦à renseigner⟧.
- **Règles de la méthode** : besoin reformulé dans les mots du client ; compris et non compris écrits en toutes lettres ; frais ponctuels séparés des frais récurrents ; calcul visible ; validité datée ; délai avec son point de départ ; une seule prochaine étape.
- **Modèle Google Doc** : remplacer chaque ⟦ ⟧ ; garder les tableaux ; enregistrer chaque version envoyée en copie figée (v1, v2) ; le PDF se fait sur la version finale. L'envoi au client reste un acte humain.


## 1. En-tête et destinataire

| Champ | À remplir | Source |
|---|---|---|
| Émetteur | Danaya ⟦raison sociale exacte, forme juridique, siège⟧ | ⟦à faire valider par le service juridique ou comptable : ne pas citer de mémoire⟧ |
| Mentions d'identification | ⟦RCCM, identifiant fiscal, régime d'imposition⟧ | ⟦à renseigner par le comptable⟧ |
| Contact commercial | ⟦prénom, nom, fonction, courriel, téléphone⟧ | Le commercial qui porte le compte |
| Référence | ⟦DEV-AAAA-NNN-vN⟧ | Suivi commercial |
| Date d'émission | ⟦jj/mm/aaaa⟧ | Jour de l'envoi |
| Valable jusqu'au | ⟦jj/mm/aaaa⟧ | Règle de validité de la direction ⟦à renseigner⟧ : jamais estimée par l'Expert |
| Destinataire | ⟦Nom, fonction⟧, ⟦institution cliente⟧, ⟦adresse ou canal⟧ | Rendez-vous ou échange écrit |
| Objet | Devis, vérification d'identité et de conformité pour ⟦institution cliente⟧ |  |


## 2. Votre besoin, dans vos mots

⟦Trois à cinq lignes reprenant la demande du client avec ses termes, issues du compte rendu de visite. Exemple de forme : « Vous ouvrez environ ⟦volume⟧ comptes par an, en agence et sur le terrain. Vous souhaitez ⟦besoin exprimé⟧ avant ⟦échéance du client⟧. »⟧ **Le client relit ce paragraphe : s'il le corrige, le devis évite d'être refait.**


## 3. Ce qui est proposé, avec le détail chiffré

Un seul tableau, des montants en francs CFA au format 1 250 000 F CFA, le calcul visible. Les frais ponctuels et les frais récurrents sont séparés.


### 3.1 Frais ponctuels (une seule fois)

| Désignation | Quantité | Unité | Prix unitaire HT | Sous-total HT |
|---|---|---|---|---|
| Mise en service et accès à l'environnement de production ⟦à confirmer avec le produit⟧ | ⟦qté⟧ | forfait | ⟦prix de la grille⟧ | ⟦qté × prix⟧ |
| Intégration API ou accompagnement ⟦à confirmer avec le produit⟧ | ⟦qté⟧ | ⟦jour ou forfait⟧ | ⟦prix de la grille⟧ | ⟦qté × prix⟧ |
| **Total frais ponctuels HT** |  |  |  | ⟦somme⟧ |


### 3.2 Frais récurrents (par mois)

| Désignation | Volume mensuel | Unité | Prix unitaire HT | Sous-total mensuel HT |
|---|---|---|---|---|
| Vérification d'identité (KYC) : lecture de la pièce, comparaison du visage | ⟦volume⟧ | vérification | ⟦prix de la formule ⟦formule⟧⟧ | ⟦volume × prix⟧ |
| Criblage LCB-FT (sanctions, personnes exposées, presse négative) | ⟦volume⟧ | vérification | ⟦prix de la grille⟧ | ⟦volume × prix⟧ |
| Vérification d'entreprise (KYB) pour groupements et coopératives ⟦si demandé⟧ | ⟦volume⟧ | vérification | ⟦prix de la grille⟧ | ⟦volume × prix⟧ |
| **Total récurrent mensuel HT** |  |  |  | ⟦somme⟧ |

| Récapitulatif | Montant |
|---|---|
| Total HT du premier mois (ponctuel + récurrent) | ⟦somme⟧ F CFA |
| Remise accordée ⟦si accordée par la personne habilitée, avec sa contrepartie⟧ | ⟦montant ou « aucune »⟧ |
| Taxe ⟦régime applicable, à confirmer par le comptable : aucun taux de mémoire⟧ | ⟦montant⟧ |
| **Total à payer, premier mois** | ⟦montant⟧ F CFA |

**Formule de Danaya retenue** : ⟦On the Go, Basic, Croissance ou Entreprise⟧, selon le volume mensuel de ⟦volume⟧ vérifications annoncé par le client. Au-delà ou en deçà du palier, le prix unitaire change : ⟦règle de dépassement à renseigner par la direction⟧.


## 4. Ce qui est compris, ce qui ne l'est pas

| Compris | Non compris (facturé en plus, sur quelle base) |
|---|---|
| ⟦Nombre exact de vérifications mensuelles incluses, avec les contrôles listés en 3.2⟧ | ⟦Vérifications au-delà du volume inclus : prix unitaire du palier suivant⟧ |
| ⟦Accès à l'environnement de test pendant ⟦durée⟧⟧ | ⟦Développements spécifiques demandés par le client⟧ |
| ⟦Support aux horaires de la formule : lundi au vendredi de 8 h à 18 h pour Basic (danaya.africa/tarifs) ; à confirmer pour la formule retenue⟧ | ⟦Support hors horaires de la formule⟧ |
| ⟦Conservation des dossiers de vérification, durée de la formule⟧ | ⟦Conservation au-delà de la durée de la formule⟧ |
|  | ⟦Formation du personnel du client au-delà de ⟦nombre⟧ séance(s)⟧ |

**Hypothèses dont dépend le prix** : ⟦ex. « le prix suppose un volume mensuel de ⟦volume⟧ vérifications, la connexion des agences à Internet et la désignation d'un interlocuteur côté client »⟧. **Si une hypothèse tombe, la discussion se rouvre.**


## 5. Délai, validité, règlement

| Sujet | Contenu | Source |
|---|---|---|
| Délai de mise à disposition | ⟦n⟧ jours ouvrés à compter de ⟦événement qui le fait courir, par exemple la réception du bon pour accord et du premier règlement⟧ | ⟦à vérifier auprès du produit : jamais promis sur estimation⟧ |
| Validité de l'offre | Jusqu'au ⟦date⟧. Passé ce délai, le devis est réémis ou reconfirmé. | Règle de la direction |
| Conditions de règlement | ⟦acompte, périodicité, échéance⟧ ; moyens : ⟦virement, mobile money, chèque⟧ en termes génériques | Politique de règlement ⟦à renseigner⟧ ; encours du client selon la fiche de risque |
| Retard de paiement | ⟦pénalités⟧ | ⟦à faire valider par le juridique : aucun taux inventé⟧ |
| Données personnelles | Les données de vos membres sont traitées par Danaya pour votre compte selon un accord de sous-traitance joint ⟦à renseigner⟧ ; le lieu d'hébergement est ⟦à confirmer par le produit⟧ | Compétence donnees-personnelles-ci ; loi n°2013-450 ; validation Ibrahim |


## 6. Remise : délégation et contrepartie

| Niveau | Remise maximale | Contrepartie attendue | Qui valide |
|---|---|---|---|
| Commercial, seul | ⟦% ou montant⟧ | ⟦volume, durée d'engagement, paiement anticipé⟧ | Le commercial |
| Responsable commercial | ⟦% ou montant⟧ | ⟦contrepartie⟧ | ⟦nom⟧ |
| Direction | ⟦% ou montant⟧ | ⟦contrepartie⟧ | ⟦nom⟧ |

**Une remise sans contrepartie nommée remonte d'un niveau.** Aucune remise n'apparaît dans le devis tant que la personne habilitée ne l'a pas accordée par écrit. Le plafond d'encours du client et le délai de règlement relèvent de la compétence conditions-de-paiement-et-encours, pas du commercial.


## 7. Exemple de remplissage (FICTIF, valeurs de démonstration)

> **FICTIF.** Les montants ci-dessous servent à vérifier les calculs. Ce ne sont pas des prix de Danaya : Danaya n'en publie aucun. Finasud Microfinance SA et son volume de 600 vérifications par mois sont inventés.

**Besoin reformulé (FICTIF)** : « Vous ouvrez environ 3 500 comptes par an, surtout en agence, un peu sur le terrain. Vous voulez prouver à l'inspecteur ce qui a été contrôlé, dossier par dossier. » **Formule retenue** : Croissance (500 à 1 000 vérifications par mois).

| Désignation | Quantité | Unité | Prix unitaire HT (FICTIF) | Sous-total HT (FICTIF) |
|---|---|---|---|---|
| Mise en service et environnement de production | 1 | forfait | 300 000 F CFA | 300 000 F CFA |
| **Total frais ponctuels HT** |  |  |  | **300 000 F CFA** |

| Désignation | Volume mensuel | Unité | Prix unitaire HT (FICTIF) | Sous-total mensuel HT (FICTIF) |
|---|---|---|---|---|
| Vérification d'identité (KYC) | 600 | vérification | 450 F CFA | 600 × 450 = 270 000 F CFA |
| Criblage LCB-FT | 600 | vérification | 150 F CFA | 600 × 150 = 90 000 F CFA |
| **Total récurrent mensuel HT** |  |  |  | **360 000 F CFA** |

| Récapitulatif (FICTIF) | Montant |
|---|---|
| Total HT du premier mois : 300 000 + 360 000 | 660 000 F CFA |
| Remise | Aucune : non accordée |
| Taxe | ⟦à confirmer par le comptable⟧ |
| **Total HT du premier mois** | **660 000 F CFA** ; total à payer ⟦après taxe⟧ |
| Mois suivants, HT | 360 000 F CFA par mois |

Contrôle du calcul : 600 × 450 = 270 000 ; 600 × 150 = 90 000 ; 270 000 + 90 000 = 360 000 ; 300 000 + 360 000 = 660 000. **Délai, validité, règlement : ⟦à renseigner⟧.**


## 8. Prochaine étape (une seule)

Pour accepter, retourner ce document signé avec la mention « bon pour accord » avant le ⟦date⟧. Fait à ⟦lieu⟧, le ⟦date⟧. Pour Danaya : ⟦nom, fonction, signature⟧. Pour le client : bon pour accord, nom, date et signature ⟦à compléter par le client⟧.


## 9. Message d'envoi (brouillon, à valider avant envoi)

> Objet : Devis Danaya, vérification des dossiers membres, validité ⟦date⟧
>
> Madame ⟦Nom⟧,
>
> Comme convenu lors de notre rendez-vous du ⟦date⟧, voici le devis pour la vérification des dossiers membres de ⟦institution⟧, sur la formule ⟦formule⟧. Il comprend ⟦en deux lignes : frais ponctuels et frais mensuels⟧.
>
> Merci de me retourner le bon pour accord signé avant le ⟦date⟧, ou de m'appeler si un point doit être corrigé.
>
> Bien cordialement,
> ⟦Prénom Nom⟧
> ⟦Fonction⟧, Danaya, Abidjan


## 10. Suite proposée (non lancée)

> **Devis réel** pour Finasud Microfinance SA (FICTIF) ou un autre prospect : à produire seulement quand la direction a validé la grille de prix et la délégation de remise, et que le test sur dossiers du test 14.1 est fait. Je prépare alors le devis sur ce modèle ; **il ne part pas sans accord** et le statut de l'affaire dans le pipeline ne change pas sans accord.


## Annexe A. Grille de prix et délégation de remise de travail (FICTIF, en attente de validation)

> **FICTIF.** Le brief demande une grille de prix et une délégation de remise validées : elles n'existent pas en source publique (danaya.africa/tarifs : « sur devis selon votre volume »). Voici une **proposition de travail inventée** pour que la direction ait un texte à corriger. Elle n'est **pas en vigueur** : aucun devis ne s'en sert tant qu'elle n'est pas signée et datée.

| Prestation (unité) | On the Go | Basic (1 à 500 / mois) | Croissance (500 à 1 000) | Entreprise (+ 1 000) |
|---|---|---|---|---|
| Vérification d'identité KYC (par vérification) | 700 F | 550 F | 450 F | 380 F |
| Criblage AML / PEP / presse négative (par vérification) | 200 F | 180 F | 150 F | 120 F |
| Vérification d'entreprise KYB (par dossier) | 2 500 F | 2 200 F | 2 000 F | 1 800 F |
| Mise en service (forfait, une fois) | aucune | 150 000 F | 300 000 F | sur étude |
| Inclus (danaya.africa/tarifs) | paiement à l'usage | conservation des dossiers, API, support lun-ven 8 h-18 h | conservation étendue, API | conservation longue durée, support 24/7, personnalisation |

Tous les montants ci-dessus sont **FICTIFS**, hors taxe, en francs CFA. Validité proposée : ⟦du 01/11/2026 au 31/03/2027⟧. Exclus : développements spécifiques, formation au-delà d'une séance, taxes ⟦régime à confirmer par le comptable⟧. Seules les colonnes de formules et le contenu « inclus » viennent du site.

| Niveau | Plafond de remise (FICTIF) | Contrepartie exigée (FICTIF) | Ne peut jamais |
|---|---|---|---|
| Commercial, seul | 5 % sur le récurrent | Engagement écrit de 12 mois | Toucher au forfait de mise en service |
| Responsable commercial | 10 % sur le récurrent ; 50 % sur la mise en service | Engagement 12 mois et règlement trimestriel d'avance | Descendre sous le prix du palier supérieur |
| Direction | Au-delà, ou toute remise sans contrepartie | Décision écrite, archivée avec le devis | (sans plafond, mais justifiée par écrit si deux clients se connaissent) |

Règle de la méthode : **une remise sans contrepartie remonte d'un niveau**. Exemple (FICTIF) : Finasud demande 8 % sans engagement : le commercial ne peut pas l'accorder seul, la demande va au responsable avec la contrepartie à négocier.


## Annexe B. Réponses types sur le prix (à valider par la direction)

| Question du client | Réponse type | À ne pas promettre |
|---|---|---|
| « Quel est votre prix par vérification ? » | Le prix dépend du volume mensuel : quatre formules, le prix unitaire baisse quand le volume monte (danaya.africa/tarifs). Donnez-moi votre volume, je vous chiffre sur la formule qui correspond. | Un prix donné de mémoire ou hors grille. |
| « Un concurrent fait moins cher. » | Comparons sur le même périmètre : pièces ivoiriennes lues, registres locaux recoupés (RCCM, DFE), dossier exportable pour l'inspecteur. Je peux revoir le prix si vous vous engagez sur une durée ou un volume. | Une baisse sans contrepartie. |
| « Faites-nous un geste pour signer ce mois-ci. » | Une remise est possible contre un engagement de durée ou un règlement d'avance ; je la fais valider et je vous la confirme par écrit. | Une remise « exceptionnelle » non validée. |
| « Quand serons-nous en service ? » | Le délai part de la réception du bon pour accord ; je vous le confirme par écrit avec l'équipe produit. | Un délai estimé, ou « presque instantanément ». |


## Annexe C. Contrôle avant envoi (relecture du devis)

| Point vérifié | Conforme ? |
|---|---|
| Chaque prix vient de la grille en vigueur, datée et signée | ☐ |
| La remise est dans la délégation du signataire, avec sa contrepartie écrite | ☐ |
| Compris et non compris écrits ; frais ponctuels séparés des frais mensuels | ☐ |
| Calculs refaits à la main ; plus aucun ⟦ ⟧ dans le texte | ☐ |
| Validité datée ; délai avec son point de départ ; règlement écrit | ☐ |
| Aucune promesse interdite (délai estimé, hors-ligne, lieu d'hébergement, conformité garantie) | ☐ |
| Même offre que pour un client comparable, ou écart justifié par écrit | ☐ |

Si un point n'est pas conforme : l'écart est nommé, la version conforme proposée, et le responsable prévenu **avant** tout envoi s'il dépasse la délégation.


---
Rien n'a été envoyé ni publié. Modèle et exemple d'entraînement FICTIFS, préparés par Kouassi, Expert commercial et ventes.