---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counted scalar implementation of the irreducible-polynomial search

The traces below execute the finite arithmetic and Boolean tests and count
their scalar operations. This is a scalar trace, not a claim that arbitrary
natural-number indexing or list construction costs one primitive bit step.
All stored scalar coefficients are in the fixed field F₃.


### `selectedTrace`

 Return the actual coefficients and both counters from one search run. 

### `searchTrace_count_nodeBound`

 When the residue field is the first ternary size above the node count,
the entire counted arithmetic search is polynomial in that count. 
