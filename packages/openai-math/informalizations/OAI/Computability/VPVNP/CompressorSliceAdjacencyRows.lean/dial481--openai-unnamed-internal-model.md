---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceAdjacencyRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceAdjacencyRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceAdjacencyRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Endpoint rows of the copy-slice scan

A bounded row records all nonempty frame identifiers at an endpoint in scan order.
For a rectangular table the opposite coordinate injects the retained frames of
one row into its slot range.


### `adjPrefix`

 Nonempty frames incident to endpoint `v` among the first `k` frames. 

### `adjPrefix_old_le`

 At an old endpoint, remainders are distinct slots below the number of new endpoints. 

### `adjPrefix_new_le`

 At a new endpoint, quotients are distinct slots below the number of old endpoints. 

### `AdjBank`

 The counter array followed by the fixed-capacity rows of one endpoint class. 

### `AdjBank.countHead`

 Base address of the per-endpoint reference counts. 

### `AdjBank.refHead`

 Base address of the rectangular array of frame-reference rows. 

### `AdjBank.size`

 Number of endpoints represented by this adjacency directory. 

### `AdjBank.cap`

 Number of reference slots reserved for each endpoint. 

### `count`

 Address of endpoint `v`'s live reference count. 

### `row`

 Address of the first reference slot for endpoint `v`. 

### `stop`

 Exclusive natural-number end address of the reference array. 

### `Inside`

 The counter and reference arrays may have an unrelated table between them. 

### `Fits`

 The count array ends before the reference array and the reference array fits in the address
space. 

### `Represents`

 Each endpoint row contains exactly its positive-length frame ordinals among the first `k`
candidates, in scan order. 

### `represents_congr`

 Cells outside the bank do not enter its row interpretation. 

### `append_step`

 Appending to one row preserves the other rows and every external cell. 
