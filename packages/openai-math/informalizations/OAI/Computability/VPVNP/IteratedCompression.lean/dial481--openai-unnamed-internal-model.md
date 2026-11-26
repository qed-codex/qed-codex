---
{
  "module": "OAI/Computability/VPVNP/IteratedCompression.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IteratedCompression.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IteratedCompression.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iterated compression with a fixed system of wire identities

Theorem 7.1 of *VP and VNP differ over every field*. The expansion here uses
the packed six-party substeps and the port refresh on the actual lifted
slots. Its finite templates, degree schedule, number of lane coordinates
per block, energy allowance, and per-vertex history bound are fixed before
choosing a network or the number of blocks.


### `procedure`

 Execute the fixed shrinking degrees followed by the expander refresh. 

### `procedure_error_eq`

 The additive energy error is the same in every ring realizing the templates. 

### `widthAllowance`

 Fixed coefficient of the initial position count in the shared-width bound. 

### `recordLimit`

 Uniform bound on each substep's records at a single vertex. 

### `growthConstant`

 The paper's `C₂`, enlarged to at least two. 

### `recordBounds`

 Local records are those of the constructed wire identities at each chosen site. 

### `execute`

 `T` complete blocks on an input with any sufficient number of lane coordinates. 

### `records`

 The complete history of actual records on every branch of `execute`. 

### `branch_bounds`

 Every branch restores the base degree, satisfies the shared-width saving
(7.4), and keeps all intermediate fields, individual map-entry degrees and
recursive vertex expansions within the stated exponential-in-block bounds. 

### `execute_contract`

 The exact identity behind the estimates holds against any original
vertex factors, including those carrying fixed external indices. 

### `exists_iterated_compression`

 Theorem 7.1. The degree schedule and integral templates are chosen once,
before specializing the coefficient ring or selecting the input. Their
quantitative conclusions for every term are `Templates.branch_bounds`, and
their exact contraction identity is `Templates.execute_contract`. 

### `fixed_templates_of_small_circuits`

 The small-circuit contradiction fixes both templates and a joint field
assignment before the simulation is instantiated at any particular length.
Every sufficient input length and block count can then use the same
`Templates.execute`, `Templates.branch_bounds` and `Templates.execute_contract`. 
