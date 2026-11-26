---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutScalarEmitter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutScalarEmitter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutScalarEmitter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Preserving signed-pair emission into a reverse buffer. The existing exact
pair serializer is called on paid copies, and its output is transferred once.
All source words survive; the four work stacks are restored to empty. 

### `emitPair`

 P0,N1 survive. Buffer2 is extended. Scratch3--6 starts and ends empty. 

### `finishList`

 Append the final false tag, then reverse the complete accumulated list. 
