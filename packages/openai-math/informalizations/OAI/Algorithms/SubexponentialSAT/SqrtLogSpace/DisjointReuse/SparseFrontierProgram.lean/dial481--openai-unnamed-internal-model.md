---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseFrontierProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseFrontierProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseFrontierProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete LIFO storage for normalized formula bodies.

Stack zero is the current body, stack two is the framed pending list, and stack
three is scratch. Stack one is preserved and may hold the declared variable
count. The list's final false bit is retained; emptiness is tested by peeking,
so an empty frontier never causes an unguarded removal of a sentinel.


### `push`

 Consume the current forward body and prepend its escaped record. 

### `initFrontier`

 Initialize the one-root frontier with its physical empty-list sentinel. 

### `pop`

 The head is known to exist: remove its list tag, parse its frame, then
restore forward order on the empty current-body port. 

### `test`

 The test preserves every stack, including the empty-list sentinel. 

### `popIfPresent`

 A public pop operation tests the sentinel itself. Empty work is a no-op
on every stack, rather than a removal of the final delimiter. 

### `push_prefix_space`

 A local linear-time push cannot allocate more than a linear amount of
temporary data. The saved declared-n word is included explicitly. 

### `pushPair`

 The splitter may already return framed children. This fixed command
consumes B then A and never touches the saved declared-variable word. 
