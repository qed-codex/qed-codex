---
{
  "module": "OAI/Computability/VPVNP/GrassmannCompactness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannCompactness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannCompactness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniformity of the strict Grassmann inequality

The last paragraph of Lemma 5.3 in *VP and VNP differ over every field*
passes from rigidity of an extremal marked configuration to a strict uniform
bound. The relevant topology is the product topology on real arrays. Restricting
to a specified set of marks and taking square roots are continuous, so a cube
in a limiting squared-distance array violates uniform cube exclusion for the
original distances.


### `markedDistances`

 The rescaled marked distances whose closure defines uniform exclusion. 

### `markedSquares`

 Rescaled squared distances. The parameter is the square of the distance scale. 

### `restrict_sqrt_mem_closure_markedDistances`

 Restricting a limiting squared-distance array to marked vertices yields
an ordinary distance array in the closure for those marks. 

### `excluded_of_mem_closure_markedSquares`

 Uniform exclusion prevents a prescribed ordinary distance array from
appearing on any set of marks in a limiting squared-distance array. 

### `uniform_gap_of_normalized_strict`

 On bounded normalizations of marked squared distances, a strict bound at
every point of the closure yields a common positive improvement. The case of
zero normalizing energy is handled by the non-strict homogeneous bound. 

### `quadBounds_of_mem_closure_markedSquares`

 Every limiting marked array retains the four-point inequality and its
opposite-side equality case, even when the target spaces vary. 

### `strict_grassmann_bound_of_rigidity`

 The compactness implication in Lemma 5.3 for the actual binary Grassmannian.
The inputs from the Grassmann combinatorics are the non-strict bounds on the
pair means and rigidity at equality. Uniform exclusion concerns the ordinary
distance array of the cube, while rigidity yields its squared distances. 
