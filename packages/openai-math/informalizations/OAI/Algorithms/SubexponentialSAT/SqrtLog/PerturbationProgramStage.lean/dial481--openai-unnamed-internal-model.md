---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact staging from the source polynomial executor ABI to the padding ABI.
The node and protected arithmetic caches are unchanged. 

### `stageInput`

 Consume the source coefficient stream on240; copy its protected runtime
coefficient count193. Ports246/248 are the padding input stream/count. 
