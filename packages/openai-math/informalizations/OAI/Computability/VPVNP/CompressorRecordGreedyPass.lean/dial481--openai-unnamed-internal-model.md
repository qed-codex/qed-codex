---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedyPass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyPass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyPass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing and reading the current compressor level

The initializer derives both greedy operand directories from the evolving level's
forward and inverse mate arrays. The color reader follows label pointers. The tag
reader additionally uses the zero and outgoing displacement cells already present
in that level. These arrays may occur anywhere outside the current output region.


### `fixed_value`

 A field outside both mutable assignments and the directory has its supplied
value throughout the complete reader scan. 

### `OffsetData`

 Existing immutable displacement data for the native tag pass. 

### `PreparedPass`

 Two consecutive native phases. The reader starts in exactly the external
memory left by the preparer's report log. Both machines reset private storage
on every call. 

### `PreparedPass.cost`

 Total calls plus probes for preparing and scanning a level with `N` base vertices. 
