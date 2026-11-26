---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/Rank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Rank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Rank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The height and radical tests for rectangular matrix multiplication

The load at a site is the sum of its incident logarithmic wire dimensions.
This file proves the equivalence of the two numerical tests in the rectangular
rank theorem, including the cases of zero loads and saturated flattenings.


### `loads`

 The three site loads for the cyclically ordered wires. 

### `HeightTest`

 Inequality (height-bound), tested at independently chosen positive heights. 

### `RadicalTest`

 The flattening and radical inequalities of the rectangular rank theorem. 

### `heightDenom_pos`

 The diagonal-price upper bound is positive for every triple of heights. 

### `HeightTest.nonnegHeights`

 Zero-height sites are obtained by approaching from positive heights. 

### `HeightTest.load_le`

 Sending one height to infinity gives the corresponding flattening inequality. 

### `HeightTest.radicalTest`

 Minimize each summand after increasing the rank parameter, then let it decrease to
its original value. This also handles sites with load equal to that parameter. 

### `RadicalTest.heightTest`

 The converse variational inequality follows from the two-dimensional Cauchy inequality. 

### `RadicalTest.mono`

 Replacing log asymptotic rank by the logarithm of a larger rank measure
preserves both inequalities. 

### `square_lower_bound`

 For three equal loads of size two the radical inequality gives the
superquadratic exponent constant. 

### `radicalTest_of_totalWireLoad_le`

 The sum of the three wire weights always passes the radical test. 

### `square_log_lower_bound`

 At square order the log-rank bound is proportional to the base-two
logarithm of the order, including order one. 

### `square_rpow_lower_bound`

 A square tensor with the finite height bound at rank measure r has
rank measure at least the stated power of its order. 
