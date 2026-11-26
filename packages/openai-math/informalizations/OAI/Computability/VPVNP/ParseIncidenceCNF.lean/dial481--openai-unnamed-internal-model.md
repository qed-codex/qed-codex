---
{
  "module": "OAI/Computability/VPVNP/ParseIncidenceCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseIncidenceCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseIncidenceCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Boolean clauses for the local incidence of an ordered parse

Each candidate production has one selection bit. Clauses require a root and both children
of each selected split, exclude ill-typed or conflicting events, and give every nonroot
production a parent. The clauses refer only to selection bits.


### `incidenceCNF`

 Clauses for a designated root and a finite enumeration of candidate productions. 

### `selectedEvents`

 The table whose events have selected flags. 

### `satisfies_incidenceCNF_iff`

 The satisfying assignments select exactly the locally valid tables with the given root. 

### `literalCount_incidenceCNF_le`

 Quadratic bound on the number of literal occurrences read by the query program. 

### `length_incidenceCNF_le`

 Guarding each clause costs at most this many extra literals. 
