---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeKeyMapProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeKeyMapProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeKeyMapProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Public native sparse-key mapper. The instruction table is independent of
the keys, clipping limits, coefficient width, and dictionary length. 

### `native_map_trace`

 The final trace has a linear dictionary-length bound, and preserves the
three caller-owned masters. All ten scratch stacks are empty on return. 
