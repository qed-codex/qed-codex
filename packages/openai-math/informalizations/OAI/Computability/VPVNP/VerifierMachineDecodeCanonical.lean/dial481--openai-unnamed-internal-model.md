---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeCanonical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeCanonical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeCanonical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recognizing the program prefix

A successful decode consumes exactly the canonical prefix of the returned machine. The length of
that prefix bounds the state space to be represented by a verifier on a fixed input length.


### `decode_eq_some_iff`

 An input successfully decodes to a given program exactly when it begins with that program's
self-delimiting code. 

### `tableBits_length_ge`

 A nonempty table spends one unary bit per running state in its header and at least nine bits
per running state on its rows. The empty table satisfies the same bound. 

### `decoded_state_bound`

 A decoded program occupies a unary-framed prefix of length at least twenty bits per running
state, plus the terminator. 
