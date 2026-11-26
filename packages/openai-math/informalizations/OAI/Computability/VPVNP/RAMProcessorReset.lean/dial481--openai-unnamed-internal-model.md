---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorReset.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorReset.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorReset.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fresh private workspace at every burst call

A call starts with one persistent word and its public constants. The processor
overwrites every private register with a width-correct zero and clears the
newest-first write log. Its cost depends on the stored entries, including for
the first call where the physical register stacks may be empty.


### `freshCall`

 Start a private call with width-correct zeroes in all registers and clear the write log's
key, value and occupancy streams. 

### `preCall`

 Before a call the private register bank may still contain bits from a
previous call. The three log streams have a bounded total entry count. 
