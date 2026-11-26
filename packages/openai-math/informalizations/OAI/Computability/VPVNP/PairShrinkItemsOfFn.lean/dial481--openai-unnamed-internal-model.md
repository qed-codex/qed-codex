---
{
  "module": "OAI/Computability/VPVNP/PairShrinkItemsOfFn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkItemsOfFn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkItemsOfFn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact items in a finite resident map row

The native map loop advances one word after each occurrence. The actions
at the finite row ordinals therefore form an exact list starting at the
published row base, including the empty row.


### `Items.ofFn`

 Consecutive source words turn the indexed occurrence proofs into the exact loop list. 

### `MapRowSource.rowStart`

 Address of the first resident-map slot of a site, including sites with no entries. 
