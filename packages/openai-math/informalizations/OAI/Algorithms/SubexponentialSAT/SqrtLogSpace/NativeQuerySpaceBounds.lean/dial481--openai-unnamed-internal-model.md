---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQuerySpaceBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQuerySpaceBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQuerySpaceBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Polynomial space for the actual complete marked and accepted queries.
The input cap is the same immutable leaf bound used by preparation. The
conditioned stream, high loop and whole-word return use their own proved
prefix bounds; no query runtime or number of attained tuples enters space. 

### `querySpace`

 Exactly the prefix expression of the completed native query, with the
source and field allowances chosen by the actual literal-query caller. 

### `envelope`

 A fixed polynomial sum dominates the nested physical prefix maxima. 

### `envelope_bound`

 The field-cardinality allowance is A+S+2 because the real serialized
port44 stores 3^d-2 and is bounded by S. The source dimensions t,d,J come
from the same produced numeric bank. Suspended words remain a separate max. 

### `polynomial`

 Coefficients and degree are fixed before the query, mark, source state,
node, signature or head assignment. This substitutes the genuine common
leaf bound directly; the retained hidden frame never enters the polynomial. 

### `shadow_polynomial`

 The bounded shadow query has no suspended frame, so its complete
source-prefix bound is this fixed polynomial in the true encoded input. 
