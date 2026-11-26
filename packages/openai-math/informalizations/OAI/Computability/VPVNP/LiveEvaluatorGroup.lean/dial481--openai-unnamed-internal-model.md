---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorGroup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact choice multiplicity of one native live evaluator group

The preparing call is the only call that can consume a choice bit. It
publishes one instruction in scratch and all later calls check its tape
cells without altering memory. The successful preparation bit streams are
in bijection with exactly the nonrejecting choices of the evaluator.


### `SuccessfulStream`

 Accepting native streams after the entire cell scan. 

### `successfulStream_iff`

 No assumptions about which evaluator row or native slot was selected
are needed. The memory contents and choice string determine that selection. 

### `streamEquiv`

 The group preserves path counts, including two slots with the same
successor, without introducing a choice in a deterministic row or carry. 
