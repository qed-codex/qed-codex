---
{
  "module": "OAI/Computability/VPVNP/BooleanTranscript.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BooleanTranscript.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BooleanTranscript.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean gate transcripts

Section 1.1 of *VP and VNP differ over every field* represents a deterministic
Boolean verifier by summing a product of local consistency tests over all gate
values. Each gate in the verifier may reuse any previously computed gate. On
Boolean inputs the product singles out its unique transcript over every field.


### `bit`

 Encode a Boolean value by the corresponding ring element. 

### `equalBit`

 Equality test on two Boolean-valued elements of a ring. 

### `Gate`

 AND and NOT with topologically ordered references, a complete Boolean gate basis. 

### `Gate.eval`

 Compute the Boolean result of an AND or NOT gate from its referenced inputs and earlier
wires. 

### `Gate.arith`

 Interpret AND as multiplication and NOT as subtraction from one in the coefficient ring. 

### `Program`

 A Boolean program built by adjoining one gate at a time. Each new gate can refer to all
preceding gates. 

### `Program.run`

 The Boolean value at each gate after running the program on the given inputs. 

### `Program.check`

 Product of all gate tests, evaluated on a proposed transcript. 

### `Program.check_bits`

 The gate tests have value one at the true transcript and zero at every other
Boolean transcript. This is an identity over any commutative ring. 

### `Circuit`

 A Boolean program together with the reference whose bit is returned to the verifier. 

### `Circuit.program`

 The ordered gates whose computed bits form the transcript. 

### `Circuit.output`

 The input, Boolean constant, or gate bit chosen as the circuit's result. 

### `Circuit.eval`

 Evaluate the program on the Boolean input and read its designated output bit. 

### `Circuit.weight`

 The transcript tests multiplied by the acceptance indicator. 

### `Circuit.sum_weight_bits`

 Summing over gate assignments recovers the Boolean verifier's answer. 
