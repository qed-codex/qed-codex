---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Counting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Counting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Counting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact counting by separated symbolic moments

This module defines the separated finite sums, rather than assuming they
return the target count. Canonical deletion is applied before coefficient
extraction and before evaluating U at one. Theorems make the algebraic
hypotheses explicit; they do not claim an executable bit-complexity bound.


### `group`

 A group polynomial after deleting precisely the forbidden monomials. 

### `groupProduct`

 The canonical product of the two separately truncated groups. 

### `separatedMoment`

 The actual two inner sums of equation (4.8), followed by canonical
reduction of the result. The input equivalence enumerates every assignment
exactly once by outer data and two fibers. 

### `extractX`

 Extract the X monomial while retaining both polynomial variables U,Z. 

### `separatedJet`

 Equation (4.7), with all moment sums actually given by the separated
construction. U=1 is applied only after canonical reduction and extraction. 

### `groupProduct_eq`

 The product used in moment extraction equals the canonical reduction of
the full product, even though the two groups were truncated independently. 

### `group_congr`

 Exact group invariance passes through canonical truncation. 

### `separatedMoment_eq_canonical_sum`

 No target-count equality is assumed: the unsimplified separated sum is
proved equal to the full symbolic moment by finite distributivity. 

### `separatedMoment_eq_sum`

 Moving canonical reduction through the finite sums and scalar weights
identifies the separated output with the full moment of canonical products. 

### `canonical_support`

 Every retained coefficient really has support in the finite moment set. 

### `groupProduct_substitution`

 Exact substitution of the canonical group product is the desired local
truncation; the two hypotheses are support filtration and nilpotence. 

### `separatedJet_eq_sum`

 The defined separated-jet construction is the sum of the correct local
truncations. Its hypotheses concern input invariance, scalar weights, support,
and nilpotence; no equality with the desired jet is assumed. 

### `rowCoefficient`

 The coefficient of Z^j in a shifted row, kept as an actual linear form
in the formal input variables. 

### `rowArgument`

 The manuscript's incidence argument, with the positive-Z expansion
constructed directly from the polynomial row. 

### `evalXU_rowArgument`

 Substitution cancels beta and reconstructs the shifted scalar row. 

### `rowGroup`

 A full symbolic factor group. Its dependence on the actual input z is
confined to beta; every rowCoefficient remains a formal polynomial. 

### `evalXU_rowGroup`

 Evaluation of an entire symbolic group is its shifted factor product. 

### `rowGroup_union`

 Disjoint factor groups multiply to the full group. 

### `rowGroup_highU`

 Prime-power divisibility kills every discarded U coefficient for the
actual row/table construction; it is not assumed for the final product. 

### `sum_evalXU_rowGroups`

 The two actual symbolic factor groups give exactly the formal expansion
of H at the chosen node after X substitution and U=1. 

### `sum_trunc_evalXU_rowGroups`

 The correct local jet expressed as the sum of the truncated group
substitutions, before the moment-separation optimization is invoked. 

### `trunc_eq_modByMonic`

 Canonical coefficient deletion agrees with monic reduction modulo Z^D. 

### `layoutBeta`

 The actual residue lift used as beta at each incidence. 

### `colorGroup`

 Factor colors determine the two concrete groups. 

### `layoutGroup`

 The actual symbolic groups determined by a lifted layout. 

### `eval_rowCoefficient_zero`

 The constant coefficient used in the symbolic argument is exactly the
actual lifted row value, before selecting beta. 

### `layoutBeta_defect`

 The local p-divisibility hypothesis is derived from the actual residue
kernel and the chosen section. 

### `cosetRepresentative`

 A concrete point in a nonempty coset, chosen independently of all weights. 

### `layoutJet`

 The complete separated local computation, with groups, representatives,
weights, and outer/inner domains supplied by the actual layout. 

### `layoutJet_eq`

 All semantic hypotheses of the separated-jet theorem are discharged by
the actual layout, residue kernel, and nilpotence. 

### `theta_unit_differences`

 Unit differences of lifted nodes follow from residue separation and the
principal nilpotent kernel; they are not an extra interpolation hypothesis. 

### `reconstructLayout`

 The concrete finite-sum CRT reconstruction fed by the actual separated
jet computation. The supplied polynomials are algebraic Bezout certificates. 

### `reconstructLayout_eq`

 CRT recovers H from the defined separated jets. The degree hypothesis is
a polynomial degree condition, discharged below for interpolated factors. 

### `differenceInverse`

 Each inverse of a node difference is computed by lifting its residue-field
inverse and applying a finite nilpotent geometric correction. 

### `explicitReconstruction`

 Explicit finite geometric CRT reconstruction of the separated jets.
There are no supplied Bezout polynomials or inverse certificates. 

### `interpolated_degree_lt`

 The strict interpolation degree budget follows from the actual bounded
factor pattern and the individual degrees of the explicit table interpolants. 

### `recoveredValue`

 The actual count value produced by separated jets and explicit CRT. 

### `recoveredValue_eq_count`

 The layout-to-counting correctness theorem. Every local jet is the
  separated construction above; the target equality is a conclusion. 

### `explicitRecoveredValue`

 The same count computation using finite geometric CRT throughout. 

### `factor_count_lt_prime_power`

 The chosen prime-power modulus strictly exceeds every possible count. 

### `actualRingValue`

 The completely instantiated ring-valued output: the actual monic-lift
quotient, integer representatives, lifted layout, residue section, separated
moments, and finite geometric CRT are all constructed. 

### `actualRingValue_eq_count`

 Every algebraic side condition is discharged for the actual prime-power
ring. Only the supplied layout and nonempty coordinate domain are required. 

### `actualCount`

 Decode the actual ring output as a natural number using its canonical
constant coefficient. This definition does not call the target factor count. 

### `actualCount_eq_count`

 Exact natural-number counting from an interpolation layout. The count is
recovered, not merely tested modulo p or compared for zero. No ring, lift,
coefficient, inverse, or desired-result equality is a hypothesis. 

### `actualCount_pos_iff`

 The resulting decision test has exactly the intended satisfying-assignment
semantics. Complexity and a concrete machine realization are separate. 
