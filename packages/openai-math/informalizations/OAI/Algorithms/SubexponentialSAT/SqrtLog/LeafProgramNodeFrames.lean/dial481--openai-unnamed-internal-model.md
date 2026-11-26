---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid conversion of flat fixed-width node words to framed node records.
Both the width and the number of nodes are read from runtime unary tapes. 

### `trace`

 Every output delimiter is written by the audited frame-producing loop. 

### `callerRegisters`

 The old flat-node slot becomes empty and the preserved master framed list
is installed at300, exactly as required by the node moment iterator. 
