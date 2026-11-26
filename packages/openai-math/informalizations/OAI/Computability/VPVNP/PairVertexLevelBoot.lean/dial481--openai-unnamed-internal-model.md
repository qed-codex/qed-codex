---
{
  "module": "OAI/Computability/VPVNP/PairVertexLevelBoot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelBoot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelBoot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Hosted initialization of the descending traversal-level scan 

### `boot`

 Copy the popped row address, form the terminal header and read the first
level header, pitch, stride and number of levels. Start at the last level. 

### `bootEvents`

 The 24 locator-bootstrap events, including reads of the first level, level pitch, row
pitch, and level count in the terminal header. 

### `bootEvents_after`

 The four header probes leave the shared memory unchanged. 

### `BootResult`

 Register and control state delivered by the locator bootstrap before the descending level
scan. 

### `boot_run`

 All 24 instructions execute on the actual host, preserving private memory,
persistent state, and all registers outside the work bank. 
