---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallABIReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallABIReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallABIReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of the six-register shrink map writer

Each emitted operand expression reads from the selected old header, its
incidence and classification tables, or the dense demand and term records
in the completed shrink arena. The same header and arena bounds used by the
native AB gather suffice for the CD lookup and the raw descriptor.


### `Job.abi_descriptor_reads`

 Every external load, including the full scan used to recover the CD
source ID, lies below the terminal controller header. 

### `Job.abi_success_reads`

 The selected handler's entire successful event list reads below the terminal
controller header, including the external setup of its private descriptor. 
