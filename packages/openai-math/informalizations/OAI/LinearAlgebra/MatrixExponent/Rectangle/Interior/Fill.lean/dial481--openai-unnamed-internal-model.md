---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Interior/Fill.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Interior/Fill.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Interior/Fill.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Private formulas and shared measurements 

### `Port`

 A batch of independent products, indexed by the group and two
outer indices. The right input has column before inner index. 

### `Seed`

 Common measurements in this seed vanish whenever the two inputs
belong to the same group and the same summation index. 


# A joint outer-product and dot-product identity

Use two affine lines of each nonzero slope in a finite auxiliary field.
Each pair of a left and a right line intersects exactly once, except
parallel lines of the same slope. Subtracting the product at every grid
point from the unrestricted product leaves the dot product of equal
slopes. All encoder entries are zero or one over the target field.



# One distinguished position per block

Use a line slope in one position, and ordinary indices in the
others. Reading the dot-product identity at the distinguished
position gives independent products, all with the same correction
dictionary indexed by words of ordinary grid points.


### `blockSeed`

 The auxiliary field indexes zero-one coefficients over `F`. 

 # Choosing the grid to retain a quadratic saving 

### `parameters`

 The width overhead grows linearly in the mesh parameter while
the block length grows quadratically. A mesh parameter proportional
to the inverse gap leaves room on both output sides. 

 # Tiling output rectangles while retaining private products 

### `tile`

 Glue independent square tiles by identifying the inputs they share. 


# Converting short sums to private products

Across a square array of groups, a short sum of separable forms is
itself a thin matrix product. Only the private terms of distinguished
sums remain private. All products for other sums are shared.


### `shared`

 Charge all corrections at each slot and all private products of
the common slots. 

 # Replicating private rectangles and cutting off the boundary 

 # Filling arbitrary output rectangles from a geometric sequence 


# Cost of words with many corrections

Give each correction letter weight `2^(b+1)`. If even the weighted
correction alphabet is no larger than the output alphabet, the
high-correction words are at most a fraction `2⁻ⁿ` of the output
words after `b n` positions.



# Removing the middle layers of a product expansion

If the corrected coordinates vanish at intermediate error counts,
the discrepancy of the private product lies in the span of the raw
words with many errors. This uses distributivity over the ground field.



# Amplifying a private seed with an agreement code

The code forces either exact agreement at all slots, annihilating
each common term, or disagreement at many slots, annihilating
all intermediate layers of the corrected expansion.

