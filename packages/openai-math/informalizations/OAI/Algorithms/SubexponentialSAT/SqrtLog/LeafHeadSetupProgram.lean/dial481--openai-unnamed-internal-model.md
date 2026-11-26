---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafHeadSetupProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafHeadSetupProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafHeadSetupProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed physical per-node head setup. Each head is selected from the actual
word table; its complete all-incidence matrix is built and bucketed; the
actual attained buckets are appended to the Cartesian stream. The entry
command is the sole explicit service parameter and must be instantiated by
the concrete LayoutProgram integer entry before claiming a closed solver. 

### `wide_execution`

 Any completed execution of the concrete local program embeds into the
40-register leaf worker while preserving all registers16..39. 
