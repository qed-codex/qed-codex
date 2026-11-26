---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SubspaceDimension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SubspaceDimension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SubspaceDimension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multicolor fixed subspaces

The generic common-kernel and zero-extension constructions from the two-color
formalization apply unchanged to an arbitrary number of colors. Here we prove
the parameter-dependent dimension bound: per-slot rank at most τ/Δ of the joint
coordinate set loses at most τ of a side's dimension after all slots.

Every subspace is defined over the same field as the constraint maps.


### `sum_rank_le_of_slot_bounds`

 Sum the slot budgets, cancelling the number of slots. The zero-slot case
is included and requires only nonnegativity of the budget. 

### `card_joint_le_card_side`

 The joint index set is no larger than the side containing it. 

### `finrank_supportedFixedSpace_le`

 A supported fixed space has dimension no larger than its side. 

### `supportedFixedSpace_dim_lower`

 All slots together lose at most a τ fraction of the side. The rank
hypothesis is the actual defect-map rank, not a bound on a proxy quantity. 

### `supportedFixedSpace_dim_lower_rat`

 Rational form for the authoritative quantitative layout interface. 

### `supportedFixedSpace_disjoint`

 Spaces supported on disjoint coordinate sets are disjoint, regardless of
the matrices used for their slot constraints. 

### `universalFixedSpace`

 The multicolor universal subspace, defined over the same field as M and
embedded in all universal coordinates by setting the other coordinates to zero.
The joint fibers have head color g and slot color different from g. 

### `universalFixedSpace_supported`

 A convenient support projection of the membership characterization. 

### `universalFixedSpace_fixed`

 A convenient slot fixed-point projection of membership. 

### `universalFixedSpace_dim_upper`

 No supported subspace can exceed the dimension of its head-color side. 

### `universalFixedSpace_dim_lower`

 Equation (3.7) as a fraction of the side size, with rational parameters.
Only nonnegativity of τ is needed by the dimension argument. 

### `universalFixedSpace_dim_lower_of_real_rank`

 Bridge from the real-valued spectral rank inequality to the rational layout
interface. The subspace and field are unchanged. 

### `universalFixedSpace_card_lower`

 Denominator-cleared universal-block dimension bound. 

### `universalFixedSpace_fullBlock_lower`

 The same bound using the paper's N = r^(Q(Δ+1)). 

### `universalFixedSpace_disjoint`

 Distinct head colors give disjoint subspaces at each interpolation point. 

### `sideConstraintMap`

 Flatten every slot equation into one finite row index. 

### `encodedSideConstraintMap`

 Encode rows and columns by explicitly supplied finite equivalences. These
equivalences are inputs, so this definition invokes no choice of enumeration. 

### `encodedConstraintMatrix`

 A concrete rectangular matrix: evaluate the encoded constraint map on
each standard coordinate vector. This is executable whenever its inputs are. 

### `encodedConstraintMatrix_zero_iff`

 The rectangular matrix kernel is exactly the side-coordinate fixed space,
with columns translated by the supplied explicit enumeration. 

### `encodedConstraintMatrix_zero_iff_supported`

 Zero extension identifies the matrix kernel with the supported universal
  space. The matrix search itself only uses the n side coordinates. 

### `decidableExtendByZero`

 Executable zero extension when membership in the coordinate side is
decidable. The earlier extension map remains its specification. 

### `encodedKernelEquiv`

 A computable linear equivalence from the finite side-coordinate kernel
to the full supported subspace. Its inverse is explicit coordinate restriction.
No basis, complement, or enumeration is selected by choice. 
