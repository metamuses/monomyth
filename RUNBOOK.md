# Runbook

This document collects some repeatable maintenance procedures for the project.
It is meant to be used as a practical checklist for maintainers handling
standard operational tasks, such as preparing new version releases, updating 
the knowledge graphs or applying internal changes. The goal is to ensure that
these tasks are performed consistently and correctly, following the same steps
and checks each time. Whenever a process changes, this document should be
updated to reflect the new steps and assumptions.

## Table of contents

- [Release a new version](#release-a-new-version)
- [Update an existing subgraph](#update-an-existing-subgraph)
- [Add a new subgraph](#add-a-new-subgraph)

## Release a new version
When a new version of the ontology and graph is ready to be released, it is
important to update their metadata accordingly and to ensure they are properly
versioned and tagged in GitHub, with a new release created from the tag.
Ontology and graph are always released together, as they are tightly coupled
and are versioned in sync.  
The versioning of the project follows the `<major>.<minor>` format, without a
patch number.

Follow these steps to release a new version:

1. Update `ontology/ontology.ttl` fields:
    - `owl:versionInfo`  
      the new version being released as string, e.g. `"1.2"`
    - `owl:versionIRI`  
      the new version IRI of the ontology, e.g. `<https://monomyth.metamuses.org/1.2/ontology.ttl>`
    - `owl:priorVersion`  
      the previous version IRI of the ontology, e.g. `<https://monomyth.metamuses.org/1.1/ontology.ttl>`
    - `vann:changes`  
      the GitHub _release_ URL for the new version, e.g. `<https://github.com/metamuses/monomyth/releases/tag/v1.2>`
    - `dcterms:modified`  
      the date of the new release in ISO format, e.g. `"2026-05-25"`
2. Update `graph/graph.ttl` fields:
    - `owl:imports`  
      the new version IRI of the ontology, e.g. `<https://monomyth.metamuses.org/1.2/ontology.ttl>`
    - `owl:versionInfo`  
      the new version being released as string, e.g. `"1.2"`
    - `owl:versionIRI`  
      the new version IRI of the graph, e.g. `<https://monomyth.metamuses.org/1.2/graph.ttl>`
    - `owl:priorVersion`  
      the previous version IRI of the graph, e.g. `<https://monomyth.metamuses.org/1.1/graph.ttl>`
    - `void:dataDump`  
      the new version IRI of the graph, e.g. `<https://monomyth.metamuses.org/1.2/graph.ttl>`
    - `dcterms:modified`  
      the date of the new release in ISO format, e.g. `"2026-05-25"`
3. Update `CITATION.cff` fields:
    - `version`  
      the new version being released as string, e.g. `"1.2"`
    - `date-released`  
      the date of the new release in ISO format, e.g. `"2026-05-25"`
4. Update `website/docs.html` with the changes to namespaces, classes,
   properties and individuals of the new version, if applicable. Then, update
   the ontology metadata section with the same changes of step 1.
5. Evaluate if the graffoo diagram of the ontology at `graffoo/ontology.graphml`
   needs to be updated to reflect the changes in the new version. If so, update
   the diagram and export it again as png at `graffoo/ontology.png` with:
     - Size: Original Size
     - Margin: 100
     - Region: Complete Diagram
     - Scaling Factor: 1.0
6. Update the `CHANGELOG.md` file with the new version and a summary of the
   changes in the release, following the format of previous entries.
7. Create a commit `"Bump version to vX.Y"` and push to GitHub, e.g. `git commit -m "Bump version to v1.2"`.
8. Tag the commit with `"vX.Y"` and push the tag to GitHub, e.g. `git tag v1.2 -m "v1.2"`.
9. Create a release `"vX.Y"` on GitHub from the tag and include the release notes
   with the same summary of changes as in the `CHANGELOG.md`.
10. Check the Zenodo publication for the new synced release being properly rolled
    out: https://doi.org/10.5281/zenodo.20324714
11. Edit the GitHub release notes to include the new version-specific Zenodo DOI
    and the IRI of the versioned ontology and graph, following the format of
    previous releases.

## Update an existing subgraph
To update an existing narrative subgraph, edit the corresponding source TTL file
and then regenerate the derived general graph and website data from it.
Subgraphs are the authoritative sources for individual narrative works, while
`graph/graph.ttl` and `website/data/modal_data.json` are generated outputs that
must stay in sync. Each update should therefore be validated before the merged
graph and website data are regenerated.

1. Edit the TTL file for the narrative work in `graph/subgraphs/`.
2. Validate that the TTL file is syntactically and semantically correct by
   running the 3 RDF validation scripts:
    - `python scripts/check_rdf_issues.py`
    - `python scripts/check_rdf_entities.py`
    - `python scripts/check_rdf_inverses.py`
3. Run `python scripts/merge_subgraphs.py` to regenerate the full graph at
   `graph/graph.ttl`.
4. Run `python scripts/generate_modal_data.py` to regenerate the JSON data for
   the website at `website/data/modal_data.json`.
5. Make sure the static data in the knowledge graphs section of the website
   (in `website/index.html`) is updated to reflect the applied changes, if
   applicable.

## Add a new subgraph
To add a new narrative work to the knowledge graph, create a new subgraph TTL
file with the appropriate content, validate its syntax and semantics, add a new
narrative card in the website, and then regenerate the derived general graph
and modal data from it.

1. Create a new TTL file for the narrative work in `graph/subgraphs/`, following
   the format of existing subgraph files.
2. Validate that the TTL file is syntactically and semantically correct by
   running the 3 RDF validation scripts:
    - `python scripts/check_rdf_issues.py`
    - `python scripts/check_rdf_entities.py`
    - `python scripts/check_rdf_inverses.py`
3. Add the new TTL file to the `SUBGRAPHS` list in `scripts/merge_subgraphs.py`
   and then run the script to regenerate the full graph at `graph/graph.ttl`.
4. Add the new TTL file to the `MODAL_TTL_MAP` dict in `scripts/generate_modal_data.py`
   and then run the script to regenerate the JSON data for the website at
   `website/data/modal_data.json`.
5. Create the static data in the knowledge graphs section of the website by
   adding a new `kg-card` and `kg-modal` element for the new narrative work in
   `website/index.html`, following the format of existing cards and modals and
   making sure to link the subgraph TTL endpoint in `kg-modal-repo-link` of
   the modal.
