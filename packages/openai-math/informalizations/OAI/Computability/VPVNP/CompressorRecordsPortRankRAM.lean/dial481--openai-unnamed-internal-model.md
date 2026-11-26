---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsPortRankRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsPortRankRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsPortRankRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-degree rank worker indexed by the old outgoing port

The burst call loads the port's classified owner, its key, and its owner's
count. It scans a fixed number of cells in the owner's key row. A saturating
countdown masks the unused tail of a thick row, so the initial contents of the
tail cells are immaterial. The resulting rank is written at the old port's
absolute address, and the returned cursor advances to the next port.


### `Ops`

 Straight-line instructions for the old-port rank worker, with nine private registers and
six public operands. 

### `owner`

 Read the classified owner of old port `i` from the owner column addressed by public operand
zero. 

### `pivot`

 Read the key of old port `i` that the worker compares with keys belonging to the same
owner. 

### `lengthAt`

 Read the number of valid entries in the old port owner's key row from the count column. 

### `start`

 Address of the first key in the old port owner's row, computed from the key-array base,
owner index and row stride. 

### `row`

 Sample `cap` consecutive key words beginning at the old port owner's row, including any
unused tail cells. 

### `result`

 Rank of the old port's key as a machine word. Count strictly smaller keys in the sampled
row prefix limited by the owner's stored count. 

### `visit`

 One straight-line template for all old ports of the same fixed degree. 

### `run_one`

 Actual native execution on arbitrary external words, including unused row
cells equal to the largest representable word. 
