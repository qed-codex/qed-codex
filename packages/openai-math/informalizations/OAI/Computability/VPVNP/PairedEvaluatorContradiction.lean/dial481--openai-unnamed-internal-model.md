---
{
  "module": "OAI/Computability/VPVNP/PairedEvaluatorContradiction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairedEvaluatorContradiction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairedEvaluatorContradiction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Proposition 9.1 for the joint compressor evaluator

The label assignment, scalar field and normalized functional all come from
one slice model of the actual grammar and compressor equations. The two
machine-count inputs are the weighted path identity for each primed pair and
the modular path count of the evaluator on its initial exponent tape. The
integer count used for the contradiction is the original paired chain.


### `pairedGroundFintype`

 Finite enumeration of the slice ground field used to instantiate the paired evaluator's
matrix-coordinate arguments. 

### `pairedGroundAlgebra`

 The algebra structure on the ambient field induced by the designated embedding of the
finite slice ground field. 

### `pairedProductionDecEq`

 Classical equality of productions for the finite choices and coefficient comparisons of the
paired evaluator argument. 

### `denseExponent`

 One cell of the physical increment array in dense parser order, followed
by compressor occurrence counts in the fixed motif order. 

### `denseExponent_labelOrder`

 Applying the dense-to-formal coordinate permutation recovers the corresponding
production or compressor count in the joint assignment. 

### `denseExponent_orderAdvice`

 The decoded order-advice word names the formal coordinate at which the
evaluator must receive this dense exponent. 

### `sum_joinedExponents`

 Groupwise exponent accumulation commutes with numbering the joint label list. 

### `PairNomination`

 The parser nominates every production using exactly the paper's `2r` bits. 

### `pairedEvaluatorContradiction`

 An actual tail evaluator cannot satisfy the physical live-count identity
alongside the weighted compressor identities of Section 12. The original
primed site labels and the evaluation functional are read out of the chosen
model of the integer equations. 
