---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineRegisters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineRegisters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineRegisters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean register transitions for the coefficient machine

Each register tests one state or one symbol in a cell of one of the two tapes.
The decoder supplies one bit per transition record. A Boolean choice selects the
branch of the current row, including its write and motion fields. A missing
branch rejects, except for canonical zero padding after an accepting halt.


### `registerStepExpr`

 Formula for one output register, using shared input wires for the decoded table
and the previous configuration. 

### `registerStepExpr_eval`

 Evaluating the next Boolean register gives the corresponding bit of the machine step. 

### `registerStepExpr_size_le`

 One step has quadratic formula size per register in the bound on the number of
states. Its cost is independent of the tape radius, since each destination uses at most
three neighboring cells. 
