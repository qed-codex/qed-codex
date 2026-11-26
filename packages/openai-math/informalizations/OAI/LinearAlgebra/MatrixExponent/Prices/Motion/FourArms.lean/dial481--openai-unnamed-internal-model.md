---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/Motion/FourArms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/FourArms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/FourArms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First displacement in a decreasing filtration of isometric actions

Orbit centers bound the change in distance to the fixed set.
The unique nearest fixed point inherits all symmetries of that set
fixing the original mark.


### `motion_scale`

 The center at the critical radius is fixed by every symmetry fixing
the base mark and mapping the fixed set into itself. 

 # Zooming into the onset of displacement along rational radii 

### `Kink.zoom`

 A single choice of rational dilation and origin works for all slopes. 


# Distances of individual leaves

Use two inner arms and one outer arm, all of the same length.
Move the inward radius to the corner of the limiting profile.
The cost of the perturbation on the second inner arm then vanishes.


### `zoom_leaf`

 A scalar squeeze for the distance at a nongeneric parameter. 


# The translation groups of valuation disks

Use multiplicative notation for the additive group of the open
valuation disk to apply the metric group-action lemmas.



# Wire tests imply radial estimates

Specialization permits using any integral parameter on the left.
There is no need to choose the same generic parameter in every test.


### `RadialStars`

 The one-inner-arm and equal-length two-inner-arm distance tests. 

 The generic rate and comparisons along a single arm. 

 The three collision arms and their two-pair endpoints. 

 A shrinking outer arm is controlled by a larger generic placement. 

 Applying the submean test on the collision, unused, and outer arms. 

### `small_X`

 The common label near the branch point has normalized price at most
three halves in the limit. An infimum avoids any derivative assumptions. 
