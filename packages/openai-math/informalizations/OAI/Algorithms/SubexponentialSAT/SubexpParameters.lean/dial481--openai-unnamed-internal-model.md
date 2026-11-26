---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Growing parameters for the multi-color construction

All finite bounds retain their constants. The asymptotic estimates are uniform
in any incidence bound `Δ ≤ C*(s+1)^d`, where `C,d` remain explicit arguments.
The integer-power characterization of subpolynomial block growth is proved
without interpreting an unbounded search as advice.


### `sizeQ`

 Number of nonzero elements in the fixed degree-four extension. 

### `degreeR`

 Exact integer degree, including the floor. 

### `blockSize`

 Size of the complete type block with `s` colors. 

### `polynomial_le_two_pow_eventually`

 A polynomial of any fixed degree is eventually dominated by `2^n`. 

### `tendsto_div_sixteen`

 The quotient used for the bit capacity tends to infinity. 

### `polynomial_le_two_pow_div_sixteen_eventually`

 The slowly growing prime still dominates every fixed polynomial in `s`. 

### `finite_tail_of_Q_bound`

 A sufficient explicit `Q` threshold for the multi-color Chebyshev test. 

### `quartic_feasible`

 The fixed extension degree four is enough under an explicit prime-size test. 

### `sizeQ_le_dyadic`

 The quartic extension size has a precise dyadic upper bound. 

### `blockSize_pow_le_doubleExp`

 A finite inequality sufficient for every requested fixed power of the block
size to fit below the natural double-exponential scale. 

### `blockSize_subpolynomial_in_s`

 Uniform subpolynomial growth on the logarithmic scale. Constants and the
incidence polynomial degree remain explicit. 

### `blockSize_subpolynomial`

 Concrete `N = n^{o(1)}` statement for the actual computable input schedule:
every fixed natural power of the block size is eventually at most `n`. 

### `blockThreshold`

 The exact threshold appearing in the full-block packing condition. 

### `blockThreshold_mul_ell_le_power`

 A finite reduction of the packing threshold, including the chunk length,
to one fixed power of the universal block size. 

### `blockThreshold_eventually_le_D`

 The block-packing test succeeds eventually for the actual schedule, for
every fixed polynomial incidence bound. 

### `four_mul_degreeR_le_Q`

 The degree choice leaves enough room on both sides of every binomial mean. 
