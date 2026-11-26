---
{
  "module": "OAI/Computability/VPVNP/CompressorEvaluatorChain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorChain.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorChain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two coefficient identities used by the diagonal chain

The joint label algebra evaluates the primed contraction to the original
integer count, and its monomial evaluator reads the production and compressor
exponents together. Accumulating the exponents across pairs permits a single
application of the functional to the entire product in the evaluator tail.


### `chainGroundFintype`

 Finite enumeration of the slice ground field used in the joint coefficient evaluation. 

### `chainGroundAlgebra`

 Scalar action of the slice ground field on the ambient field through the chosen slice
embedding. 

### `productionValues`

 Grammar specialization in the algebra chosen for both compressor blocks. 

### `compressorValues`

 The same slice point specifies all shrinking and refresh map entries. 

### `compressorEvaluator_primed`

 The primed chain uses the actual grammar solution in the common finite algebra. 

### `compressorEvaluator_monomial`

 Evaluate a single monomial consisting of production labels and fixed
compressor labels. The coordinate numbering agrees with the joint equations. 

### `compressorEvaluator_pair_product`

 After the chain accumulates one pair's exponents at a time, the tail
counts precisely the functional applied to the product of all pair weights. 
