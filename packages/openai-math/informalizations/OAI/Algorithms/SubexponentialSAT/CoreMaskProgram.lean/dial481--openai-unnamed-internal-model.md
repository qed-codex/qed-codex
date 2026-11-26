---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CoreMaskProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CoreMaskProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CoreMaskProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Applying a runtime mask to an encoded clause

The mask and clause occupy separate Boolean stacks.  Selection consumes one
mask bit per literal, treating a missing bit as false and leaving excess mask
bits unread.  Payloads are copied as framed bit strings without interpreting
their contents.


### `maskForSubset`

 Explicit membership mask, padded to the caller's fixed mask width. 
