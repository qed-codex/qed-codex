---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesScalars.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesScalars.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesScalars.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Polynomial numerical dimensions of every actual large-input query.
These bounds do not include serialized bucket or sparse-dictionary buffers. 

### `SmallInputs`

 This cap applies to scalar counts only. The free/incidence counts are
read from the native scan; no independent statistics are supplied. 

### `eventually_small_inputs`

 All scalar input fields are bounded together, with one cutoff depending
only on k and the initial occurrence exponent. 
