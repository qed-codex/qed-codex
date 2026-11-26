---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorChargedRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorChargedRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorChargedRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking the per-instruction call simulation to the bucket loop

The startup unit is charged before execution. A site with no remaining
credit rejects at startup. Successful startup resets the registers and log,
and the segment simulation then follows the real instruction table.


### `startRuns_of_segments`

 Fold the concrete call induction through both startup labels. 
