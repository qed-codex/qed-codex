---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSwapMultiplicity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSwapMultiplicity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSwapMultiplicity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multiplicities of register-swap eigenvalue labels

The negative local labels are strictly below the diagonal and the positive
labels are on or above it. Counting these labels and their tensor words is
independent of the characteristic of the coefficient field.


### `supportFiberEquiv`

 Prescribing the negative positions leaves independent negative and
positive label choices on the two parts. 

### `card_weight`

 Exact tensor multiplicities for any finite positive/negative alphabet. 

### `multiplicities_add`

 The positive and negative labels account for every ordered pair. 

### `sum_swap_multiplicities`

 Total tensor multiplicity; neither the number of registers nor the
number of positions is hidden as a fixed parameter. 

### `negativeProbability`

 Probability of a negative local eigenvalue for a uniformly chosen
ordered pair label. 

### `swapProbability`

 The uniform word measure, expressed with exact rational arithmetic. 

### `swapProbability_eq_binomial`

 Exact binomial probability mass function of the negative weight. 

### `swapProbability_Q_eq_binomial`

 The source paper uses precisely `Q - 1` independent register pairs. 

### `negativeProbability_bounds`

 The local negative probability belongs to the range used in the paper. 

 ## General binomial second moment and the interval tail 

### `binomialExpectation`

 Finite expectation for a binomial parameter `θ`; no special value of
the parameter is built into the recurrence or moment identity. 

### `binomialExpectation_succ`

 Adding one independent Bernoulli coordinate, proved by Pascal's identity. 

### `binomialExpectation_centered_square`

 The exact central second moment for every rational parameter. 

### `tail_second_moment`

 A finite Chebyshev inequality for the actual swap probabilities. The
geometric hypothesis says every omitted weight is at least `R/4` from the
actual mean, in squared form. 

### `tail_chebyshev`

 The uniform variance bound `θ(1-θ) ≤ 1/4` loses no dependence on `r`. 

### `tail_bound_of_budget`

 The source's arithmetic budget implies the required normalized tail,
once the interval geometry is supplied. All parameters remain explicit. 
