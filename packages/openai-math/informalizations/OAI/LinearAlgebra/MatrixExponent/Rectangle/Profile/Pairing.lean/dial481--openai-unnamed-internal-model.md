---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Profile/Pairing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Profile/Pairing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Profile/Pairing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial multiplication with many input lengths

The output has the sum of the input lengths as its capacity. Extra
coordinates, if any, have zero coefficients.


### `polynomial_rank`

 Vandermonde evaluation and interpolation give one rank-one term
for each available output coefficient. 

 # Three labelled sites with two inputs and one output 

 # Finite row inequalities for ordered polynomial multiplication 

### `BinaryLaw`

 The finite determinant and tripling inequalities, in degree indices. 

 # Keeping the weight-zero coefficients of a nonnegatively graded tensor 

 Grading away unequal labels exposes a diagonal of identical copies. 


# Equal-block degeneration

For block number `a`, length `l` and offset `d`, assign the input the
integer weight `a(a-1)l + a(2d+1)`. Its excess above the supporting
line for the output block `b` is positive unless `a=b`. The supporting
lines add to the output weight because degrees add.


 # Continuum profile for univariate polynomial multiplication 

 # From ordinary base-two prices to natural-log profiles 

 # Reindexing the two-input polynomial tensor 

 # Width profiles on a three-point placement 

 Restrictions by absorbing the last input at the output site or extracting a fixed total degree. 

### `shift`

 An out-of-range difference uses the spare output coordinate of the pair. 

### `extract_pair`

 Pin the output at degree `L i + L j - 1` and reverse the degree
on input `k` to expose a two-input polynomial with output at `k`. 

 # Compatibility of the width profiles with site permutations 
