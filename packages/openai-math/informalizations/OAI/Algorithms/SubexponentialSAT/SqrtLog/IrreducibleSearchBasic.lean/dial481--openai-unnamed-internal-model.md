---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite coefficient tests for arbitrary-degree irreducible search

Only vectors, finite lists, and scalar arithmetic are executed. `ofFn` and
the polynomial interpretation occur solely in the correctness proofs.


### `entry`

 Read a coefficient with zero padding outside the stored vector. 

### `convolution`

 Ordinary schoolbook convolution, using no polynomial operations. 

### `candidateEntry`

 A monic candidate consists of its `d` lower coefficients. 

### `nonconstant`

 Test that a stored factor has a nonzero positive-degree coefficient. 

### `productEq`

 Compare all potentially nonzero product coefficients. 
