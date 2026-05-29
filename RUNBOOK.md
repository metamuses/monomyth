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
      the new version being released as string, e.g. "1.2"
    - `owl:versionIRI`  
      the new version IRI of the ontology, e.g. `<https://monomyth.metamuses.org/1.2/ontology.ttl>`
    - `owl:priorVersion`  
      the previous version IRI of the ontology, e.g. `<https://monomyth.metamuses.org/1.1/ontology.ttl>`
    - `vann:changes`  
      the GitHub _release_ URL for the new version, e.g. `<https://github.com/metamuses/monomyth/releases/tag/v1.2>`
    - `dcterms:modified`  
      the date of the new release in ISO format, e.g. "2026-05-25"
2. Update `graph/graph.ttl` fields:
    - `owl:imports`  
      the new version IRI of the ontology, e.g. `<https://monomyth.metamuses.org/1.2/ontology.ttl>`
    - `owl:versionInfo`  
      the new version being released as string, e.g. "1.2"
    - `owl:versionIRI`  
      the new version IRI of the graph, e.g. `<https://monomyth.metamuses.org/1.2/graph.ttl>`
    - `owl:priorVersion`  
      the previous version IRI of the graph, e.g. `<https://monomyth.metamuses.org/1.1/graph.ttl>`
    - `void:dataDump`  
      the new version IRI of the graph, e.g. `<https://monomyth.metamuses.org/1.2/graph.ttl>`
    - `dcterms:modified`  
      the date of the new release in ISO format, e.g. "2026-05-25"
3. Update `CITATION.cff` fields:
    - `version`  
      the new version being released as string, e.g. "1.2"
    - `date-released`  
      the date of the new release in ISO format, e.g. "2026-05-25"
4. Update `website/docs.html` with the same changes in step 1 for the ontology
   metadata.
5. Update the `CHANGELOG.md` file with the new version and a summary of the
   changes in the release, following the format of previous entries.
6. Create a commit `"Bump version to vX.Y"` and push to GitHub, e.g. `git commit -m "Bump version to v1.2"`.
7. Tag the commit with `"vX.Y"` and push the tag to GitHub, e.g. `git tag v1.2 -m "v1.2"` .
8. Create a release `"vX.Y"` on GitHub from the tag and include the release notes
   with the same summary of changes as in the `CHANGELOG.md`.
9. Check the Zenodo publication for the new synced release being properly rolled
   out: https://doi.org/10.5281/zenodo.20324714
10. Edit the GitHub release notes to include the new version-specific Zenodo DOI
    and the IRI of the versioned ontology and graph, following the format of
    previous releases.
