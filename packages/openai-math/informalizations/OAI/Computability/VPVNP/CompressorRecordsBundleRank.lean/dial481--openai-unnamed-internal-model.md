---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ranks of the CD pieces and the old thick wires in an absolute bundle

Appendix E collects two bounded lists at each packed bundle. The old arc label
distinguishes parallel wires. A CD piece is ranked by its old arc after
discarding the residual lane. A thick wire is ranked by its color and slot.
Translating either list to role-A lane zero preserves these comparisons, so
the native unsigned rank scan computes the numbers used in the shrinking step.


### `motifKey`

 Numeric key of an absolute CD occurrence, independent of its residual lane. 

### `thickKey`

 Numeric key in the old thick-wire concatenation, in outgoing numbering. 

### `sortedBundle_lt`

 The piece numbers of Appendix C compare by the relative keys even at an
arbitrary absolute bundle. Transport back uses the lane of role A. 

### `motif_rank`

 Count smaller keys in the collected CD row to recover its piece number. 

### `thick_rank`

 Count smaller keys in the collected thick row to recover its concatenation number. 

### `RankWrite`

 The native call ranks the pivot, writes the designated field and has a fixed
number of dispatches and probes for a row of this length. 

### `motif_rank_native`

 Rank and write the actual CD piece number from the bundle's unsorted row. 

### `thick_rank_native`

 Rank and write the actual thick wire's position in the concatenation. 
