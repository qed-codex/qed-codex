---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafOuterProgramStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafOuterProgramStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafOuterProgramStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact composition and memory charging for fixed outer-leaf stages. 

### `stage_bounded_eval`

 Uniform linear overhead, including dirty subprogram output cleanup.
The native subprogram's own trace budget is the only non-storage term. 

### `eval_stackBits`

 A long-running subprogram may dirty its workspace. This standard bit
trace estimate charges that dirt by its actual number of instructions. 
