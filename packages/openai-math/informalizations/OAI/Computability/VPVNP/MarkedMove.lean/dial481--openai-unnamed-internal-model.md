---
{
  "module": "OAI/Computability/VPVNP/MarkedMove.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedMove.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedMove.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Moving one marked tensor index along an identity wire

Appendix A.2 of *VP and VNP differ over every field* bounds the cost of moving
an index of dimension `q` by `q ^ d(a,b)`. The local maps copy the background
indices, pass the wire endpoint at the destination to the output, and pair the
other endpoint with the marked index at its original party. These operations
also apply when both endpoints are at the same party.


### `marked_restricts_move`

 An identity wire supplies a local restriction moving the marked index
from `b` to `a`, over any commutative semiring. 

### `value_marked_le_wire_mul`

 The wire's spectral value bounds the factor required to move a marked index. 

### `value_marked_move_le`

 The elementary index-moving bound of Appendix A.2. 

### `value_marked_eq_zero_iff`

 Vanishing of the marked tensor's spectral value is independent of the placement. 

### `value_marked_eq_of_dist_zero`

 Moving a marked index between parties at zero wire distance preserves its value. 

### `value_marked_eq_of_card_one`

 The placement of a one-dimensional marked index has no effect on its value. 
