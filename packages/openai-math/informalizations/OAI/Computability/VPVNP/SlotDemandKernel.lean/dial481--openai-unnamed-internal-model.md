---
{
  "module": "OAI/Computability/VPVNP/SlotDemandKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotDemandKernel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotDemandKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Repartitioning wire payloads into the AB and CD demands

A thick–thick bundle is one ordered string at A and B. Each demand reads its
contiguous slice at both ends in the same order. This module identifies the
individual old bits with the repartitioned bits and proves the product of
the motif demand coefficients is exactly the original wire-network coefficient.


### `orderedBits`

 Enumerate all bit positions by concatenating fields in the given order. 

### `ThickFiber`

 Old thick–thick wires whose underlying site and port identify bundle `b`. 

### `MotifFiber`

 Shrinking motifs whose CD demand is assigned to bundle `b`. 

### `ThickNumbering`

 The numbering of old wires used at both packed ends. 

### `thickNumbering`

 Choose a bijection from the thick–thick wires in each bundle to the first `2 ^ c * d / 4`
indices when `2 ≤ c`. 

### `demandBitEquiv`

 Pass from an AB slice and its local bit to an old wire and its local bit
through the common offset in the concatenated payload. 

### `abWord`

 Read the AB slice of a single motif at one packed endpoint. 

### `abWords_eq_iff`

 All AB tests together impose precisely equality on every old thick–thick wire. 

### `oldWireNetwork`

 Actual input network of the shrinking step. 

### `outgoingWord`

 Old source word of a directed wire. 

### `incomingWord`

 Old destination word of the same wire, using its original outgoing label. 

### `cWord`

 CD word at its designated thin endpoint. 

### `dWord`

 CD word at its other old endpoint. 

### `demandCoeff`

 Coefficient of the two demand wires read from an arbitrary assignment of
independent old half-wires. 

### `oldWireNetwork_coeff`

 Exact demand factorization for the shrinking step of equation (7.1). 
