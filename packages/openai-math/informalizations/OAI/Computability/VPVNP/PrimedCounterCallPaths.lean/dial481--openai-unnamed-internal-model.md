---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterCallPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterCallPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterCallPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading back a native call of the scheduled pair counter

The final tick compares the next cursor with the total count. Recovering
the structured execution before that tick yields both the consumed binary
tape and the post-call external memory used by the next scheduled item.


### `exec_memory`

 Report replay has exactly the external-memory effect of the structured body. 

### `execute_iff`

 Exact decomposition of a successful native call. The inequality counts
the body events, the cursor comparison and the terminal return/accept opcode. 
