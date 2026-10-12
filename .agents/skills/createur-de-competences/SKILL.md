---
description: Aide à la conception et à la génération de nouvelles compétences Antigravity en français, en respectant les standards officiels.
---

# Créateur de Compétences

Cette compétence guide l'agent pour créer de nouvelles compétences (`skills`) de manière structurée et conforme à la documentation officielle d'Antigravity.

## Quand utiliser cette compétence
Utilisez cette compétence dès qu'il est nécessaire de :
- Concevoir une nouvelle capacité réutilisable pour l'agent.
- Structurer un dossier de compétence avec ses scripts, exemples et ressources.
- Rédiger des instructions claires et une description d'activation efficace en français.

## Comment l'utiliser
Suivez ces étapes pour chaque nouvelle compétence :

### 1. Structure du Dossier
Créez un dossier dans `.agents/skills/<nom-de-la-compétence>/` avec la structure suivante :
- `SKILL.md` (Obligatoire)
- `scripts/` (Optionnel : scripts utilitaires)
- `examples/` (Optionnel : fichiers de référence ou modèles)
- `resources/` (Optionnel : templates, documentation additionnelle)

### 2. Rédaction du fichier `SKILL.md`
Le fichier doit commencer par un frontmatter YAML :
```yaml
---
description: Traduction concise de l'objectif de la compétence à la 3ème personne (ex: Génère des tests unitaires...).
---
```

Le corps du Markdown doit être en français et structuré ainsi :
- `# Nom de la Compétence`
- `## Quand utiliser cette compétence`
- `## Instructions détaillées`
- `## Scripts et Outils` (si applicable)
- `## Checklist de Qualité`

### 3. Principes de Rédaction
- **Précision** : La `description` dans le YAML est cruciale pour l'activation. Utilisez des mots-clés pertinents.
- **Français** : Tout le contenu doit être rédigé dans un français clair et professionnel.
- **Scripts** : Si des scripts sont inclus, documentez leur usage (ex: `python script.py --help`).
- **Exemples** : Fournissez toujours un exemple concret dans le dossier `examples/`.

## Checklist de Création
- [ ] Le dossier est bien situé dans `.agents/skills/`.
- [ ] Le fichier `SKILL.md` possède une description YAML valide.
- [ ] Toutes les instructions sont en français.
- [ ] La description permet une activation logique par l'agent.
- [ ] Les éventuels scripts sont exécutables et documentés.
