---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# How the three exponent equalities are assembled

AI drafted this autoinformalization from the original source. It is open for mathematical review.

This file gives a short final argument for each target. Its four imports concern the division-free exponent over nonzero commutative rings, the dual exponent, the rectangular circuit model and the square rank model. I read this finishing file and the challenge statement. I did not build the project or follow the imported arguments back to their premises. [Imports](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L1-L8) · [Challenge targets](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L106-L132)

**Square matrices.** Fix a field. Two equalities with a common middle term suffice. The first identifies the formal exponent at weights $(1,1,1)$ with the quantity called `omega` in the matrix-exponent development. The second evaluates that quantity. Composing them gives the stated value $9/4$. [Square equality](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L10-L12)

**The dual exponent.** The challenge defines it by taking the supremum of a subset of $[0,1]$. The finishing argument unfolds the two competing supremum definitions and compares their defining sets element by element. Once $t$ is in the interval, the nonnegativity of $t$ and of the fixed weights lets it rewrite the formal exponent through the model with whole-number matrix dimensions and cycle the rectangular weights. It can then use `dual_square` with both facts obtained from `omega_eq_and_rigidity` to reach $1/2$. [Supremum definition](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/MatrixExponent.lean#L110-L115) · [Set comparison and evaluation](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L14-L27)

**Rectangular matrices.** Here the order of the three inputs matters in the intermediate notation. The private lemma starts with `U c b a`. It selects the largest and smallest weights and recovers the middle weight by subtracting them from the sum. With the smallest weight in the last position, swapping the two remaining arguments leaves the benchmark expression unchanged. The case split on `U` uses this symmetry to reach one sorted expression. [Sorting lemma](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L29-L46)

The public statement allows arbitrary real weights. First the argument takes their nonnegative parts. It rewrites the exponent using the formula for that whole-number dimension model, now with three nonnegative arguments, and applies the sorting lemma. For example, if the smallest clipped weight is zero, the correction vanishes and the expression reduces to the sum of the two larger weights. [Clipping and final application](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean#L48-L61)
