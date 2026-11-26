---
{
  "module": "OAI/Computability/VPVNP/BalancedCircuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedCircuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedCircuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Balanced rank decompositions of exact circuits

In Theorem 4.2 of *VP and VNP differ over every field*, a monomial selects one variable
at each of the `ℓ` parties. Its circuit may use arbitrary intermediate monomials. Taking
the queried coefficients of a balanced product expansion yields one matrix on each party
cut. The sum of these matrices recovers the coefficient tensor, and the number of graded
circuit states bounds every matrix rank.


### `cutExponent`

 An assignment to the selected parties, viewed as an exponent of the whole polynomial. 

### `CutFactors`

 Matrix of one cut, including the factorization through a finite state index. 

### `CutFactors.left`

 Left factor of the cut matrix, with one row per assignment of labels in `J` to the
  parties of `S` and one column per state in `B`. 

### `CutFactors.right`

 Right factor of the cut matrix, with one row per state in `B` and one column per
  assignment of labels in `J` to the complementary parties. 

### `CutFactors.matrix`

 Matrix on assignments to the two sides of the cut, obtained by multiplying the factors and
summing over the shared state index `B`. 

### `Circuit.BalancedStates`

 The finite index of all balanced states, for a circuit on party-indexed variables. 

### `Circuit.exists_balanced_cutFactors`

 Every coefficient selecting one variable per party is the sum of factored
cut matrices. An unbalanced cut contributes the zero matrix, and each factorization
uses only the balanced graded states of the given circuit. 

### `Circuit.exists_balanced_matrices`

 Grouping by cut gives the balanced flattening-rank estimate of Theorem 4.2. 
