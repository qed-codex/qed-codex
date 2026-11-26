---
{
  "module": "OAI/Computability/VPVNP/PairCoefficient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairCoefficient.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairCoefficient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The histogram coefficient of a primed pair

For fixed exterior cut bits, `input s v` is the primed bit string at site `v`
when the internal shared bits have assignment `s`. No machine-transcript
validation is imposed on that assignment. Section 9.3 expands the product
of all these sites' label queries over the integers. Its coefficient counts
joint choices of internal bits, ordered parses, and leaf bijections with the
prescribed histogram of terminal and binary productions.


### `Choices`

 Each site makes its own ordered parse and its own assignment of its
terminal occurrences to the distinct queried positions. 

### `jointHistogram`

 All occurrences of one grammar label at all sites of the pair share one counter. 

### `jointPolynomial`

 The polynomial `F` in equation (9.4), before assigning scalars to any labels. 

### `jointPolynomial_eq_sum`

 Fully expand the product over all sites before grouping equal label monomials. 

### `coeff_eq_count`

 Exact multiplicity of each histogram. The integer coefficient includes
every choice of internal bits and every tuple of local parses with this histogram. 

### `histogram_component_le`

 A parse uses one label at each terminal and one at each binary node.
This gives the component bound used for the `2r`-bit nominations in (9.4). 

### `pair_counter_capacity`

 For two groups of `R = 2^r` sites, the paper's `2r`-bit counters cover
all histograms whenever `4n ≤ R` and the layer has degree `n`. 

### `evaluate_by_nominations`

 Nominate every histogram whose individual counters fit in the chosen
fixed width. Evaluating the primed pair polynomial over any field or
commutative ring sums its monomials with the number of matching parses. 
