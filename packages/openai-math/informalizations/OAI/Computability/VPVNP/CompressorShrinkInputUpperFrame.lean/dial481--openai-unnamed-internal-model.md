---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkInputUpperFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkInputUpperFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkInputUpperFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The upper frame of the pre-selection input scans

The complete greedy, placement, ranking and width scans access the old
incidence data and the freshly allocated input arena. Their stores preserve
every address at or above the arena's exclusive end.


### `input_access`

 Bounds on all sixteen deterministic input segments before the absolute-ID
scatter. The old width and incidence columns can be anywhere below the arena. 
