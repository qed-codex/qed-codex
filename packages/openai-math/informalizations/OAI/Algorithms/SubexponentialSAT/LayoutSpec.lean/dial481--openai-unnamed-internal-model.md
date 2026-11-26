---
{
  "module": "OAI/Algorithms/SubexponentialSAT/LayoutSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LayoutSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LayoutSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The exact interpolation-layout interface

This module states the finite mathematical output of Lemma 3.1.  It does not
assert existence of a layout, construct its universal block, or claim a running
time.  Constants are independent of the coordinate and factor index types.

Rows are indexed by **incidences** `(e,v)`, not just by coordinates `v`.
The subspaces are over `ZMod p`; row coefficients and interpolation nodes are
over a possibly larger finite extension field.


### `Constants`

 The fixed numerical parameters in Lemma 3.1, before the input size varies.
Primality is a typeclass hypothesis on layouts; oddness and the positive
combinatorial bounds are recorded here. 

### `exists_polynomial_lift`

 A surjective residue map lifts a polynomial without increasing its degree,
while permitting a prescribed lift of its constant coefficient. 

### `Layout`

 The finite output of the layout lemma for a bounded factor pattern.
`dimension_lower` is `dim K >= D/4` with denominators cleared; natural-number
division would incorrectly weaken that requirement when `4` does not divide D.
The nonzero-node equivalence records both distinctness and completeness. 

### `fieldEquiv`

 Adding zero to the node enumeration enumerates the entire extension field. 

### `fieldFintype`

 The output specification itself implies finiteness of the extension field;
an additional finite-field hypothesis is not silently required. 

### `fieldFiniteDimensional`

 The prescribed positive extension degree also implies finite dimension. 

### `node`

 The node as an extension-field element. 

### `rowMap`

 A row evaluation is a genuine linear map over the base field. 

### `rowMap_eq_of_sub_mem`

 The row is constant on every coset of its factor's selected subspace. 

### `K_disjoint`

 Disjoint coordinate supports imply disjoint subspaces over the base field. 

### `localK`

 The selected subspace written using only its supported coordinates. 

### `Outer`

 The outer choices: complementary coordinates and a coset on each side. 

### `coordinateOuterFiberEquiv`

 The actual bijection partitioning all assignments into outer data and two
local cosets. No assignment is omitted or counted twice. 

### `reconstruct`

 Reassemble an assignment from its outer data and two inner points. 

### `card_outer`

 Exact number of outer choices for the layout's own subspaces. 

### `iteration_bound`

 The actual enumeration count, as distinct from a bit-operation cost. 

### `LiftedLayout`

 Coefficient and node lifts needed in Section 4.  The residue map need not
have a ring-homomorphic section.  Its row lifts retain their exact selector
constant coefficient and their degree. `ofSurjective` below constructs these
lifts from a surjective residue map. 

### `ofSurjective`

 A surjective residue homomorphism suffices to construct all node and row
lifts, including the exact zero-value and degree requirements. This is a finite
existence construction; no algorithmic cost for choosing preimages is claimed. 

### `liftedRow`

 Actual lifted row evaluation, with arbitrary coordinate representatives.
Only the residue condition is used; carries between representatives are allowed. 

### `beta_eq_of_sub_mem`

 Chosen residue representatives are exactly constant on the selected cosets. 

### `beta_reconstruct_left`

 A color-zero beta ignores the left inner point once outer data are fixed. 

### `beta_reconstruct_right`

 A color-one beta ignores the right inner point once outer data are fixed. 
