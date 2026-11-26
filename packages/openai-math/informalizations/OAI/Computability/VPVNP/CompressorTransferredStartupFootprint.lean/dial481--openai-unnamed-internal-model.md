---
{
  "module": "OAI/Computability/VPVNP/CompressorTransferredStartupFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTransferredStartupFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTransferredStartupFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Protected low memory across the eight native startup calls

Each source report preserves every cell below the descriptor workspace. The
linker writes its tag after each report, so every other low cell retains its
initial value at all nine entries. These statements use the reports of the
linked machines on the actual intermediate memories.


### `Runs.source_below`

 The native source of every transfer keeps the protected low memory. 

### `Runs.entry_below`

 Every prefix, including the last transfer to the online worker, preserves
all low cells outside the pair tag. 

### `Runs.after_source_below`

 The post-memory of any of the eight source reports also agrees with the
original input on every protected address. 
