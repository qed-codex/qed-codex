---
{
  "module": "OAI/Computability/VPVNP/VerifierMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean circuits for the coefficient verifier

The input consists of the word and one choice bit per clock tick. The first circuit
decodes the transition table from the word. The next layer initializes the tape windows,
and the simulation applies one transition per choice bit. This gives a polynomial-size
Boolean verifier for the coefficients in equation (1.1).


### `verifierFrame`

 The final Boolean circuit checks that the literal program is valid and that its
canonical path choices end in acceptance after the universal clock. 

### `verifierSize`

 Size of the compiled verifier, counting binary AND and unary NOT gates. 

### `verifierCircuit`

 The single-output Boolean circuit on the input bits and its canonical path-choice bits. 
