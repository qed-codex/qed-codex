---
{
  "module": "OAI/Computability/VPVNP/RankQueryDescribeArms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryDescribeArms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryDescribeArms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Terminal and arity arms of the physical Schur dispatch 

### `Wire`

 Auxiliary stacks used by the description arms, comprising six descriptor words, the
extension modulus coefficients, and two scratch stacks for writing field literals. 

### `livePort`

 Embed one of the ten live Schur frame slots into the stack ports of the interpreter. 

### `signal`

 Push the descriptor branch bit onto the engine's condition stack. A true bit signals a
returned scalar and a false bit starts a child scan. 

### `literalPorts`

 Connect the constant writer's input and work stacks to the coefficient, extra and scratch
wires, and send its packed scalar to `out`. 

### `literal`

 Write the packed scalar one for `true` or zero for `false` to the selected engine port,
using the field advice on the coefficient wire. 

### `livePorts`

 The ten stacks holding the current Schur frame, in field order, which the terminal arm
clears on return. 

### `finish`

 Clear the ten live frame fields and push the true return signal once the scalar result is
in place. 

### `terminal`

 Return the constant selected by `b` from a Schur leaf by writing its packed scalar,
clearing the live frame and signaling completion. 

### `arity`

 Start a child scan by copying descriptor word one into the remaining-child count, setting
the scalar accumulator to zero and pushing the false signal. 

### `Clean`

 The coefficient wire holds the packed vector `c` at limb width `v`, and the scratch and
extra wires are empty for a constant write. 

### `constant`

 The scalar selected by a constant descriptor in `Scalar c`, equal to one for `true` and
zero for `false`. 
