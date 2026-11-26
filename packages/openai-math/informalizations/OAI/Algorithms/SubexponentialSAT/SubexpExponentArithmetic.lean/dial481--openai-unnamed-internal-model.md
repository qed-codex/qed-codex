---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpExponentArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpExponentArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpExponentArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Growing-parameter exponent arithmetic

All factors in this module are actual real powers. The bounds expose the
growing parameters; they assert no program-running-time fact.


### `shiftedLogLog`

 The real logarithmic scale used in the final statement. 

### `exponentialPart`

 The exponential part of one leaf calculation, with its overhead constant visible. 

### `dimension_le`

 The packing ceiling gives D ≤ 33 n/s for the source's bit capacity range. 

### `exponent_le`

 Explicit Section 5.4 bound, before raising two to these exponents. 

### `exponentialPart_le`

 No input-dependent multiplicative constant is hidden in this inequality. 

### `rpow_eq_two_rpow_logb`

 A polynomial base can be rewritten as an actual base-two real power. 

### `eventually_logb_sq_le`

 The square of log base two is eventually at most n, with the shift included. 

### `eventually_shiftedLogLog_le_logb`

 The iterated logarithm is eventually bounded by the first logarithm. 

### `eventually_logb_le_scale`

 The polynomial-overhead absorption inequality is proved from logarithm
growth, rather than supplied as a runtime assumption. 

### `natLog2_le_shiftedLogLog`

 Lower comparison needed for the growing per-node search exponent. 

### `shiftedLogLog_le_twice_natLog2`

 The two integer logarithms lose at most a constant factor on the final scale. 

### `parameter_cost_le`

 All polynomial overhead is represented by H ≤ (n+16)^d with d explicit.
The extra color factor r is also charged, rather than hidden in a constant. 

### `branched_parameter_cost_le`

 Also charge the sparsification factor 2^(n/s). 

### `eventually_branched_parameter_cost_le`

 For the source's actual integer s, the analytical scale assumptions are
discharged eventually. Remaining hypotheses concern the concrete parameters. 

### `eventually_source_cost_le`

 The source's choices tau = 1/s, r = s, and c = 128, with a completely
explicit final coefficient. No field-size or layout constant is held fixed. 
