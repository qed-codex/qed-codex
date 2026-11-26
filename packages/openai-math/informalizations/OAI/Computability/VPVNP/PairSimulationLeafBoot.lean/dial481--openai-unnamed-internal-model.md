---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafBoot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafBoot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafBoot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing a cursor-zero leaf from its four half buffers and operand cache

The parent call supplies the decoded node and site addresses, the full O
header, and the cache base. Its private RAM reads the 38 cached words,
computes the stride, and executes the scalar and incident instruction
tables. The result gives the entire private scratch after the last write.


### `ticks`

 Instruction count for cursor-zero startup, including the fixed cache and capacity setup,
scalar stack initialization, and incident-bit copy. 

### `still_stored`

 Word addresses of the four slices precede the private stack arena,
so every word survives the allocation and scalar writes. 
