---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CosetCardinality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CosetCardinality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CosetCardinality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cardinalities for the separated coset enumeration

The outer data are a vector on the complementary coordinates and one quotient
class on each of two coordinate blocks. The inner data are actual vectors in
those quotient classes. These theorems establish their exact cardinalities and
the algebraic identity in equation (4.9). They do not assert a bit-complexity
bound for enumerating a basis, a quotient, or the symbolic ring.


### `card_of_linearEquiv`

 Linear equivalences preserve the cardinality of the underlying set. 

### `finiteCoordinateEquiv`

 A finite-dimensional space has a linear coordinate system with exactly
`finrank` coordinates. The basis choice here carries no algorithmic cost claim. 

### `card_module`

 The cardinality formula for a finite-dimensional vector space. 

### `card_submodule`

 The size of an inner subspace is the field size to its dimension. 

### `card_quotient`

 The number of cosets in a coordinate block. 

### `CosetFiber`

 A coset is represented as the fiber of the actual quotient map. 

### `quotientFiberEquiv`

 Taking a quotient class together with a point of that class partitions the
ambient vector space exactly, without duplicates or omitted vectors. 

### `cosetEquiv`

 Translating the subspace by any representative enumerates its coset
bijectively, even when the field elements are later represented by integers. 

### `card_coset_eq`

 Every quotient class has the same cardinality as its subspace. 

### `card_coset`

 Every inner sum over a coset has exactly this many terms. 

### `fintype_card_submodule`

 Fintype-facing version for finite sums indexed directly by subspace vectors. 

### `OuterData`

 The actual type of outer choices used in Section 4.5. 

### `outerFiberEquiv`

 Every split assignment is uniquely an outer datum and a pair of vectors
in its two cosets. This is the full-domain partition behind the enumeration. 

### `card_outer`

 Product cardinality gives the number of outer choices. 

### `iteration_identity`

 The arithmetic identity behind equation (4.9). The dimension assumption
is essential when subtraction is natural-number subtraction. 

### `iteration_bound`

 An integer-exponent version of the final inequality in (4.9).
The hypotheses express `d0,d1 ≥ D/4` without rounding ambiguity. 

### `card_outer_times_inner`

 Counting each term in each of the two inner sums for every outer datum.
This is an iteration count, not a Turing-machine runtime theorem. 

### `coordinateSplitEquiv`

 The disjoint coordinate supports and their complement split every ambient
assignment uniquely. This map is the actual restriction of coordinates. 

### `coordinate_card_partition`

 Three disjoint coordinate blocks account for the full ambient dimension. 

### `CoordinateOuterData`

 Restricting each subspace to its own coordinate support is represented by
the local domains `S0 → 𝔽` and `S1 → 𝔽`. 

### `coordinateOuterFiberEquiv`

 A complete ambient assignment is an outer datum and a point in each of
its two cosets, through explicit coordinate restriction and quotient fibers. 

### `coordinateReconstruct`

 Reconstruct an ambient assignment from its outer data and two coset points. 

### `coordinateReconstruct_components`

 Reconstructing an assignment gives exactly its three supplied coordinate blocks. 

### `card_coordinate_outer`

 The exact outer count for disjoint coordinate supports, with `D` given by
the cardinality of the original coordinate type. 

### `fintype_card_coordinate_outer`

 Over a finite field the outer data themselves form a finite type, with
the expected power of the actual field cardinality. 

### `coordinate_dimensions_le`

 Disjoint supports bound the sum of the two inner dimensions by the
ambient number of coordinates. 

### `coordinate_iteration_count`

 Equation (4.9), before the real-valued `3D/4` estimate: the outer count
times the two inner sizes is the sum of these two powers. 

### `card_coordinate_iteration_type`

 The iteration formula counts a concrete type: an outer choice, followed
by either an index for the first inner sum or an index for the second. 

### `coordinate_iteration_bound`

 The complete integer-cardinality bound in (4.9). The exponent is the
floor of `3D/4`, so this is slightly sharper than its real-exponent version. 

### `coordinate_inner_sizes`

 The sizes of the actual two cosets used for any outer choice. 

### `coordinateRestriction`

 Restriction of an ambient subspace to a selected set of coordinates. 

### `coordinateRestriction_injective`

 Restriction loses no information for a subspace supported on `S`. 

### `restrictedSubspace`

 The same supported subspace, viewed as a subspace of its local coordinates. 

### `restrictionEquiv`

 Ambient and local presentations of a supported subspace are linearly equivalent. 

### `card_supported_outer`

 The outer-count theorem with precisely the ambient-subspace support
hypotheses of the interpolation layout. 

### `mem_of_restriction_mem`

 A supported ambient vector whose restriction lies in the restricted
subspace already lies in the original ambient subspace. 

### `sub_mem_of_local_quotient_eq`

 Equal restrictions modulo the local subspace and equality outside its
support imply that the ambient difference belongs to the original subspace. 

### `coordinateReconstruct_left_sub_mem`

 With outer data and the right point fixed, varying the left point within
its local coset changes the ambient assignment by a vector of the global `K0`. 

### `coordinateReconstruct_right_sub_mem`

 The symmetric global-subspace difference statement for the right point. 
