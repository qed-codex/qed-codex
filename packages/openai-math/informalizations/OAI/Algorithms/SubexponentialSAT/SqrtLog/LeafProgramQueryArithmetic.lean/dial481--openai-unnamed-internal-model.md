---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One actual arithmetic preparation per query: ring caches, interpolation
caches, then the inverse layout denominator. All three run before branching. 

### `ArithmeticOutput`

 The final arithmetic state remembers the exact generated cache state;
only port728 is added after the ring/interpolation program. 
