---
{
  "module": "OAI/Computability/VPVNP/PairShrinkGatherClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkGatherClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkGatherClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform work of the shrinking-party gather

The register-setup text and the list of frames are fixed by the stage, grid
point, party and layout. Each frame reads at most three additional external
words. Only the private bit-copy instructions depend on the row's bit length.


### `allowance`

 Fixed allowance per visited frame, given a coefficient for its payload length. 

### `clockConstant`

 This finite sum depends only on the fixed stage text and the chosen width coefficient. 

### `trace_bound`

 The bound uses the old state's maximum wire width even on surviving subdivisions. 

### `uniform_clock`

 One constant bounds all selected jobs from the entire finite family of stage images. 
