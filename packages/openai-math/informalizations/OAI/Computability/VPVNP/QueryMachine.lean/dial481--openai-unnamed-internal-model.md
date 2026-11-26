---
{
  "module": "OAI/Computability/VPVNP/QueryMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clocked simulation of a finite query program

For every query the head scans to the end of the input, then back to the selected payload
bit. The bound allows one final transition into a halting state, including on query timeout.


### `correct`

 At every clock above the bound the literal table counts exactly the query result. 
