---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafAssignmentMergeProgramNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafAssignmentMergeProgramNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafAssignmentMergeProgramNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Preserving shell for the assignment merge. Only output9 and registers
change; the masters and both reserved words are preserved. 

### `command_eval`

 Local3 and4 are arbitrary preserved words, so this helper can share the
weight helper's ABI without overwriting the cached ring constants. 

### `program_ofFn`

 The actual program outputs the full original-ID assignment needed for
incidence beta, choosing the head assignment exactly at the supplied mask. 
