---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotOrdinals.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotOrdinals.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotOrdinals.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Guarded cursors of the shrinking slot program

Each successful slot worker advances the dense ordinal by exactly one,
including the guarded append into an owner's row. A run whose writes lie
outside the active scheduler controls passes every dispatch guard when
the initial row is ready and its exclusive stop fits the word.


### `Stage.advance`

 The cursor result comes from the actual instruction table. The assertion
holds for arbitrary public words and memory whenever the reset call succeeds. 

### `Source.validTrace`

 A guard proof may use the writes of the actual source log. The induction
invariant keeps its remaining successful zero-tape suffix. Consequently only
the real writes need to be disjoint from scheduler control cells. 
