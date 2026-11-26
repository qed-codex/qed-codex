---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The integer-signature and head-bucket enumeration costs, with the actual
joint-signature count rather than rank used as the exponential resource. 

### `enumerationWork`

 Uniform head size and joint-label estimates give this concrete enumeration
counter.  The number of heads is a polynomial factor, not an exponent n. 

### `enumerationWork_le`

 Natural integer signature range, converted to the exact binary exponent. 

### `signature_log_budget`

 With epsilon=1/(32 B r L²), total rows ≤ 2 epsilon n B means
16 r L² rows ≤ n.  Combined with the integer label-height bound, the logarithm
of the full joint signature image is at most n/(2r). 

### `eventually_enumeration_target`

 Both the label enumeration and the head assignments fit the target.
The concrete head estimate 3n/(2r) is relaxed to 2n/r, and heads ≤ n+1 is
charged through a logarithmic exponent. 
