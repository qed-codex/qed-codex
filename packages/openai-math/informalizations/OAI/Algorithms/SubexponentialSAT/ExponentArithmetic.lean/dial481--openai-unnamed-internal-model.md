---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExponentArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExponentArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExponentArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Section 6: real exponent arithmetic

These are inequalities of actual real powers. They do not themselves establish
that a program runs within any of these bounds. The fixed multiplicative factor
depends on p and is independent of the Boolean input size n.


### `log2`

 The real base-two logarithm used in the field-to-Boolean conversion. 

### `leafCoefficient`

 The coefficient in the exponent before rounding up to 0.79. 

### `fixedFactor`

 The explicit fixed factor due to replacing D = ceil (n/ell) by n/ell+1. 

### `fieldCost`

 The exponential part of the field-variable cost in Section 6. 

### `fieldCoefficient`

 Base-two exponent per field variable. 

### `leafCoefficient_le_exact`

 The exact worst-case coefficient allowed by ell ≥ 4096. 

### `ceil_div_le_add_one`

 Natural ceiling, cast back into the reals, has the required additive-one bound. 

### `fieldCost_le_fixedFactor`

 Actual real-power bound, with the ceiling and logarithm bounds as explicit
arithmetic assumptions. Its multiplicative factor depends only on p. 

### `fieldCost_le_079`

 The advertised per-leaf exponential bound once the bit capacity is large. 

### `sparsification_times_leaf_le_09`

 Multiplying the per-leaf exponential factor by the sparsification factor
leaves room below the theorem's exponent 0.9. 

### `combinedCost_le_09`

 The combined numerical bound. Any actual runtime bound by the left-hand
side, including its polynomial overhead, is a separate algorithmic obligation. 

### `packed_fieldCost_le_079`

 Per-leaf bound after substituting the actual natural floor and ceiling.
There are no independently assumed rounding or logarithm estimates here. 

### `packed_combinedCost_le_09`

 Section 6's combined bound with the actual packing parameters. 

### `bruteForce_le_fixedFactor`

 On the bounded brute-force range, the remaining factor is independent of n. 
