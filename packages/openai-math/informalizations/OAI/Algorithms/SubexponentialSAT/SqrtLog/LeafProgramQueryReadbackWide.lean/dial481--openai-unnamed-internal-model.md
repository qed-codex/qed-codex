---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryReadbackWide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryReadbackWide.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryReadbackWide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Relocation of the concrete reader into the shared marked/branch caller. 

### `run`

 The caller pays the reader's compiled halt instruction. All additional branch/setup
stacks and their controller registers are physically framed. 

### `run_at`

 Readiness is stated on the real wide caller tapes, without requiring a
caller to supply a preconstructed embedded machine state. 
