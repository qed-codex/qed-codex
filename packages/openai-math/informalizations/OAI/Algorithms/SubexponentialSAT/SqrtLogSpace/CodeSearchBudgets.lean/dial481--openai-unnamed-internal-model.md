---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeSearchBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeSearchBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeSearchBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-degree bounds for the actual streamed sparse-code search commands.
The time comparison uses the original complete numerical search envelope;
workspace is bounded separately by ordinary input words and dimensions. 

### `streamedCodeTime_le`

 Every candidate and every invalid two-bit word is charged. 

### `streamedCodeSpace_le`

 The retained code-search workspace contains no enumeration-domain factor. 

### `localCodeSpace_polynomial`

 Actual local-search storage is quadratic in ordinary dimensions and words. 

### `graphCodeSpace_polynomial`

 Graph-word comparisons contribute only a fixed quadratic storage bound. 

### `localCodeTime_le_numeric`

 The entire new local search is dominated by a fixed cubic power of the
original explicit worst-case budget, not by the old successful execution time. 

### `graphCodeTime_le_numeric`

 Both graph tuple domains are charged, including all rejected candidates. 

### `codeTime_le_envelope`

 One fixed envelope covers both complete native code searches and their
retained outputs. No accepting candidate is a hypothesis. 

### `cubic_cost_runtimeBound`

 Fixed cubic numerical overhead preserves the supplied exponent scale. 

### `eventually_codeTime`

 The input-independent cubic comparison preserves the original runtime
scale. Arbitrarily large physical input words remain in an explicit polynomial. 
