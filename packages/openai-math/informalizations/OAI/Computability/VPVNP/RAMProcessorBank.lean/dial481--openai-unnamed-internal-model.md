---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared stack bank of the physical burst-site controller

The instruction interpreter and credit routines read the same fuel tally.
The site tests read the same cost and persistent state as the call controller.
Record fields three and four directly name the saved start cost and current
probe ordinal.


### `Port`

 Stacks of the physical site controller for instruction execution, credit accounting, tests,
record emission and temporary work. 

### `localPorts`

 Embed the local instruction processor, sharing its fuel stack with the credit bank and its
choice stream with the site tests. 

### `testPorts`

 Route the cost and cap tests to the credit bank and the state test to the persistent ISA
word, with the other tests on their dedicated ports. 

### `recordPorts`

 Route the record's starting cost and probe ordinal to their live credit stacks and its
other fields to the record buffer. 

### `localBlock`

 One call segment performs the actual instruction fetches and stops on its
external-action label, with private choice bits and fuel updated in the bank. 
