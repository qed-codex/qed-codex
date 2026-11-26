---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterAdminExec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdminExec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdminExec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Straight-line executions of scheduled calls

A straight-line trace gives the exact events, registers and memory of the corresponding
structured body. Its instructions consume no choice bits. The scheduled call rejects any
surplus bits when it compares the next cursor with the total and halts or returns.


### `exec_lines_iff_trace`

 Compiling a nonempty list of lines preserves and reflects its entire trace. 

### `trace_choiceBits`

 A successful straight-line trace contains only ticks, reads and writes. 

### `call_reject_nonempty`

 A call whose body consumes no choices rejects every nonempty tape, for every fuel. 

### `lines_call_reject_nonempty`

 A scheduled straight-line body rejects every nonempty choice tape. 
