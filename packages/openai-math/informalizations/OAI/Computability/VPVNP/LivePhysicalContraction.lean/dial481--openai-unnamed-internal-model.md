---
{
  "module": "OAI/Computability/VPVNP/LivePhysicalContraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePhysicalContraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePhysicalContraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The integer count from the physical live program

The group program's specification is local. On each group it checks the two
incident mode bits, then accepts in unit mode or runs the first-half pair or
the tail transition. Reindexing the raw shared bits and summing these native
counts yields one unit path plus the full evaluator sum, on the same processor
prefix and advice as the primed contraction.


### `groupEvaluation`

 First-half and tail checks, selected by the one-based group number in
its header. Agreement of the mode bits is imposed separately. 

### `specifiedGroupCount`

 The integer count required from one native group, including mixed mode,
clamped endpoints, and failure of a first-half or tail check. 

### `groupEvaluation_incoming`

 Every nonzero product supplies the canonical incoming first-half or tail
format from the predecessor's own successful outgoing check. 

### `specifiedGroupCount_product`

 At fixed physical cuts, enforcing both incident formats in each
group preserves the original product. A malformed incoming cut already
forces a zero factor at its predecessor. 

### `physical_two_modes`

 The integer identity from Section 14.3, reduced to the native site and
single-group specifications. It holds for the very same prefix whose clocked
path count occurs in the integer family. 
