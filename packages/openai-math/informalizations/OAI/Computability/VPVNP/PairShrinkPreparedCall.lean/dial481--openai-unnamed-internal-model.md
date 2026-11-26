---
{
  "module": "OAI/Computability/VPVNP/PairShrinkPreparedCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPreparedCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPreparedCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A native map-call descriptor from a selected shrinking term

The real demand and supply readbacks, the recorded branch widths and the
private workspace intervals supply every input of the compiled descriptor
writer. These facts hold for arbitrary choices of the local half-wires and
absorbed words, including data on which the grouped entry test rejects.


### `noncomputable local instance : DecidableEq X.Base`

 Classical decidable equality on the compression state’s base vertices for the native
map-call descriptor of a selected shrink term. 

### `widthsDemand`

 Demand widths of a motif computed from the numbering and wire widths of the input state. 

### `width`

 Supply widths of a motif for the term chosen by the shrinking selection. 

### `input`

 The full selected input, with the original matrix coordinates at this party. 

### `values_eq`

 The descriptor's scalar and address words agree with the map initializer's
precise ABI, including its separate directory, ordinal and label addresses. 

### `resident`

 Every incident bit is the local matrix's actual coordinate. Descriptor
writes and the directory fill are disjoint from all these reads. 
