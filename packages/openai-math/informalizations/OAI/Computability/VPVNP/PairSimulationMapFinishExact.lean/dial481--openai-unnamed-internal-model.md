---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapFinishExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapFinishExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapFinishExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact native time for the successful width check and label histogram

Each matching width consumes one guard instruction, and a final guard transfers
control to the histogram scan. That scan increments one private counter for each
emitted label, including repetitions.


### `checkSteps_of_all`

 A successful guard sequence reads every tested pair and reaches the final guard. 

### `checkCode_success`

 The complete successful guard chain leaves the counter operands intact. 

### `native_success`

 Matching payload widths give the exact successful path, including the empty
width vector and an empty sequence of emitted labels. 
