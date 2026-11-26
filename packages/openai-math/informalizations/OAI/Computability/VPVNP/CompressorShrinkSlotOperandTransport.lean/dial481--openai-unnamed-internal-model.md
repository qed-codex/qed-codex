---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotOperandTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotOperandTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotOperandTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Replaying shrinking slot operands after earlier workers

When memory agrees on the original roots, every load computes the same
address. The structural footprint therefore holds in the next memory and
may be widened to the scheduler's persistent operand region.


### `PhaseRecipe.Expr.reads_transport`

 A footprint is preserved when its input cells retain their contents,
including for a load whose address is computed by a nested load. 

### `ShrinkSlotCalendar.rootCell_operandRegion`

 The pitch belongs to the online operand region. Both header intervals
lie in the data suffix, as does the chosen score cell when its address is
at or above the first header. 

### `Stage.eval_transport`

 The evaluated worker bounds and bank agree between the original and
current packet inputs on the same stage, even when the entry layouts differ elsewhere. 
