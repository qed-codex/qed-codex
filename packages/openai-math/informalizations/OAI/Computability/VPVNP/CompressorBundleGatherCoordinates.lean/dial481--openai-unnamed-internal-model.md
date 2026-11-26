---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleGatherCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleGatherCoordinates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleGatherCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense cursor order and physical addresses for the fixed-bank key gather

Each cursor decodes to a packed port and an element of the disjoint sum of
its thick and motif entries. The physical address embeds this sum into two
separate sets of equal-stride rows. Both maps work with empty classes.


### `Entry`

 A live entry identified by a bundle and either a thick-wire index or a motif index. 

### `entryCount`

 Total number of live thick-wire and motif entries across all bundles. 

### `slots`

 Number of physical slots reserved for the two strided row banks, including padding. 

### `entryIndex`

 Number the live entries consecutively, using the thick-wire indices before the motif
indices within each bundle. 

### `physical`

 Place thick-wire entries in the first bank of rows and motif entries in the second,
retaining their index within each row. 

### `slot`

 Map the dense cursor range bijectively onto the live rectangular slots. 

### `parameters`

 The gather worker's seven operands, encoding the row dimensions and the identifier,
lookup-key and output bases. 

### `offset_eq`

 The native decoder gives the exact embedded slot. The stop word of the
absolute-port scan represents its full entry count. 
