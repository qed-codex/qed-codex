---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual preparation of the selector's alphabet and its two unary loop
counters. Input ports0,5,6 hold binary alphabet size, tuple depth and round
count. Port9 is an arbitrary saved row stream; other ports start empty.
The arithmetic that computes these three binary values remains a separate
caller obligation. Their expansion is performed here, with its full cost. 
