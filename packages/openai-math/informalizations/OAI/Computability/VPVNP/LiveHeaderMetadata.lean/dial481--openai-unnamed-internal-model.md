---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderMetadata.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderMetadata.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderMetadata.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running all width, phase, and mode stages consecutively

The eleven scalar stages fill consecutive scratch words. A frame outside the
written prefix transports the scan summary, advice and original packed sites
across the real linker handoffs.


### `Field`

 A scalar metadata item produced by the live header, covering five cut widths, four phase
flags, the first-tail flag, and mode. 

### `Field.stage`

 The header stage that computes the selected scalar metadata item. 

### `Field.address`

 The physical scratch address at which the selected scalar metadata item is stored. 

### `order`

 The order of the eleven scalar metadata calls, beginning with cut widths and ending with
the mode. 

### `stageId`

 Convert a metadata position to its header stage number, with position eleven denoting the
following stage. 

### `Correct`

 The stored word has the scheduled width when needed, the encoded truth value for a flag, or
the selected mode code. 

### `Image`

 Completed fields have their mathematical values. Later cells and packed
processor sites still have their values at entry to the width stage. 

### `run_prefix`

 Execute any prefix of the eleven scalar stages. The first ten can run
before the two mode bits are known to be compatible. 
