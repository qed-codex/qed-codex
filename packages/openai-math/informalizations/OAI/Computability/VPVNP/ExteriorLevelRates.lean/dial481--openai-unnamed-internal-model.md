---
{
  "module": "OAI/Computability/VPVNP/ExteriorLevelRates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExteriorLevelRates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExteriorLevelRates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adjacent exterior dimensions

Appendix A, equation (A.2), of *VP and VNP differ over every field* chooses
three adjacent exterior powers of a `Q`-dimensional space. Rounding the real
level `(Q + 1) / (1 + x)` approximates the target adjacent-dimension ratios
`x` and `1 / x` within a factor of four, including the extreme levels.


### `choose_up_ratio`

 The exact upward dimension ratio in (A.2). 

### `choose_down_ratio`

 The exact downward dimension ratio in (A.2). 

### `level`

 The rounded level, capped to leave room for one more generator. 

### `level_bounds`

 Both adjacent binomial ratios attain their target to within a factor of four. 

### `powerLevel`

 The exterior level at tensor power `n` for a marked index of dimension `q`. 

### `powerLevel_log_bounds`

 The error in each *unnormalized* logarithm is at most `logb q 4` for every positive `n`. 

### `exists_level_rates`

 Equation (A.2) along `Q = q ^ n`, simultaneously for the two adjacent dimensions. 

### `choose_adjacent_pos`

 The three exterior dimensions used in (A.2) are all positive. 

### `tendsto_nthRoot_of_logb_rate`

 Exponentiating a normalized base-`q` logarithmic rate gives the limit of nth roots. 
