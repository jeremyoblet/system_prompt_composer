# Architecture

- Architecture hexagonale (ports & adapters)
- Définir des ports (protocoles/interfaces) côté domaine/application.
- Implémenter des adapters côté infrastructure (DB, HTTP, FS, queues, APIs).
- Les dépendances pointent vers l’intérieur (domaine/application), jamais l’inverse.
