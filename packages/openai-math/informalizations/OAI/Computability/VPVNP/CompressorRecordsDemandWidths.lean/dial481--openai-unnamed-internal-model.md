---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsDemandWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Simultaneous demand and thick-wire width columns

After the sorted-width scatter and the two old-field prefix scans, one native
balanced-piece scan materializes all AB widths. It preserves the sorted CD
widths, the original thick-wire widths, and the starts of both old field
families. Thus the AB and CD words for a single term share a bundle and rank.


### `Outside`

 An old rectangle lies outside each of the new AB output rectangles. 

### `packedPublic`

 Allocate two dense AB rectangles of equal extent, with the total column
already reserved at its supplied address. 

### `Stored`

 All demand widths and all old and AB field offsets in one memory snapshot. 

### `complete`

 A fixed scan gives both sides of the input to every demand motif and the
two orderings needed by the AB-copy kernel at its endpoints. 

### `from_ranked_input`

 Scatter the ranked actual widths, compute both old-field prefix rectangles, and
then materialize the AB widths. These four segments use one post-memory after
another. Their combined cost is ten units per old port plus four per motif. 

### `allocation`

 Following the old sorted-width rectangle, reserve the two old-start
rectangles, the two old-total columns, and finally the AB width and start
rectangles. One last-address bound suffices for all three subsequent scans. 
