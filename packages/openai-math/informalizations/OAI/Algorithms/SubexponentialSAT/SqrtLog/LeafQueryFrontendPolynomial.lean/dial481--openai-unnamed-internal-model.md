---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendPolynomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendPolynomial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendPolynomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `inputBudget_polynomial`

 One fixed polynomial bounds the complete frontend from its physical input
capacity, uniformly over queries and fixed-width choices. 

### `frontend_time_polynomial`

 Every actual native frontend run satisfies the same ordinary-polynomial
bound; no intermediate state, computed parameter, or free statistics input is
assumed in this theorem. 
