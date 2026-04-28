from rdflib import Graph, URIRef
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
GRAPHS_DIR = ROOT_DIR / "ontology/graphs"

BASE_URI = "https://monomyth.metamuses.org/graph/"

g = Graph()

for ttl_file in GRAPHS_DIR.glob("**/*.ttl"):
    print(f"Loading {ttl_file}")
    g.parse(ttl_file, format="turtle")


def is_local_resource(node):
    return isinstance(node, URIRef) and str(node).startswith(BASE_URI)


resources = set()

for s, p, o in g:
    if is_local_resource(s):
        resources.add(s)
    if is_local_resource(o):
        resources.add(o)

orphans = []

for resource in resources:
    incoming_local_links = [
        (s, p) for s, p in g.subject_predicates(resource) if is_local_resource(s)
    ]

    if not incoming_local_links:
        orphans.append(resource)

print("\nOrphans:")
if not orphans:
    print("  => None")
else:
    for orphan in sorted(orphans):
        print(f"  => {orphan}")
