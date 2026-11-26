---
{
  "module": "OAI/Computability/VPVNP/CompressorInitialClocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorInitialClocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorInitialClocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The block program's source clock within the live pair clock

The inner source reports run at the fixed block program's polylogarithmic
clock. The workspace frame needs twenty-four ticks per call, and the pair
transfer needs three further ticks on a terminating source report.


### `sourceCap`

 Private clock left after the online dispatch and the twenty-four framing instructions. 

### `eventually_clocks`

 The same length threshold supplies the real smaller clock and the
three transfer ticks for every group and every eleven-word operand vector. 
