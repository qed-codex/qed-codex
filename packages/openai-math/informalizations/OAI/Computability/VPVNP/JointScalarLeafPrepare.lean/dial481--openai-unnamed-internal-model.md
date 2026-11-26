---
{
  "module": "OAI/Computability/VPVNP/JointScalarLeafPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarLeafPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarLeafPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical preparation and cleanup of a returning signed coefficient query

Copy the exponent payload and blank counters from immutable ports. Prepend
the low row-address bits and the polarity. Switching polarity consumes and
replaces only the first query bit. Cleanup returns the count registers and
the query workspace to empty stacks.


### `copies`

 Four source–destination pairs that initialize the checker query, witness word and two count
operands. 

### `load`

 Copy the packed exponents into the query and the zero templates into the three counter
registers, using the saved-bits stack as scratch. 

### `prefixPorts`

 Connect the row-prefix routine to the leaf’s row register, width template, query stack and
two scratch stacks. 

### `prependRow`

 Prepend the prescribed number of low row-address bits to the query, padding missing high
bits with zero and restoring the row register. 

### `pushSign`

 Prepend the requested polarity bit to the checker query. 

### `switchSign`

 Replace the positive query’s leading false bit with true to select the negative count on
the same row and exponents. 

### `cleanPorts`

 The query, witness and two count-operand stacks cleared at return. 

### `cleanup`

 Clear the query, witness and both count operands to return the leaf bank to its clean call
boundary. 
