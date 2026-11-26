---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackGramPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The shared determinant and scalar-reader ports for the weighted Gram matrix 

### `Aux`

 Auxiliary ports shared by the Schur descriptor, the matrix-entry reader, and the
multiply-and-add routine. 

### `bank`

 Embed the Schur dispatch registers into the descriptor side of the Gram engine's auxiliary
bank. 

### `scratch`

 The temporary stack reserved for the Gram engine's scan and child-call routines. 

### `macPort`

 Embed a multiply-and-add port into the Gram engine's auxiliary bank. 

### `route`

 Route descriptor calls through the Gram engine, sharing the live frame, result, and
condition ports. 

### `extra`

 The descriptor's scalar workspace and matrix reader are ready for a query with column count
`m`. 

### `Ready`

 Entry condition for the Gram engine, combining the dispatch register bank, scratch stack,
scalar arithmetic advice, and reader state. 

### `Pending`

 State of the Gram engine after staging a child query and before activating its six output
words. 
