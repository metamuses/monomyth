from rdflib import Graph
from rdflib.plugins.parsers.notation3 import BadSyntax
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
GRAPHS_DIR = ROOT_DIR / "ontology/graphs"

g = Graph()

for ttl_file in sorted(GRAPHS_DIR.glob("**/*.ttl")):
    try:
        print(f"Loading {ttl_file}")
        g.parse(ttl_file, format="turtle")
    except BadSyntax as e:
        print("\nTurtle syntax error")
        print(f"File: {ttl_file}")
        print(f"Line: {getattr(e, 'lines', 'unknown')}")
        print(f"Message: {e}")
        sys.exit(1)
