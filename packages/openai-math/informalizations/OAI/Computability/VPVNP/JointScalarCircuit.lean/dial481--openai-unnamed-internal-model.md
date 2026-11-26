---
{
  "module": "OAI/Computability/VPVNP/JointScalarCircuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarCircuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarCircuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The advised signed scalar checker

This Boolean circuit takes the raw binary equation address, the formal
exponent array, and a polarity bit. Its witness banks are counted by the
fixed bit-stack enumerator. Inactive banks are forced to zero, preserving
the number of accepting witnesses on the selected branch.


### `parseWire`

 Wire the parse verifier to the low equation-address bits, the formal exponent array and the
parse-event flags of the joint checker. 

### `pathWire`

 Wire the universal-machine path verifier to the low equation-address bits and the clocked
choice bits of the joint checker. 

### `zeroWords`

 Boolean expression testing whether every supplied fixed-width exponent word represents
zero. 

### `Checks`

 The two Boolean outputs retained from the parse verifier and the clocked path verifier. 

### `finish`

 Formal coordinate placements are encoded in the circuit wiring. The
negative grammar branch is enabled precisely for the zero exponent. 

### `frame`

 Use the actual grammar and clock circuits as shared subcircuits on the
same raw inputs. 

### `eval_grammar`

 On a grammar row the sign bit selects either the positive parse count or
the negative constant path count. 

### `eval_motif`

 On a fixed row the signed coefficient is counted by an unsigned witness
comparison. The two machine banks contribute their unique all-zero strings. 
