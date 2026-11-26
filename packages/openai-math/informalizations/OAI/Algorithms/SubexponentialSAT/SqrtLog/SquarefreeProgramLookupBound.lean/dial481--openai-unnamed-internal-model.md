---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramLookupBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramLookupBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramLookupBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The lookup suffix is bounded by the original table. This explicit bound
pays for reclaiming the unused suffix in dictionary updates. 

### `scan_eval_tail`

 An actual first-match scan of the encoded table. All scratch strings are
cleared by the existing record routine before the next iteration. 
