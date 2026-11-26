---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshFrontFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshFrontFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshFrontFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Guarded refresh gather, directory and segment scans

The first two scans read only the old incidence columns. The offset scan reads the new
scratch columns, using the translated destination stored by the bundle scan. All three
write inside the selected level's allocation and return consecutive ordinal cursors.


### `OldCell`

 An address in one of the six old incidence columns within the specified segment count. 

### `LevelCell`

 An address in the half-open interval allocated to this refresh level. 

### `gather_scan`

 The entire gather reads the old width permutation and writes only inside the selected level. 

### `bundles_scan`

 Every bundle reads an old target and displacement, initializes three scratch cells,
and advances the ordinal and the genuine partial-directory invariant. 

### `offsets_scan`

 The selected segment permutation stays inside the scratch arrays in every prefix. 
