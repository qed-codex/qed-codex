---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorPhysical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorPhysical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorPhysical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Evaluator inputs and outputs from the actual physical header

The live header parser supplies the mode, the two router flags, the raw cut
field and the zero-default outgoing endpoint. This proof reconstructs the
outgoing case at every evaluator group and the incoming field at every
noninitial group, without assuming well-formed configuration words.


### `sizes`

 The evaluated header dimensions used to recover the evaluator routes from the physical cut. 

### `headerBase`

 The physical header workspace base for the current evaluator group. 

### `headerEnd`

 The first address past the group's live-header buffers. 

### `physicalOutput`

 The actual header supplies every outgoing constructor input. A last cut
uses the zero-default memory beyond the header allocation. 

### `physicalIncoming`

 The incoming zero-flag case recovers its actual raw array from the left
incident cut. The semantic boundary includes its mode and padding tests. 
