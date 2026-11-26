---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeaf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeaf.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeaf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual adapters for the streamed counting leaf. Both initial code rows
and newly generated rows use the canonical modulus word's exact width. 

### `route_space`

 Each concrete route clears its destination before copying, so its
temporary and destination fit the original source-word envelope. 

### `clearOutput_space`

 Clearing a port never enlarges any retained word, including before return. 

### `clearSequence_space`

 The fixed bank cleanup preserves the incoming per-stack bound. 

### `copyWord_space`

 The copy table preserves its source and never needs a word longer than
that source when its destination and scratch are initially empty. 

### `loadLeaf_space`

 Clearing, resetting and copying the three actual leaf inputs retain the
same per-stack envelope, even when the ambient numeric words are padded. 

### `exportLeaf_space`

 Exporting the full count word and clearing the leaf bank also preserves
the incoming envelope at every prefix. 

### `loadLeaf_input_bound`

 The loaded leaf is small independently of the suspended DFS envelope.
The two parameter word caps come from concrete pre-DFS production. 
