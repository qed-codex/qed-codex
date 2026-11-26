---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling the local slot arrays in address order

A scan over absolute endpoint fields visits each genuine arc in relative-key
order, followed by the padding arcs. Nonexistent mixed-radix IDs are each
sent to a separate unused row, so the scan requires no preliminary compacting
pass. Each real row then contains the absolute field addresses in slot order.


### `Directory`

 Numeric endpoint field space and the selected owners for the current layout. 

### `Directory.address`

 Inject each genuine or dummy endpoint field into its absolute address in the candidate
  range. 

### `Directory.decode`

 Decode an absolute candidate address to its endpoint field when occupied, returning none
  for a hole. 

### `Directory.owner`

 Real owner row to which an endpoint field is assigned under the chosen layout. 

### `Directory.destination`

 Allocate an auxiliary row for each unoccupied address. Its count is at most one. 

### `Directory.wordOwner`

 End-site index stored in the owner array for each candidate absolute field. 

### `real_prefix_length`

 Among the fields scanned before cursor `k`, the real entries of row `b`
are exactly the identified endpoints in that row with address below `k`. 

### `parameters`

 The count and bounded row arrays lie immediately after the owner stream. 

### `fill_run`

 A complete sequence of native append calls fills all rows. Empty row
counters are the only initialization needed beyond the selected owner stream. 

### `stored_at_rank`

 The entry indexed by the number of earlier incident fields is exactly
this field. This read uses a single directly addressed cell in the filled array. 

### `sortedFields`

 Number fields first by their row owner and then by increasing numeric
field address within the row. Every real row has the fixed degree `deg`. 

### `sortedFields_val`

 The contiguous real rows have this concrete rectangular address order. 

### `rectangular_rows`

 Every cell of the real rectangular array holds its designated absolute
endpoint field. The spare rows for holes follow the entire real array. 

### `Tables`

 Direct row lookup and its inverse, after both native array passes. 

### `scatterParameters`

 Allocate the inverse immediately after all bounded rows. 

### `build_tables`

 First fill the rectangular rows, then invert only the real rows. The
scatter pass starts with the physical post-memory of the population pass.
The two final tables agree on every occupied field. 
