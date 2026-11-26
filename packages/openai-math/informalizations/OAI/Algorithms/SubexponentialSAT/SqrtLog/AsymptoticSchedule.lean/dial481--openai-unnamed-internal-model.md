---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact, computable square-root-log scheduling. No algorithmic assertion is
hidden in these numerical lemmas. Small inputs may have schedule zero. 

### `sqrt_logSize_le`

 An explicit lower-bound comparison, with the only small-input condition
being positivity of the actual integer schedule. 

### `eventually_schedule_comparison`

 Both comparisons have absolute constants; the lower bound is eventual
because the exact integer schedule is deliberately allowed to be zero. 
