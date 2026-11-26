---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleKeys.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleKeys.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleKeys.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bundle addresses and relative sorting keys from physical source ports

The classifying scan reads both thickness flags and the bundle assignment at each
endpoint. Its table separates thick wires from CD wires while retaining every
old port as its absolute identifier. Sorting keys remove the residual lane and
retain the original port, mask, and slot-label fields.


### `numericBucket`

 The two bundle arrays are adjacent. A CD wire belongs to its thin endpoint,
with the source used when both endpoints are thin. 

### `numericKey`

 The thick-wire key uses the two suppressed source fields. The motif key
includes the normalized source base, tag and physical outgoing slot. 

### `OldArc`

 An arc in the pre-shrink graph, carrying the source port, lane information, and mask used
to classify it into a packed bundle. 

### `oldArcOrder`

 Scan each physical outgoing slot, keeping the separate parallel-port numbers. 

### `bundleAddress`

 Numeric owner of either kind of bundle in the combined count and row arrays. 

### `numBundles`

 Number of packed port bundles in one of the two classification arrays, also the offset
where the CD bundle array begins. 

### `keyAt`

 Compute an old arc's within-bundle sort key from the decoded source number and outgoing
slot, using the thick-wire or CD ordering as selected. 

### `thick_key`

 The value emitted in a thick bundle equals its sort key at its actual lane. 

### `motif_key`

 The CD sorting key is the key of the normalized original arc in Appendix C. 

### `siteRow`

 Four stored placement columns and the source and target vertices of the assigned
bundle, expressed solely in terms of the constructed packing. 

### `bucketFromRows`

 Look up the independently stored source and destination placement records. 
