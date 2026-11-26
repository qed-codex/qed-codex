---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortCompare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortCompare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortCompare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Return values and exact costs of the physical sorting comparator 

### `ready`

 Isolate two records, leaving the supplied tails and destination history
untouched until they are needed. 

### `returned`

 A clean return bank with the new validity bit. The caller may latch
this bit or reject as soon as it is false. 

### `verify_runs`

 Verifying an outgoing slot compares all five raw words and rejects
noncanonical records through the returned bit. No input values affect its clock. 

### `select_runs`

 Select the comparator output and append its reversed five-word encoding
to the backward destination block. All scratch stacks are empty on return. 
