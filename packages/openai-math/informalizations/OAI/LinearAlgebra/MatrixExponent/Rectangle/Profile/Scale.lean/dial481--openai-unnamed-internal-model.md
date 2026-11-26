---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Profile/Scale.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Profile/Scale.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Profile/Scale.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dilation and the two one-coordinate slopes

Vary one width forward and the other backward by reciprocal factors.
Homogeneity gives the exact difference of the two log-prices. Taking
the limit in rational lower bounds on the increments needs no
differentiability of the two-width profile.



# A continuum profile from integer dilations

Approximate each ray from below by a common rescaling of a lattice
point. Integer dilation makes every such lower bound valid eventually.
Slightly enlarging the target widths bounds arbitrary approximations
from above.



# Common slope of two coupled rows

Taking the supremum of a two-width quotient gives the common limiting
slope. A single tripling beyond the widths under test bounds that
quotient by every earlier secant, even at unequal widths.



# Strong minimum principle for a homogeneous defect

A positive value on one coordinate ray makes its integral decrease
strictly at first order under radial dilation. Telescoping the three
coordinate increments bounds any such decrease by an arbitrarily
small multiple of the dilation parameter.


### `vanishes`

 A single interior zero forces vanishing throughout the positive orthant. 


# Matching intercepts at the three critical width pairs

Write each log-price as its first intercept plus a normalized
displacement. The two displacements in each row sum to at most
zero. Across an edge the two displacements sum to at least minus
the scaled defect. A displacement exceeding twice this error would
force the three intercepts to increase strictly around a cycle.


### `Critical`

 Price at a critical width pair, shared between its two orders. 

### `Critical.error`

 Uniform error at a critical pair. No upper bound on the arm
lengths or distances is needed. 

 # Critical estimates from polynomial width profiles 

### `rate`

 Common slope at first width `u i`. 

 # Global two-input envelope and a sector estimate near contact 

### `Family.ratio_contact`

 Control the excess at every width by its value in the companion
row at a single critical width. 
