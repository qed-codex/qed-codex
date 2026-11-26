---
{
  "module": "OAI/Computability/VPVNP/PairVirtualCursorLeafExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualCursorLeafExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualCursorLeafExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native leaf execution on the virtual pair's scan state 

### `nativeNumberedLeaf`

 On the scan's original coordinate numbering, the leaf handler accepts
and rejects exactly as its machine entry does on every stored cursor packet. 

### `VirtualPairs.cursorLeafExact`

 Success and rejection for the installed vertex machine at any leaf packet
of the selected virtual pair. Its cache contains the actual auxiliary data. 

### `CanonicalScan.CursorLeafExactCalls`

 At each reached vertex, the same private arena supplies both exact
execution on arbitrary nomination tapes and the selected cursor jobs. 

### `eventually_virtualCursorLeafExactCalls`

 One threshold supplies the exact native cursor handler and its selected
row effects for every nomination and chronological vertex of the fixed pair. 
