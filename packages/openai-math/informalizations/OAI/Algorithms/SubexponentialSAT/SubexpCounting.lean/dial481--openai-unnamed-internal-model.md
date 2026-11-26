---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCounting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCounting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCounting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact counting with arbitrarily many symbolic color groups

This module preserves the binary-color proof in `Counting` and gives the
Section 4 computation with an arbitrary finite color type. The number of
colors is not fixed in the statements. All sums, products, truncations, and
coefficient extractions are defined before their correctness is proved.


### `group`

 The canonical representative of one full symbolic color group. 

### `groupProduct`

 Multiply all separately truncated groups and reduce again. 

### `separatedMoment`

 Equation (4.6): one outer scalar times the product of the independent
inner sums, reduced to its canonical representative. 

### `separatedJet`

 Equation (4.5): extract each matching X monomial and only then set U=1. 

### `groupProduct_eq`

 The product in the quotient has the canonical representative of the
full product, regardless of the number of color groups. 

### `separatedMoment_eq_sum`

 Finite distributivity identifies the actual separated computation with
the full symbolic moment. The hypothesis is only own-coordinate dependence. 

### `groupProduct_support`

 Every canonical product has the actual retained monomial support. 

### `groupProduct_substitution`

 Lemma 4.1, after independently reducing every color group. 

### `separatedJet_eq_sum`

 Exact multi-color symbolic counting before global interpolation. All
canonical products and separated sums are actual definitions above. 

### `rowJet`

 The separated jet with each group built from the actual colored factor
polynomials and their incidence-specific polynomial rows. 

### `rowJet_eq`

 Local degree, residue-defect, and own-color invariance properties suffice
for the defined separated calculation to recover the true global jet. 

### `layoutBeta`

 The actual chosen lift of each incidence row's residue. 

### `layoutGroup`

 Full symbolic groups indexed by all r colors. 

### `layoutBeta_defect`

 The coefficient of U becomes p-divisible under input substitution because
beta is an actual section of the residue map. 

### `layoutOuterWeight`

 The complement-coordinate part of an actual moment weight. 

### `layoutInnerWeight`

 The part of the moment weight supported on a single color. 

### `layoutJet`

 The separated calculation on the actual outer coordinates and color
cosets of a layout. Its representatives are independent of every moment. 

### `layoutJet_eq`

 Every semantic premise of multicolor separation is supplied by the
actual layout, its lifted rows, and the principal nilpotent residue kernel. 

### `theta_unit_differences`

 The distinct residue nodes have unit differences in the lifted ring. 

### `differenceInverse`

 Explicit finite geometric correction of each residue-field inverse. 

### `explicitReconstruction`

 Explicit finite geometric CRT applied to the defined separated jets.
No inverse or Bezout certificates are supplied by the caller. 

### `interpolated_degree_lt`

 The degree budget is uniform in the number of colors: colors do not
increase the degree of the actual global polynomial. 

### `explicitRecoveredValue`

 Evaluate the explicit reconstruction of the interpolated factor tables
at the selector origin. This is a defined calculation, not a count oracle. 

### `actualLiftedLayout`

 Lift every node and incidence row of the multicolor layout into the
actual monic quotient with this same residue field. 

### `actualRingValue`

 The fully instantiated output of the actual multicolor separated
calculation and finite geometric CRT, in the prime-power ring with mu=D+1. 

### `actualRingValue_eq_count`

 All ring, lift, kernel, nilpotence, inverse, and local-separation conditions
have been discharged. The layout and positive dimension are the only inputs. 

### `actualCount`

 Decode the actual output using its canonical constant coefficient.
No call to the target factor count occurs in this definition. 

### `actualCount_eq_count`

 Exact natural-number counting from the multicolor interpolation layout,
uniformly in the number of colors and all field parameters. 

### `actualCount_pos_iff`

 Positivity of the recovered integer has the intended assignment semantics.
Executable refinement and running time are separate from this identity. 

### `selectedLiftedLayout`

 The multicolor layout lifted into the quotient by the exact quartic
coefficients returned by the executable field construction, using finite
coefficientwise lifting of every row. 

### `selectedRingValue`

 Exact-ring output using the selected quartic and its integer coefficient
lifts, with the same separated moments and finite geometric reconstruction. 

### `selectedCount`

 Decode the actual multicolor output in the selected-quartic quotient. 

### `selectedCount_eq_count`

 The exact natural count using the same quartic as the executable ring
backend. No field identification or count equality is an input. 
