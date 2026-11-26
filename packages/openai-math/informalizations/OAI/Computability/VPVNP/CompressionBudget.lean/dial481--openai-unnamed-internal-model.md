---
{
  "module": "OAI/Computability/VPVNP/CompressionBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Communication budgets for a compressed pair of groups

Sections 12 and 13 of *VP and VNP differ over every field* compare the
compressed bit count and the number of external accesses with the budget
of a live group. All bounds below are uniform in the choice of compression
terms, with thresholds depending only on the fixed constants.


### `eventually_absorb_polylog`

 Every fixed power of the binary logarithm is eventually absorbed by any
positive gap between two real power exponents, with any prescribed coefficient. 

### `preparation_isLittleO_processors`

 The live address exponent can be fixed after the polynomial preparation
exponent. The multiplicative constant and the polylogarithmic power may
still depend on the chosen address exponent. 

### `eventually_finalWidth_le`

 Equation (12.1) for every energy sequence satisfying the one-block recurrence.
`P` and `W` are the initial position count and width, and `R` is the live site count.
The eventual threshold is independent of these counts and the term choices. 

### `simulationCost_isLittleO`

 Proposition 13.1's external calls and probes use a vanishing fraction of
`R K`. The hypotheses separate the initial geometry, final bit count and the
per-path operation estimate from this asymptotic comparison. 

### `pairSimulation_budget`

 Combine the wire-energy and operation estimates for an entire family of paths.
The final bit count is the sum of the actual final arc widths. Only the per-block
recurrence, initial envelopes, and accounting inequality for the simulated path
are required as input. 

### `regularWire_sqrtEnergy_le`

 In a regular network with `P d` arcs of equal mass, bounding each width by `W`
bounds the initial square-root energy by `P d W`, also for an empty network. 

### `eventually_fieldGrowth_le`

 Field lengths and local monomial degrees satisfy the section 12 exponents
whenever the block growth bound is `C₂^T (W+1)`, with any fixed multiplier. 

### `eventually_burst_le`

 Fetching the incident bits and history descriptors at one final vertex fits
in a live bucket. The fixed number of counter updates may be included in `A`. 

### `eventually_counter_lt`

 With `R ≥ n^5` the total increment from at most `P n^0.01` map occurrences
of degree at most `n^0.4` fits strictly below `R²`, the limit of a `2r`-bit counter. 
