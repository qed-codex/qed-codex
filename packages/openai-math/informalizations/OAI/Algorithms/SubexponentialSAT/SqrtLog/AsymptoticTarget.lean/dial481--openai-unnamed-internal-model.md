---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticTarget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticTarget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticTarget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Conversion to the exact natural-logarithm target and absorption of
fixed polylogarithmic construction, search, and arithmetic overheads. 

### `eventually_polylog_bounded_target`

 Any explicitly bounded fixed polylogarithm is absorbed, irrespective of
which stage of the construction produced it. 

### `finite_prefix_absorption`

 Numerical finite-prefix absorption. This does not construct or dispatch
a small-input machine; it only supplies the uniform multiplicative constant
once the work at each exceptional dimension has already been bounded. 
