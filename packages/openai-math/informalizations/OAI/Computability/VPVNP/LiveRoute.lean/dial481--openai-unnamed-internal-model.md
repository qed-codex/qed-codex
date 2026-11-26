---
{
  "module": "OAI/Computability/VPVNP/LiveRoute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveRoute.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveRoute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Branching between live stages using checked header flags

The routing call reads one word from the group's header workspace. Each of
zero, one, and two can select a stage, accept, or reject. A transfer stores
the selected stage tag at the outer linker's address and returns cursor zero.


### `Target`

 Result of a live router decision, either reject, accept, or jump to the indicated stage
tag. 

### `table`

 Public operands are the tested flag address and the outer stage tag address. 

### `report`

 Explicit report for each selection and any remaining branch bits. 

### `execute_flag`

 Successful routes have exactly the indicated source flag and destination.
Unused choice bits reject, including at an immediate accepting exit. 

### `execute_unknown`

 An unrecognized flag value always rejects. 

### `report_spec`

 A successful source decision consumes no choice and uses at most two
external probes. The jump writes its tag and returns zero, and the accepting
exit leaves memory untouched. 
