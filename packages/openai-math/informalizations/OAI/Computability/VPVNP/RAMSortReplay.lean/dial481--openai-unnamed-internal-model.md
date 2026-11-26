---
{
  "module": "OAI/Computability/VPVNP/RAMSortReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local replay of the distributed sorting layers

A site keeps its current records and reads the matching site's send field
only at a cross-site stride. The local check at every such layer compares
its outgoing field with its own pre-comparison block. For a fixed input all
send fields are uniquely determined by these checks, and the final records
at each site agree with the globally addressed bitonic network.


### `Stage`

 One comparator layer in an array with `2^b` positions. 

### `Stage.phase`

 Bitonic merge phase exponent, whose bit in the global wire index selects the comparison
  direction. 

### `Stage.stride`

 Bit position toggled in the wire index to find its comparator partner in this layer. 

### `strides`

 The last `k` layers of phase `a`, in the order of execution. 

### `phases`

 All layers in phases one through `a` of a fixed-width array. 

### `Sends`

 Exactly one block is sent by each site on a cross-site layer. A local
layer has a unique empty field since its domain `h ≤ s.stride` is empty. 

### `Fields`

 Chronologically arranged outgoing fields. Each receive is addressed to
the corresponding field of its partner site. 

### `sourceSite`

 Arithmetic address of the unique sender supplying this entire block. 

### `localLayer`

 Update one site's block. Internal strides read both records locally.
Cross-site strides read the partner's outgoing block at the same offset. 

### `localLayer_block`

 Sending the actual pre-comparison records produces the same local block
as the XOR comparator layer. 

### `checks`

 All outgoing fields agree with this site's computed records. 

### `replay`

 The site's final records, computed only from its local input and the
cross-site receive fields. 

### `actual`

 The actual pre-comparison blocks sent throughout a sequence of layers. 

### `fields_eq_actual`

 The local send checks determine the entire exchange transcript uniquely. 

### `replay_phases`

 A locally accepted exchange reconstructs the correct globally sorted
records at every site. 

### `existsUnique_fields`

 For fixed records there is exactly one assignment of cross-site send fields. 
