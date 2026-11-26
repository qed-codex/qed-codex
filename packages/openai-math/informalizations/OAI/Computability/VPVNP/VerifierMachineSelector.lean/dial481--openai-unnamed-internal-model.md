---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineSelector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineSelector.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineSelector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting one transition from the decoded program

The current state and the two symbols under the heads determine a row. The next witness
bit selects its branch. The disjunction tests every possible instruction in that slot
against a Boolean predicate on its fields. It returns false for a halted state, a missing
branch, or an instruction failing the predicate.


### `instructionKey`

 Represent an instruction in the fixed range allocated for an input of length `n`. 

### `selectedExpr`

 Test whether the instruction selected by the current state, scanned symbols, and branch bit
satisfies the supplied predicate. 

### `size_selectedExpr`

 Each possible source and instruction contributes one constant-depth selector term. 
