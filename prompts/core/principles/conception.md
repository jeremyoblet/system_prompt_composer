# Principes de conception à respecter systématiquement

## SOLID (maîtrise et respect)

- Single Responsibility : chaque module/classe/fonction a une responsabilité claire.
- Open/Closed : extension par composition/configuration plutôt que modification.
- Liskov : substituabilité respectée (si polymorphisme).
- Interface Segregation : petites interfaces centrées sur un usage.
- Dependency Inversion : dépendre d’abstractions, injection de dépendances, ports/adapters.

## KISS (maîtrise et respect)

- Prioriser la solution la plus simple qui répond au besoin.
- Éviter les abstractions prématurées.
- Préférer des structures de données/approches standard.

## YAGNI (maîtrise et respect)

- Ne pas implémenter de fonctionnalités “au cas où”.
- Limiter la généricité aux besoins actuels.

## DRY (maîtrise et respect)

- Éliminer la duplication utilement (sans sur-abstraction).
- Mutualiser via fonctions/objets dédiés lorsque la duplication devient coûteuse.

## Tell, don’t ask (maîtrise et respect)

- Favoriser l’encapsulation : demander à l’objet d’agir plutôt que d’extraire son état pour décider ailleurs.
- Déplacer la logique au plus près des données.
