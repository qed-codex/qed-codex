---
{
  "module": "OAI/Computability/VPVNP/AdviceInterpreter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceInterpreter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceInterpreter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit-stack interpreter for Boolean circuit advice

The stream contains a gate tag followed by one or two unary operand addresses.
Each lookup preserves the valuation stack. The gate body removes its operand
bits from scratch and prepends its result to the valuation stack. The control
and the four stacks are fixed independently of the circuit, input and gate count.


### `routine`

 Executable instruction loop. An exhausted advice stream returns to the caller. 

### `routine_runs`

 A successful abstract execution is implemented by at most sixteen stack
instructions per advice bit, including the final end-of-stream test. 
