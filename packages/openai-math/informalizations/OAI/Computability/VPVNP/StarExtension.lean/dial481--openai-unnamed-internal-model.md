---
{
  "module": "OAI/Computability/VPVNP/StarExtension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarExtension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarExtension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact extension for a prescribed width profile

Theorem 2.4(2) requires the extension to match every old tensor value and
the target of one dyadic star. Products of the old generators reduce to
one old tensor, while all star occurrences combine into one power. This
identifies the finite-generator estimates with the concrete contraction
bounds on arrays.


### `dyadicStarClass`

 The class of the star whose width at leaf `j` is `w j`. 

### `contractionClassValue_old_star_le`

 A monomial with a combined old factor and a star power obeys its target bound. 

### `contractionClassValue_old_star_root`

 The root limit of a power of one folded monomial equals its target. 

### `exists_starRate_extension`

 Theorem 2.4(2), attainment. A single new spectral point preserves every
old tensor value and realizes the profile rate as its weighted star length. 

### `starRate_isLeast`

 Equation (2.1). The minimum over all spectral points extending `F` is
attained, for each individual choice of the width profile. 
