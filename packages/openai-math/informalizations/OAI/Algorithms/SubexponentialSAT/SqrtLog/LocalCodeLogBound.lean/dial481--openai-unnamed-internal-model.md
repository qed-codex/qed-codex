---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LocalCodeLogBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LocalCodeLogBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LocalCodeLogBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The reviewed log-size variant of the local code, using only integer bounds. 

### `exists_local_code_log_bound`

 An unconditional finite local-code existence theorem. `ell` only needs
to bound the binary logarithm of the local length; no entropy estimate is
assumed. The row budget is expressed without rounded division. 
