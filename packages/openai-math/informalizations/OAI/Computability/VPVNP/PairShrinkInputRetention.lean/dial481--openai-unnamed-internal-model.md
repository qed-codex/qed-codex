---
{
  "module": "OAI/Computability/VPVNP/PairShrinkInputRetention.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkInputRetention.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkInputRetention.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading original arc lists and ranks during a shrinking simulation

The append pass lists old outgoing identifiers in scan order. The gather pass
writes its keys above these lists, and the rank pass writes above the keys.
The absolute-identifier scatter reuses the gathered-key rectangle. The list
rows, counters and owners lie below that rectangle, and the ranks lie above
it. Consequently the simulation can combine the original scan-order lists
with the ranks in the selected ordering in the same memory.


### `post_eq_append`

 Below the gathered-key rectangle the width, rank, and gather scans all
preserve the memory left by the original list builder. 

### `original_preimages`

 The complete old-port lists in any later snapshot that preserves the
part of the shrinking directory preceding the gathered keys. 

### `original_ranked`

 Original ranks, owners and exact widths. The later snapshot need only
agree on the lower directory and the rank column. The gathered keys may
have already been reused for absolute motif IDs. 

### `original_after_absolute`

 Read both tables after the native absolute scatter and subsequent stages
which preserve the shrinking input area. 

### `CompleteTables.old_call_tables`

 Read all original inputs of a resident map in the final snapshot produced
by the hidden and map directories, the AB intersections, and the surviving
and ordered-slot scans. Later stages may reuse the gathered-key rectangle. 
