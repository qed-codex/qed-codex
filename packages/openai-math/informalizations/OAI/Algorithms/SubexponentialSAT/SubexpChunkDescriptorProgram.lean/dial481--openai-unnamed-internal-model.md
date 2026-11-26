---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpChunkDescriptorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpChunkDescriptorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpChunkDescriptorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite chunk-descriptor producer

The core consumes a unary variable count on stack 0 and preserves a positive
unary chunk width on stack 1. Its two output streams are the framed unary
widths and the framed singleton scopes, in increasing chunk order. All loops
below inspect actual stack bits/presence flags. Natural-number functions in
the specifications do not occur in instructions.


### `emitBits`

 This list is part of the finite program text, never runtime data. 
