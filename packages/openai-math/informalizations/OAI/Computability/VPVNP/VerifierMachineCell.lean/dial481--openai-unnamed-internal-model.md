---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineCell.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineCell.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineCell.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One tape cell in the Boolean coefficient verifier

For a fixed candidate move, the destination reads a blank at the boundary, the written
symbol at the old head, and the old symbol at every other source. A disjunction over the
three moves selects this candidate, and a multiplexer preserves the tape on halted branches.


### `movedCell`

 The symbol bit at a destination for a fixed candidate move. 

### `cellNext`

 The new one-hot bit for symbol `s` at tape cell `i`. 
