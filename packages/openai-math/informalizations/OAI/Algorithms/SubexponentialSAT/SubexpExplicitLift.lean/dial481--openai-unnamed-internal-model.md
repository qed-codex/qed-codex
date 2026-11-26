---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpExplicitLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpExplicitLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpExplicitLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit finite coefficient lifts of a multicolor layout

The polynomial lift uses exactly `bound + 1` coefficients of the original
polynomial and applies one fixed residue section to each. No polynomial or
node is obtained by choosing an arbitrary preimage of a surjective map.
The section is an ordinary function, not a ring homomorphism.


### `coefficientData`

 The explicit array of lifted coefficients, including zero padding up to
the supplied degree bound. 

### `liftPolynomial`

 Reconstruct the lift from the finite list of source coefficients. 

### `liftPolynomial_eq_coefficientData`

 The construction is literally a finite array fold over `bound + 1`
entries. This identity makes the data inspected by the lift explicit. 

### `coeff_liftPolynomial_of_degree_le`

 With a zero-preserving section and a valid bound, every coefficient is
exactly the image of the corresponding original coefficient. 

### `natDegree_liftPolynomial_le_bound`

 Finite reconstruction cannot introduce a coefficient beyond the stated
bound, irrespective of any algebraic property of the section. 

### `natDegree_liftPolynomial_le`

 Zero preservation also prevents the padding from increasing the degree
above that of the source polynomial. 

### `map_liftPolynomial`

 Reduction recovers the original polynomial coefficient by coefficient. 

### `natDegree_liftPolynomial_eq`

 The lift preserves the source degree exactly when it has a residue
left inverse. In particular the layout degree budget is unchanged. 

### `fromSection`

 Lift every node and every one of the `c.R + 1` row coefficients through
the given fixed section. Preserving zero and one gives the exact coordinate
row at the origin, rather than only its residue. 

### `fromSection_row_coeff`

 Every stored row coefficient has the promised explicit formula. 

### `explicitLiftedLayout`

 The selected-ring lift of an actual multicolor layout. Nodes and all row
coefficients use the explicit four-coordinate residue section. This does
not invoke the generic surjective-preimage layout construction. 

### `explicitLiftedLayout_row_coeff`

 The exact source-to-target coefficient rule for every lifted incidence. 

### `explicitLiftedLayout_row_eq_sum`

 The semantic row is constructed from precisely `c.R + 1` explicitly
lifted coefficient entries, including zero padding. 

### `explicitLiftedLayout_row_natDegree`

 The lift changes no incidence-polynomial degree. 
