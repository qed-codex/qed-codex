---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgramNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgramNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgramNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Preserving physical wrapper for the Boolean head-weight scan. The actual
ring zero and one are arbitrary runtime words, so the ring degree is dynamic. 

### `command_eval`

 Every input word is preserved and all four private work stacks are empty
at return. Only the output word and registers can change. 

### `program_lifted`

 Generic caller relocation preserves every nonlocal register and stack. 
