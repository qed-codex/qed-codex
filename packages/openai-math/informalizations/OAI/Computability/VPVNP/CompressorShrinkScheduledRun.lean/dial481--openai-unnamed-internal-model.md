---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkScheduledRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScheduledRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScheduledRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Running every shrinking visit from the common native selection state

At each reachable level the deterministic prefix leads to one fixed term
input memory. For any admitted selection the following native packet and all
of its deterministic continuations build and publish the actual output graph.
The full suffix has exactly the length prescribed by this script's window.


### `next`

 The destination level of shrink step `i` in a live block round, one level past its source. 

### `old`

 The source level of shrink step `i` in a live block round, at offset `i.val` from the
round's first level. 

### `column_lower`

 Every real column used by a pass lies in the descriptor data suffix. 

### `PacketFacts`

 Facts of the physical shrinking interval. Keeping their component types
as parameters also lets the kernel check each large stage separately. 

### `Result`

 Complete native packets and the physical readbacks needed by the next
level and by the terminal traversal. 
