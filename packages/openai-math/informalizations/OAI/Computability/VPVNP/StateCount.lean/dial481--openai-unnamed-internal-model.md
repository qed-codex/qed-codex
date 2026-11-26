---
{
  "module": "OAI/Computability/VPVNP/StateCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StateCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StateCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

Note from QED Codex: the notes below name results of Kirill Khoruzhii. [Lemmata entry (CC BY 4.0)](https://github.com/ZIB-IOL/lemmata/blob/a2dd430f283febd755a6ee6932d0b0fdabfb330c/docs/crossing-decomposition/index.md)


# State counts for the shifted crossing

Appendix B of *VP and VNP differ over every field* bounds the sizes of two
integral factorizations using different energy cutoffs. Energies here are
doubled, so a signed integer shift changes the cutoff by twice that integer.

We use the fermionic partition asymptotic from Khoruzhii's development, count
the finite-mode states, and evaluate the two dimension sequences and both
factorization bounds for the same shift.


### `cutoffCount`

 Number of fermionic states of doubled energy at most `H`. Each occupied
mode `i` contributes `2*i+1`. 

### `stateExponent`

 Base-two growth constant for a cutoff measured in doubled energy. 

### `cutoffCount_limit`

 The partition-function asymptotic in the logarithmic base and energy units
of the two shifted flattening bounds. 

### `occupationCount_le`

 The dimension bound for finite occupation states of doubled energy at most `k`. 

### `occupationCount_eq`

 Once modes below `k` are included, the entire partition cutoff occurs. 

### `occupationCount_of_neg`

 A negative doubled-energy cutoff contains no states, including the vacuum. 

### `roundedQuadratic`

 A signed integer cut at quadratic scale. In particular the displacement may be negative. 

### `quadraticEnergy`

 A nonnegative integer energy, obtained from the signed cut by truncation at zero. 

### `shiftedEnergy`

 Both shifted energies use the same integer displacement. 

### `count_quadratic_limit`

 The logarithmic state-count asymptotic along an integral cutoff growing as
`v * n²`. The growth constant is expressed in base two. 

### `logb_polynomial_overhead`

 A fixed power of the quadratic energy cutoff has subexponential size. 

### `logb_pred_rate`

 Removing the empty state preserves any positive exponential growth rate. 

### `crossingEnergy`

 Doubled-energy cutoff of a wire with prescribed base-two logarithmic rate. 

### `crossingShift`

 The integer shift shared by the two crossing factorizations. 

### `crossingFactorBound`

 The number of available factor coordinates on one of the two cuts, including
the polynomial cost of summing over cardinalities, energies, and monomials. 

### `shiftedCrossing_rates`

 The exponential rates in Theorem 3.1, using one integral displacement for both
bounds. The first dimension omits the empty state and the second includes it. 
