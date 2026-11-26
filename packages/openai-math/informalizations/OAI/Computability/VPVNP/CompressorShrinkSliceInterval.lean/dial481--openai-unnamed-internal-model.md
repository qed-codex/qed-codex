---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSliceInterval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceInterval.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceInterval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Shrinking tables survive writes to the descriptor header

The AB and CD interval lookups use cells between the first slice table and
the ordered-slot workspace. The forward and inverse slot lookups use cells
in the workspace. The two transfers only need agreement on those ranges.


### `SliceReadbacks.transfer_interval`

 Slice-table readbacks require agreement only from the AB base through
the end of the CD tables. Earlier header or resident cells may be written. 

### `OrderedTables.transfer_interval`

 The sorted endpoint and inverse-field tables use addresses inside the
ordered-slot workspace. 
