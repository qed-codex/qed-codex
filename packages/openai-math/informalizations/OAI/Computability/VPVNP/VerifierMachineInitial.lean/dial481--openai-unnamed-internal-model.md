---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineInitial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineInitial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineInitial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading the coefficient machine's Boolean registers

An initial state bit reads the decoder's empty-program flag or its complement.
At a first-tape input position the symbol-two register reads the input bit, and
the symbol-one register reads its complement.
All other cells initially contain the blank symbol.


### `initialRegisterExpr`

 Initialize each one-hot register using at most a single input and a negation. 
