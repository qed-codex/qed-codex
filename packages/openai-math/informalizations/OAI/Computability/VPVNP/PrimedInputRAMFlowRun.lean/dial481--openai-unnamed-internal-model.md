---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMFlowRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlowRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlowRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Execution of a linked structured burst program

The interpreter for a finite control graph consumes one unit of fuel at
each label. Word operations use the native burst opcodes, and branches use
the supplied bit stream. The normal exit is a continuation, so the result
applies both to standalone calls and to blocks inside a larger program.


### `Next`

 Continuation at a label with its updated registers and memory and the
remaining branch bits. 

### `Jump.run`

 Interpret a single labeled jump on the current registers, memory and choice stream, passing
the result to the selected continuation. 

### `run`

 Execute a subgraph with a continuation at its normal exit. 

### `Linked.execute`

 The compiled table and the named control graph have the same execution
on every fuel and branch stream, including rejected and unfinished calls. 

### `template_executes`

 Execute from the entry of the compiled template, with freshly zeroed
registers and private memory. 
