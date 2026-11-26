---
{
  "module": "OAI/Computability/VPVNP/MarkedTensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedTensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedTensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local operations on marked tensor indices

In Appendix A, the same coefficient table can place its marked indices at
different parties. Each party retains its background basis while receiving one
factor for each marked role assigned to it. These local operations describe
the arrays in the two orders of the exterior-algebra splitting identity.


### `MarkedArray`

 A table on the background bases and additional marked indices. 

### `placedWith`

 Place all marked indices while retaining the original background basis at
 each party. This applies when multiple roles have the same party. 

### `marked`

 One marked index, keeping the background bases unchanged. 

### `placedWithEquiv`

 A complete assignment of local indices to a placed tensor is equivalently
an assignment of the background indices and one index per role. 

### `markedEquiv`

 Move one extra factor into party `a`'s local basis, carrying it there as a function on the
equality witness. 

### `placedEquiv`

 Regroup role-indexed factors by their assigned parties, with one factor for each role
placed at a given party. 

### `contract_marked_operator`

 Identity matrix on the background and new marked indices, and a local
pairing between the old marked index of the tensor and that of an operator. 
