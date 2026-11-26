---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectTuple.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectTuple.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectTuple.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The concrete indexed tuple family discharges the selector's coverage
hypothesis from a supplied lower-support code. All tuples, including repeated
coordinates and repeated resulting rows, remain in the enumeration. 

### `select_cnf_with_code`

 The only semantic assumptions left are the code distance and the exact
answers of the evaluator on the actual trial matrices. 
