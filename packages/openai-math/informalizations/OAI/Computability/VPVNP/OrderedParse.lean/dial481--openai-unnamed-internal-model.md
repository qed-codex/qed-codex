---
{
  "module": "OAI/Computability/VPVNP/OrderedParse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OrderedParse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OrderedParse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite ordered parses

A parse of layer `d` has `d + 1` terminal occurrences. At a binary production, the
split records the layer of the left child, and the two state labels specify the roots
of the child parses. The root state of the entire parse is supplied by the grammar.


### `OrderedParse`

 Ordered binary parse with terminal variables, child states and fixed leaf count. 

### `leafEquiv`

 A parse in degree one is determined by its sole terminal. 

### `nodeEquiv`

 Decompose a binary parse into its split, child states and ordered subtrees. 

### `leaves`

 Terminal word, read from left to right with multiplicity. 
