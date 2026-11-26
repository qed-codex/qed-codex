---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleKeyMaterialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleKeyMaterialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleKeyMaterialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering classifier keys for the arcs of one bundle

The classifier stores a key for every old arc at its absolute identifier.
The preimage scan stores a consecutive row of the identifiers assigned to
one bundle. The worker looks up each identifier's key and writes it at the
same offset in a separate row. The rank scan can then traverse these keys
without changing the original identifiers or the old widths.


### `materializeKey`

 Public words are the starting addresses of the ID row, global key column,
and destination row. The persistent cursor is an offset in the two rows. 

### `materializeEvents`

 Each row entry requires an ID read, an indirect key read, and one write. 

### `KeyRowRegions`

 The output interval is disjoint from the ID row and both absolute-arc
columns. Each disjoint interval can lie on either side of the output. 

### `materialize_run`

 Gather the complete row in ID order. One call and three probes per entry
fill the destination. Every cell outside it keeps its value, including the
whole old-width column. 
