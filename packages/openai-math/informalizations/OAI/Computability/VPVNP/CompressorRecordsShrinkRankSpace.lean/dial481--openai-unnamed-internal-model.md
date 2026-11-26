---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkRankSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkRankSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkRankSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The rectangular work area for ranking old arcs

Starting at a fresh address, reserve absolute owner and key columns, a count
per bucket, two bounded ID and key rectangles, and the final absolute rank
column. The two classes of bundles share the larger CD stride.


### `degree`

 Number of outgoing slots at each site when the slot index uses `a` bits. 

### `cap`

 Number of CD pieces per bundle, used as the common row capacity for motif and thick-wire
buckets. 

### `slots`

 Total number of old outgoing ports to rank, counting every outgoing slot of every old
position. 

### `bundles`

 Number of bundles in each class, one for each outgoing slot of each packed site. 

### `rectangle`

 Word count of one complete ID or gathered-key table, including the padded thick-wire rows
and the motif rows. 

### `Shape`

 Dimensions and starting address of the workspace that classifies old ports by bundle and
ranks them within each bucket. 

### `Shape.vertices`

 Number of base vertices before accounting for tags, lanes, or outgoing slots. 

### `Shape.degreeBits`

 Bit width of a slot index. It determines the degree, tag width, and number of colors used
  to size the arena. 

### `Shape.residualBits`

 Bit width of the residual lane retained alongside the tag at a packed site. 

### `Shape.origin`

 First address reserved for the rank arena, where the per-port bucket owner column begins. 

### `A`

 Number of old outgoing ports, and hence the length of each column indexed by absolute port
ID. 

### `B`

 Number of packed outgoing ports. Each port indexes one thick-wire bucket and one motif
bucket. 

### `Q`

 Common row stride for the two bucket families, equal to the number of CD pieces per bundle. 

### `rectangleSize`

 Words reserved for one rectangular table with two rows per bundle and `Q` slots per row. 

### `owner`

 Base address of the column mapping each absolute old port ID to its bucket. 

### `key`

 Base address of the sorting key column indexed by old port ID, immediately after the owner
column. 

### `counts`

 Base address of the live entry counts for all thick-wire buckets followed by all motif
buckets. 

### `ids`

 Base address of the bucket rows listing absolute old port IDs, directly after the count
column. 

### `gathered`

 Base address of the key rows, where each key occupies the same bucket and offset as its ID
in the preceding table. 

### `ranks`

 Base address of the column storing each old port's rank within its bucket, indexed by
absolute port ID. 

### `stop`

 First free address after the rank column, marking the end of the rank arena. 

### `classifyBank`

 Public words for classifying each old port, including the packing radices, incidence and
placement columns, and the destinations for its bucket and sort key. 

### `collectBank`

 Public words for collecting old port IDs into bucket rows, specifying the owner column,
count column, row stride and ID table along with their dimensions. 

### `Values`

 Natural values of every newly allocated address. 

### `gatheredTable`

 Describe the dyadic gather table that looks up each collected port's absolute key and
writes it to the matching bucket slot. The descriptor also identifies the old width column. 

### `regions`

 All count/row, gather, and rank layout conditions follow from the final
address bound and the position of the old width array. 
