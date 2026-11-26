---
{
  "module": "OAI/Algorithms/SubexponentialSAT/FactorReduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FactorReduction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FactorReduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact count preservation under finite coordinate encodings

This file constructs the validity and clause factors, rather than assuming
equality of their counts with the source problem.


### `solutionEquiv`

 A semantic image characterization gives an actual bijection of solutions. 

### `EncodedSatisfies`

 The unary checks and the encoded local clause checks. 

### `factorScope`

 Each original coordinate receives one unary factor in addition to the
original local constraints. 

### `factorTable`

 An explicit finite table construction. All existential searches range over
finite source alphabets; there is no unbounded semantic oracle. 

### `factorSystem`

 A genuine finite factor system with one unary validity table per coordinate. 

### `assignmentFromChunks`

 Reassemble all chunk bits using an explicit partition of the variables. 

### `cnfScope`

 A clause touches exactly the chunks containing one of its variables. 

### `cnfTable`

 Off-scope variables are assigned false only to make clause evaluation total;
the next theorem proves these default values are never read by the clause. 

### `cnfFactorSystem`

 Actual CNF-to-factor reduction for any injective encoding of each chunk. 

### `packedCNF`

 The concrete finite-label packing from Section 3. 

### `packedCNF_unary_iff`

 The validity table accepts exactly the prescribed initial segment. 

### `primeLabelCNF`

 The same concrete packing into `ZMod p`; primality is only needed later for
field operations, not for count preservation. 
