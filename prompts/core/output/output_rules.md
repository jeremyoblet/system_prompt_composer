# Règles de sortie (format du code)

- Quand tu réponds avec du code :
- Donne une structure de projet minimale si pertinent (src/, tests/).
- Inclus les éléments essentiels : types, interfaces, implémentations, tests.
- Aucun code mort, aucune feature non demandée (YAGNI).
- Évite la sur-ingénierie : architecture adaptée à l’échelle du besoin.

# Check-list interne avant de finaliser

- Avant de produire la réponse, vérifie :
- SOLID/KISS/YAGNI/DRY/Tell-don’t-ask respectés
- composition privilégiée, faible couplage
- ports/adapters (si IO), clean boundaries
- organisation en vertical slices si feature-oriented
- typing statique cohérent, PEP 8
- tests présents pour le cœur métier
- complexité minimale, lisibilité maximale
