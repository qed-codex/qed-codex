---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Correctness of the fixed head rescan. The invariant retains the current
normalized dictionary and the actual immutable source words. Its compact
boundary is reused after every candidate; no execution service is assumed. 

### `retainedPorts`

 All words retained by one head, excluding its changing cursor and sum. 

### `advance`

 The semantic sum and immutable inputs survive the real increment and
countdown, including the terminal assignment overflow. 

### `actual_product_value`

 Exact physical high/mask words and the actual ambient overlay identify the
whole assignment product with the original free-variable source expression. 

### `run`

 The fixed head program produces the exact restricted signature-fiber sum.
Both resource bounds refer to this same run; every retained stack is counted. 
