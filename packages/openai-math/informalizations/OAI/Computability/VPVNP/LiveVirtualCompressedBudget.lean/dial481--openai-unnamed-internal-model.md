---
{
  "module": "OAI/Computability/VPVNP/LiveVirtualCompressedBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualCompressedBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualCompressedBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Accounting for all linked calls of the compressed pair

The online dispatcher reads six workspace words in addition to its own
probes. The compressed-pair linker and the surrounding live-group linker
each read one tag and may write one transfer. The same source report
sequences determine the two margins in the native single-pair specification.


### `linkedRow`

 Both tags are charged on every call, including the final call of a stage. 

### `onlineLogs`

 Online reports after the workspace reads and the two enclosing dispatches. 

### `terminalLogs`

 Terminal reports as executed by the enclosing live pair stage. 

### `wrappedStartup`

 The startup reports, each charged for its own stage transition. 

### `logs`

 The startup, online and terminal reports in their execution order. 

### `linked_caps`

 The eventual per-branch estimates may be invoked with any fixed
constant. A sixty-fourth share for each of the two variable traversals
suffices after both tag protocols and the online pointer reads. 
