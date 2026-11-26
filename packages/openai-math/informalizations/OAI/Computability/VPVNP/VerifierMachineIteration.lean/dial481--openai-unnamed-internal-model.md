---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineIteration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineIteration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineIteration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iterating the universal verifier on its bounded tape window

One circuit layer consumes the next choice bit and computes the next configuration.
The decoded table and the input and choice bits remain accessible by wire references
at every layer. After exactly `T` layers the circuit tests validity and the accepting state.


### `Slice`

 Inputs and choices, decoded table flags, and configuration registers for a radius-`r` window. 

### `simulate`

 Append exactly one Boolean circuit layer per choice bit, in order. 

### `simulate_eval_register`

 All bounded configuration bits after `T` layers encode the run on the supplied choices. 

### `accept`

 Circuit output after executing the entire witness and checking that its table was valid. 

### `accept_size_le`

 The simulation has a fixed width, and the output test uses three more circuit nodes. 
