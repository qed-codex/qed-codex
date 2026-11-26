---
{
  "module": "OAI/Computability/VPVNP/RAMSortedRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortedRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortedRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking the reads after the addressed Batcher sort

The canonical call buckets supply `2^d` contiguous blocks, each of width
`4 * 2^e`. The globally addressed sorting layers permute these very records.
Consequently the predecessor check on the final array recovers the original
read semantics from the headers.


### `recordWires`

 The padded records on the input wires. Outside the physical array the
wire function is extended by the empty slot. 

### `raw_recordWires`

 The finite input to the network is exactly the array produced by the
call buckets. Every comparison moves the full record. 

### `block_recordWires`

 Reading the aligned input block at site `v` uses precisely the records
from that site's canonical call bucket. 

### `sortedRecords`

 The five-word slots after the last addressed layer of the network. 

### `flatten_sorted_record_blocks`

 Concatenate the final blocks scanned by the physical site validators,
retaining every padding slot. 

### `sortedRecords_perm`

 The physical ascending output contains exactly the original padded records. 

### `sortedRecords_sorted`

 The physical output is in the paper's padded-key order. 

### `sortedRecords_read_check`

 The local predecessor rule applied to the actual sorting-network output
accepts exactly the correct read guesses of the original RAM events. 
