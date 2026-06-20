# Changelog

All notable changes to this project's ontology and/or knowledge graph will be
documented in this file.  

## Unreleased
[Diff](https://github.com/metamuses/monomyth/compare/v1.1...main)

### Ontology

- Declared `monomyth:hasHero` and `monomyth:heroOf` as sub-properties of `monomyth:hasCharacter` and `monomyth:characterOf` respectively (`rdfs:subPropertyOf`), making the hero/character hierarchy explicit at the schema level while preserving existing explicit triples.
- Fixed incorrect class name `MonomythInstance` → `MonomythExpression` in the `rdfs:comment` of `monomyth:stageRealizationOrder`.

## 1.1 - 2026-05-21
[Release](https://github.com/metamuses/monomyth/releases/tag/v1.1) |
[Diff](https://github.com/metamuses/monomyth/compare/v1.0...v1.1)

### Ontology

- Introduced `monomyth:stageRealizationOf` as inverse of `monomyth:hasStageRealization` to enable bidirectional navigation between `StageRealization` and `MonomythExpression`.
- Added extensive OWL disjointness axioms across core classes (`owl:disjointWith`) to enforce clear semantic boundaries.
- Added explicit inequality assertions among key individuals (`owl:differentFrom`) for acts, stages, archetypes, and fit-quality values.
- Tightened constraints with additional property characteristics:
  - Functional object properties (e.g. `monomyth:belongsToAct`, `monomyth:realizesStage`, `monomyth:hasFitQuality`).
  - `monomyth:followsStage` marked as `owl:FunctionalProperty`, `owl:IrreflexiveProperty`, and `owl:AsymmetricProperty`.
  - Functional datatype properties (e.g. `monomyth:actOrder`, `monomyth:stageOrder`, `monomyth:fitScore`, `monomyth:stageRealizationOrder`).
- Changed ranges from `xsd:string` to `rdfs:Literal` for:
  - `monomyth:fitNote`
  - `monomyth:realizationDescription`
  - `monomyth:divergenceRationale`
- Removed `owl:FunctionalProperty` from `monomyth:stageRealizationOf` so a `StageRealization` can belong to multiple `MonomythExpressions`.
- Declared all ontology individuals also as `owl:NamedIndividual` (acts, stages, archetypes, fit-quality values) for clearer semantic distinction.
- Expanded/rewrote several narrative comments and reordered some triples for clarity.
- Added VANN metadata:
  - `vann:preferredNamespacePrefix`
  - `vann:preferredNamespaceUri`
  - `vann:example`
  - `vann:changes`
- Added new documentation URL in `rdfs:seeAlso`.
- Updated ontology version metadata:
  - `owl:versionInfo` → `1.1`
  - `owl:versionIRI` → `/1.1/ontology.ttl`
  - Added `owl:priorVersion` pointing to 1.0
- Updated `dcterms:modified` to release date of v1.1 update.

### Knowledge Graph

- Dataset root now typed as both `owl:Ontology` and `void:Dataset`.
- Replaced `dcterms:conformsTo` with explicit `owl:imports` `<.../1.1/ontology.ttl>`.
- Added versioning metadata:
  - `owl:versionInfo` `"1.1"`
  - `owl:versionIRI` `<.../1.1/graph.ttl>`
  - `owl:priorVersion` `<.../1.0/graph.ttl>`
- Updated distribution/access metadata:
  - `void:dataDump` → `1.1/graph.ttl`
  - added `void:sparqlEndpoint`
  - added `void:uriSpace`
- Updated `dcterms:modified` to release date of v1.1 update.

## 1.0 - 2026-05-13
[Release](https://github.com/metamuses/monomyth/releases/tag/v1.0)

**OWL ontology** for modeling narrative works through **Campbell's monomyth framework**. 11 classes, 26 properties (19 object, 7 datatype), serialized in Turtle at the `monomyth#` namespace.

**Core modeling patterns**: `MonomythExpression` anchors per-work interpretations; `StageRealization` captures concrete manifestations of Campbell's 17 stages with ordered positioning and prose descriptions; `FitQuality` provides a six-point assessment scale (PerfectFit through InvertedFit). Character-archetype linkage follows Vogler's dramaturgy via `embodiesArchetype`.

**Three divergence classes** (`NarrativeDivergence`, `SequentialDivergence`, `SemioticDivergence`) model departures along the what/when/how axes, each with prose rationales. Integrates selected CREON elements (Gangemi & Lucifora, 2024) for creative product divergence classification.

Includes **12 instantiated knowledge graphs** spanning ancient myth, classic literature, film, animation, videogames, and music.
