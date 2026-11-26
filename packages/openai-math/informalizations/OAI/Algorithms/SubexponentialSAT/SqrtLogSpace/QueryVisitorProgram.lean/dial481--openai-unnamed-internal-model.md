---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed two-pass visit of one emitted attained-signature tuple. The first
pass reconstructs the entire ambient representative assignment; the second
rescans the assignments in each head against those fixed foreign values.
Every concrete subroutine is fixed here, without an evaluator argument. 

### `loadHead`

 Load the head at the reverse traversal's paid unary address. The suspended
DFS address on845 and its representative frames remain caller data. 

### `baselineHead`

 Install each representative into the ambient tuple before evaluating any
head. This pass also handles zero-width heads by consuming their real frame. 

### `evaluateLoadedHead`

 The full key and factor-record stream are staged once per head. All raw
head assignments then pass through the concrete key/correction gate, factor
evaluator, and addition/reset path before multiplication into the tuple. 

### `visitor`

 One fixed visitor reconstructs representatives, evaluates all head sums,
and adds the completed product to the current finite-difference pair. The
unit construction and empty passes retain the empty-tuple contribution. 
