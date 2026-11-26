---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramExpansion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native expansion of one selected raw hash row.  The row is read from the
dispatcher result; every original clause lookup and coefficient lift is paid
by the fixed assembler.  The original formula and dynamic width words are
read in place, so they remain available for the next factor. 

### `command_eval`

 The only inputs besides the actual row/source bytes are represented
runtime dimensions.  In particular, the theorem does not assume a supplied
inline row or a trace for a source lookup. 
