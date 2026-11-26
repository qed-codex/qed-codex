---
{
  "module": "OAI/Computability/VPVNP/Diagonal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Diagonal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Diagonal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The paired-chain contraction in Proposition 9.1

`Cut` indexes all assignments to the exterior cuts of the primed pairs.
`Path ξ i μ` indexes the successful local paths for pair `i` at exterior
assignment `ξ` and nominated production histogram `μ`. The weights below
are the values of the corresponding label monomials in the coefficient algebra.

The algebraic argument uses linearity only after multiplying the weights of
all the pairs. The local simulation, equality with the original contraction,
and realization by the live program are explicit hypotheses of the criterion.


### `evaluationMode`

 Sum of the tail contributions over cuts, nominations, and local paths. 

### `primedContraction`

 Equation (9.5) evaluated in the coefficient algebra, using the
production coefficients in (9.4). 

### `originalContraction`

 Equation (9.2), with an assignment to the shared bits split into the
exterior cuts `ξ` and the internal bits `s i` of each pair. The sites in
pair `i` contribute the product of their integer path counts. 

### `primedContraction_eq_original`

 Replacing the site counts using (8.1) and expanding each pair by
(9.4) preserves the original contraction, as in (9.3) and (9.5). 

### `evaluationMode_eq`

 The weighted path identities for individual pairs determine the entire
evaluation-mode sum, even when the tail functional is not multiplicative. 

### `labelMonomial`

 The value of a label monomial with the given vector of exponents. 

### `labelMonomial_accumulate`

 Adding the exponents along the chain produces the same element of the
coefficient algebra as multiplying the local label monomials. 

### `evaluationMode_accumulated`

 Apply the evaluator to the accumulated exponents exactly once at the tail
of the chain. Its scalar contributions then sum to the evaluation-mode count. 

### `pairedChainCriterion`

 Algebraic contradiction of Proposition 9.1. The count `Y` is the
original integer path count. The primed contraction represents that count
in `A`, while the live program counts one unit path plus evaluation mode
in `k`. Taking `k = ZMod p` gives the paper's contradiction modulo `p`. 

### `OriginalPaths`

 The configurations counted by the original chain. For fixed cut bits and
internal bits, each site chooses one of its accepting paths independently. 

### `LiveModes`

 The paths produced by the two live modes. In evaluation mode the tail
has a separate contribution for each sequence of branch choices. 

### `noPairedChainSimulation`

 Proposition 9.1 in terms of the asserted path bijection, sitewise
coefficient equations, local weighted simulations, and tail path counts.
Canonical cut fields and padding in the live program ensure that its
evaluation mode has exactly the path multiplicities in `LiveModes`. 
