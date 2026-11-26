---
{
  "module": "OAI/Algorithms/SubexponentialSAT/MonomialCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/MonomialCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/MonomialCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting the retained symbolic monomials

The exponent vectors are genuine natural-valued functions (and, equivalently,
finitely supported functions) with a bound on the sum of their entries.  Adding
a slack coordinate identifies them with weak compositions, so that stars and
bars counts the actual exponent vectors.


### `BoundedExponents`

 Exponent vectors in `D` variables of total degree at most `N`. 

### `slackEquiv`

 Adding the unused degree as the first coordinate makes a weak composition. 

### `boundedEquivSym`

 The stars-and-bars equivalence for degree-bounded exponent vectors. 

### `card_boundedExponents`

 Exact cardinality of the actual degree-bounded exponent vectors. 

### `BoundedFinsupp`

 The equivalent exponent-vector type used by multivariate polynomials. 

### `RetainedX`

 The retained `X` monomials for `μ = D + 1`. 

### `card_retainedX_pow_five_le`

 The fifth power includes four symbolic-operation factors and one moment loop.
This is an arithmetic bound on the index count, not a machine-runtime theorem. 

### `UZIndices`

 Independent retained exponents of `U` and `Z`. 

### `RetainedMonomial`

 A coefficient slot in the full canonical symbolic representative. 
