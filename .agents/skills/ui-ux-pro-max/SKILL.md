---
name: ui-ux-pro-max
description: Intelligence de design pour créer des interfaces professionnelles (SaaS, E-commerce, portfolios). Fournit des palettes de couleurs, des polices, des styles UI (glassmorphism, bento, etc.) et des systèmes de design complets.
---

# UI UX Pro Max

Cette compétence est une boîte à outils d'intelligence de design fournissant des bases de données de styles UI, palettes de couleurs, associations de polices, types de graphiques et directives UX.

## Quand utiliser cette compétence
Utilisez cette compétence pour :
- Concevoir une nouvelle interface utilisateur (Landing page, Dashboard, App mobile).
- Rechercher des inspirations de styles (ex: Glassmorphism, Minimalisme).
- Générer un système de design cohérent pour un nouveau projet.
- Vérifier les bonnes pratiques UX et éviter les anti-patterns.

## Instructions d'utilisation

### 1. Recherche de Design par Domaine
Vous pouvez rechercher des éléments spécifiques via le script Python inclus.
```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<votre_requête>" --domain <domaine>
```
**Domaines disponibles :**
- `product` : Recommandations par type de produit (SaaS, e-commerce, etc.).
- `style` : Styles UI (glassmorphism, bento) + prompts IA et mots-clés CSS.
- `typography` : Combinaisons de polices avec imports Google Fonts.
- `color` : Palettes de couleurs par type de produit.
- `landing` : Structures de pages et stratégies de CTA.
- `chart` : Types de graphiques et bibliothèques recommandées.
- `ux` : Meilleures pratiques et anti-patterns.

### 2. Recherche par Stack Technique
Adaptez les composants à votre technologie :
```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<votre_requête>" --stack <techno>
```
**Technos supportées :** `html-tailwind` (par défaut), `react`, `nextjs`, `vue`, `react-native`, `flutter`, `shadcn`.

### 3. Génération de Système de Design (Avancé)
Pour générer un système de design complet à partir d'une simple description de produit :
```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "votre description" --design-system -p "NomDuProjet"
```

## Principes de Design
- Toujours privilégier l'accessibilité (contraste WCAG AA).
- Utiliser des animations subtiles (150-300ms).
- Éviter les dégradés complexes type "AI purple/pink" sauf si c'est explicitement demandé.

## Checklist de Qualité UI/UX
- [ ] Le contraste du texte est au minimum de 4.5:1.
- [ ] Les états de survol (hover) sont présents et fluides.
- [ ] La hiérarchie typographique est respectée (H1, H2, etc.).
- [ ] Le design est cohérent avec le système de design généré.
