---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering the two bundle numberings from the classified arc directory

The preimage pass stores original arc IDs. To rank one of them, gather the
keys at those IDs into a consecutive row and run the native rank scan on the
row. Both steps use the same actual arc order, including distinct parallel
arcs. Their order in memory can differ from their order by relative key.


### `thickRow`

 The typed thick row is in the actual ID order used by the append scan. 

### `motifRow`

 The typed motif row has the same indices as the native row of original IDs. 

### `Gathered`

 A successful native key scan on this bundle, together with the untouched
old width column. Its report sequence includes all addresses and costs. 

### `gather`

 From the actual memory of the preimage pass, gather keys by indirect lookup.
Every returned position now addresses the classifier's key for its typed arc. 

### `thick_read`

 Materialized row addresses correspond one-for-one to old thick wires.
The classifier column can be populated anywhere disjoint from the destination. 

### `gather_rank_thick`

 Gather an actual DD row from the classified directory. Starting in that
post-memory, ranking any of its members writes its concatenation number. 

### `gather_rank_motif`

 Gather the actual CD row and rank a member to obtain its AB piece number
in the sorted bundle numbering. 
