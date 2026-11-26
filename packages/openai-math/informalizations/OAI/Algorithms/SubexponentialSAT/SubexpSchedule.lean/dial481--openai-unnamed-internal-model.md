---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The actual input-dependent parameter schedule

The width `k` is fixed before the input is supplied. All other displayed
parameters are computed from the prepared variable count. The reciprocal
sparsification budget is tested by exact natural-number arithmetic, and the
prime comes from the bounded search in `SubexpPackingParameters`.


### `M`

 Threshold parameter for the exact reciprocal budget `1 / s n`. 

### `B`

 Occurrence bound of the actual quantitative sparsification leaves. 

### `delta`

 The extra one is the unary validity factor at each packed coordinate. 

### `Dstar`

 No ceiling is needed: `tau⁻² = s²` and the remaining factors are integers. 

### `degree_budget`

 The degree budget holds even when the floor gives zero. Readiness tests
separately ensure that the interpolation interval is large enough. 

### `parameters`

 The actual multicolor parameter record, before a factor pattern is given. 

### `exists_occurrence_bound`

 The occurrence polynomial's constants are selected for `k` before `n`. 

### `exists_incidence_bound`

 Packing increases the fixed polynomial degree by at most one. 

### `checks`

 These are exactly the natural-valued checks implemented by the source's
main-branch guard. The parameter record itself requires no tail assumption. 

### `eventually_ready`

 Both substantive numerical checks eventually pass for the selected prime
and the selected sparsification threshold. No tail or block-growth assumption
remains in this theorem. 

### `exists_fallback_cutoff`

 One fixed cutoff suffices for every failure of the growing-parameter guard. 

### `intervalStart`

 The interpolation interval is computed from the actual swap mean. 

### `weighted_tail`

 The exact degree-cleared tensor-multiplicity tail used by the actual
multicolor layout constructor follows from the source's numerical guard. 
