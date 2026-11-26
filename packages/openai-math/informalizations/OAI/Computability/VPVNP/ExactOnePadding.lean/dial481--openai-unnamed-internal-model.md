---
{
  "module": "OAI/Computability/VPVNP/ExactOnePadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOnePadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOnePadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A dummy variable for exact-one instances

The Hamiltonian graph needs at least one variable track. Adding a final variable
and a singleton negative clause gives each old assignment a unique extension
with the same weight, including when the original instance has no variables.


### `pad`

 Embed the old variables as the initial coordinates and force the final one to false. 

### `padProjection`

 The forced coordinate carries the unit label. 

### `holds_pad_iff`

 The old coordinates retain all the old constraints. 

### `weightedExactOne_pad`

 The added variable has weight one in every satisfying product because it is forced false. 

### `weightedExactOne_padProjection`

 Variable-or-constant labels of the original exact-one polynomial lift to the padded graph. 
