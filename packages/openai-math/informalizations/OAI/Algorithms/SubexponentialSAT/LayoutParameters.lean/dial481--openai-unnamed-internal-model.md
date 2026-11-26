---
{
  "module": "OAI/Algorithms/SubexponentialSAT/LayoutParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LayoutParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LayoutParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit parameters and the binomial tail for the interpolation layout

The binomial law is represented by exact integer weights
`choose m w * 3^(m-w)`, of total mass `4^m`.  The central second moment is proved
by the binomial recursion, without any assumed concentration inequality.


### `binomialWeight`

 Integer numerator of `Bin(m,1/4)` at `w`. 

### `weightedSum`

 An unnormalized finite expectation, kept rational for subtraction. 

### `weightedSum_centered_square`

 The exact central second moment, after multiplying the centered variable by four. 

### `binomialWeight_sum`

 The total mass of the exact integer binomial numerators. 

### `intervalStart`

 A consecutive interval centered within a bounded rounding error of `m/4`. 

### `intervalTail`

 Integer numerator of the mass outside `[A,A+R)`. 

### `intervalTail_second_moment`

 Exact finite second-moment (Chebyshev) inequality, with no probabilistic assumptions. 

### `intervalTail_bound`

 A sufficient arithmetic budget converts the second moment into the required tail. 

### `layoutDenom`

 The denominator in the layout's degree choice. 

### `layoutThreshold`

 A deliberately generous explicit sufficient lower bound on `Q`. 

### `arithmetic_of_large_Q`

 The explicit threshold handles the floor loss and the second-moment budget. 

### `tail_of_large_Q`

 The explicit large-`Q` hypothesis implies the actual binomial tail bound. 

### `exists_layout_parameters`

 Existence of all integer parameters in (5.1)--(5.2), with the actual tail
proved rather than included as a hypothesis. Field construction can use this
strictly positive exponent. 

### `binomialProbability`

 The normalized rational probability mass of `Bin(m,1/4)`. 

### `interval_card`

 The interval in the theorem really contains exactly `R` integers. 

### `tail_probability_eq`

 Exact equivalence between the finite tail sum and its integer numerator. 

### `tail_probability_le`

 The integer tail inequality is precisely the probability bound (5.2). 
