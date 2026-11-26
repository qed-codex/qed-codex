---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwnerAux.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerAux.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerAux.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native initialization of the auxiliary endpoint owner tables

One eight-cell scan writes the selected layout's A, B, and D column offsets.
Another scan rotates the tag digit of each site, keeping its vertex and lane.
Both tables are produced by fixed straight-line programs, using one write per
cell and no external reads.


### `roleCode`

 The edge type has two binary digits. Its incoming end has role D precisely
when the digits differ. Its outgoing end has role D only on the last type. 

### `roleValue`

 Select the role-site offset for an edge type and endpoint side in the chosen layout, using
the low cursor bit for the side. 

### `roleValue_eq`

 The program implements the selected layout's outgoing and incoming roles
on all eight entries of the finite role table. 

### `nextCode`

 Public fields give lane count, tag count and cyclic successor table start. 

### `nextValue`

 Compute a packed site's cyclic successor by advancing its tag modulo the tag count at the
same base vertex and residual lane. 

### `nextValue_eq`

 Numeric cycle with the same original vertex and lane even when the tag wraps. 

### `roles_run`

 Fill the finite role table. Its final cells are the role offsets needed
by the selected layout, with the outgoing cell first in each pair. 

### `next_run`

 Build the entire cyclic successor table directly from the two radices.
The result satisfies the input predicate used by the native dummy worker. 
