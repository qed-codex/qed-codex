---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Exterior/Strips.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Exterior/Strips.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Exterior/Strips.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Padding exterior stacks to whole rows

Reserve one partial row per occupied holder. Unused slots receive
dummy stacks so the reindexing is a bijection on a fixed tape.


### `Grouping`

 A genuine stack and its padding copy occupy distinct slots. 

### `needed`

 Ceiling of the stack count divided by the capacity `q`, with
zero rows for an unoccupied holder. 

### `orderedSlot`

 Within each holder the rank fixes both the local row and offset. 

### `group_order`

 If one row per occupied holder fits in the padding budget, doubling
the stack count suffices, preserving any prescribed order inside each holder. 

 # Canonical port ordinals for exterior stacks 

### `stack_slot`

 The position of a stack on its channel depends only on the
stack indices present at the same occurrence. 

### `point`

 All finest bundles of a stack are consecutive at its port. 

### `port_ordinals`

 If names sharing a holder always use different channels, the
port ordinals enumerate exactly the stacks of one name at that holder. 

 # Aligning exterior stacks with the port rows of a contraction 

### `pack_ports`

 For the prescribed port order, all active exterior rows pair
one-to-one with their inside rows. The within-row offset is unchanged. 


# Arity of the short exterior sorts

Stack addresses grow at most quadratically in the beat count. The
payload covers the address, and the logarithm of the entire table
arity fits both caps for a short sorting vertex.


### `recipe_limits`

 Apply both caps to the height and bundle width chosen by the batch recipe. 

 # Exterior row capacity and channels on the reduced host 

### `channels`

 Assign local channels to exactly the exterior names reaching a site. 

### `capacity`

 Relative to one original name, the tail blocks pay for the final
partial row at every holder. 

### `load_eq`

 The external port inventory counts all exposed bits, in units of
final bundle width. 

 # Naming the finest exterior bundles by their source stack 

 # Exterior descriptors for a canonical port layout 

### `Descriptor`

 The name belongs to the row. Only the stack address is needed for
each active payload inside that row. 

### `make_descriptor`

 Construct a descriptor for the rows that actually carry exterior
stacks. The output agreement is stated at every finest bundle. 
