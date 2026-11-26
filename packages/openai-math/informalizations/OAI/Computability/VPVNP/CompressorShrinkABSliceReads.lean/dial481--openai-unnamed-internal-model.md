---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of a whole-level AB slice visit

Clear reads no cell. Pair tests read the two width and two start columns.
Incidence reads the frame length and at most two counts in the current
bundle's bank. These bounds hold even for arbitrary contents of those
cells. The global-row prologue consists entirely of private operations.


### `ReadRegion`

 The four physical input rectangles and the interval banks are the only
regions from which this part of the calendar may read. 

### `source_progress_reads`

 The real global-bundle cursor advances from zero to the planned stop.
Its emitted events read only the actual columns and bank rectangles. 
