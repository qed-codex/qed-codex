---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutNumerator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutNumerator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutNumerator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer numerators for the actual universal swap matrices

The parity coefficients are the immutable library's coefficients, instantiated
over the integers. Their images are the same coefficients over every
commutative ring. Clearing the projector denominators uses only powers of two.


### `integerDifference`

 The same ordered difference product, without requiring a field. 

### `entry`

 Each summand is a literal integer; no rational rounding is used. 
