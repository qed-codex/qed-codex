---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpInvariance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpInvariance.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpInvariance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arbitrarily many colors: exact dependence on one inner coordinate

For a row of color g, every other color subspace is contained in its kernel.
After fixing the outer datum and one coset in each component, this forces the
row residue, its fixed chosen lift, and the actual symbolic factor group to
depend only on the g component. Coordinate lifts need not preserve addition.


### `assemble`

 Assemble an ambient input from a fixed outer part and its color blocks. 

### `assemble_sub_eq`

 Changing just one color block changes the ambient input by exactly
the zero-extended difference of that block. 

### `linear_map_assemble_eq`

 Killing every other color gives equality for arbitrary tuples in fixed
component cosets, provided their own-color components agree. 

### `linear_map_pi_eq`

 Product-coordinate specialization, using genuine single-coordinate
linear embeddings rather than a functional-dependence assumption. 

### `beta_eq_of_components`

 Exact beta equality for all colors simultaneously. 

### `beta_add_other_color`

 A factor of color g is invariant under translation by any other
color's ambient subspace. 

### `lifted_group_eq_of_components`

 Any fixed construction on the beta vector inherits the proved
independence. No invariance premise is imposed on the constructed values. 

### `cosetFiber_sub_mem`

 Equal quotient classes provide exactly the component-difference
hypotheses used by the linear argument. 

### `beta_eq_on_coset_fibers`

 For fixed outer cosets, only the own-color inner point matters. 

### `rowGroup_eq_of_components`

 The actual polynomial group from Counting, before truncation, depends
only on its own color coordinate. Its invariance follows from row kernels. 

### `rowGroup_eq_on_coset_fibers`

 The fixed-coset formulation matches the inner tuple used by the
multi-color separated moment sum. 

### `rowGroup_eq_representatives`

 Explicit factorization through the own-color point: all other
components may be replaced with fixed representatives in their cosets. 

### `canonical_rowGroup_eq_on_coset_fibers`

 The equality survives the manuscript's canonical symbolic truncation. 

### `coordinateExtend_restricted_mem`

 A point of a restricted supported subspace returns to that subspace
under actual zero extension. 

### `restrictedSubspace_le_ker_coordinateExtend`

 Global layout annihilation implies exactly the local kernel hypothesis
used by the arbitrary-color coset proof. 

### `coordinateAssemble_sub_mem`

 Changing one color's point inside its fixed coset changes the actual
ambient reconstruction by a vector of that color's global subspace. 

### `beta_coordinateAssemble_eq`

 Exact beta invariance for the actual zero-extension reconstruction,
using only supported-subspace and annihilation facts from the layout. 

### `beta_coordinateSplitEquiv_symm_eq`

 Same statement phrased using the inverse of the genuine coordinate
linear equivalence. 

### `rowGroup_coordinateAssemble_eq`

 The actual symbolic group is exactly independent of the other inner
coset points in the actual ambient coordinate reconstruction. 
