---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Progress and footprints of the executed AB calendar

Each reset sequence advances the global bundle cursor and reads inside the
four input columns and the allocated bundle banks. These inputs suffice to
replay the full calendar. Applying the frame theorem to every compatible
initial memory shows that all emitted writes stay in the data region.


### `Guarded`

 The AB worker runs from cursor zero to the row count and all reads and writes in its report
log lie in the supplied data region. 

### `guarded_walk`

 The same fixed stage list as the graph builder, with the scheduler's
per-packet progress, read and write predicates proved for its actual reports. 
