---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGraphStart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphStart.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphStart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Beginning a charged call in the site graph

The first call initializes the global allowance by subtraction. Every call
restores its own allowances, snapshots the start cost, and pays its startup
unit. Its private register bank and memory log are then reset before fetching
the first opcode of the fixed program.


### `Snapshot.afterStart`

 Reset the call allowance, save the starting cost and charge for the new call. 

### `Snapshot.startTicks`

 Instruction count of the call-start credit and reset routine. 

### `Snapshot.afterFresh`

 Initialize private registers and the write log at the template's entry. 
