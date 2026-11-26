---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkScoreVisits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScoreVisits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScoreVisits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Typed planner launches for the score workers 

### `Stage.fuel`

 Per-call instruction budget for a score worker, seven for clearing, twenty-seven for an
axis, and ten for comparison. 

### `Readback`

 Relates the planner operands to the native score table by matching the term base, motif
count, term stride, selector width, score base, and layout cell. 
