---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeSearchNativeBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeSearchNativeBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeSearchNativeBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Numerical bounds for the actual graph-then-local code stage, including
all physical routing, saved outputs, and reused-bank cleanup. 

### `searchBoundary_le`

 Unary entry metadata already pays for both retained matrix dimensions. 

### `searchesSpace_le`

 The actual graph/local sequence has a quadratic source-prefix bound
when its exact input metadata words fit in the supplied input bound. 

### `produced_dimensions_le`

 The actual four code dimensions satisfy the original numerical height
estimate, uniformly over every leaf with the chosen occurrence cap. 

### `searchesTime_le_envelope`

 All actual routes, searches, retained outputs and clearing fit a fixed
cubic power of the original explicit numerical envelope. 

### `eventually_searchesTime`

 The complete native code stage preserves the supplied exponent scale;
its actual retained input bound remains an explicit fixed polynomial factor. 

### `eventually_produced_searchesTime`

 Uniform runtime for the actual selected dimensions. The only remaining
size hypotheses are the sparse leaf count and physical entry-word bounds. 
