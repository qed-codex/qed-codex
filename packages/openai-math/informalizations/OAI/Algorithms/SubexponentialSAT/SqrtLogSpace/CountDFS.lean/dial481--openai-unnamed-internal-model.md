---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CountDFS.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CountDFS.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CountDFS.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Typed refinement of the concrete streaming frontier.

Depths and derivation trees below are proof indices. The physical pending tape
contains only formula bodies, and every formula keeps the same declared `Fin n`.
The selector and leaf execution contracts must still be supplied by their actual
finite programs; this module does not postulate a final counting service.


### `Boundary`

 The loop boundary charges original input and parameter words separately.
Only the invariant ports needed by the count/frontier refinement appear here. 

### `Valid`

 Normalized syntax invariants are retained even though encountered clause
order differs from the canonical finite-set encoding. 

### `Transition`

 Every raw step names the actual disjoint list outputs. Leaf exact counts
here specify the semantic transition, and do not compute a runtime callback. 

### `Derivation`

 This proof-only tree follows the actual encountered-order children. 

### `childA_body`

 The encoded core child agrees with the typed result literal by literal. 

### `finished_output`

 Once the actual raw transition refinement reaches an empty frontier,
export copies its canonical exact count to the physical output tape. 

### `AfterVisit`

 Persistent words after a concrete branch or count addition. Scratch and
current-formula cleanup is performed by the real finishVisit command. 
