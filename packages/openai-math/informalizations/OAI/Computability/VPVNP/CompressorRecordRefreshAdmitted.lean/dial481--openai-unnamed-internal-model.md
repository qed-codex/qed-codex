---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshAdmitted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshAdmitted.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshAdmitted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native term choices of a degree refresh

Each port block's dense demand vector is read from its generated record. A single native
call at the block ordinal selects a fixed grid row, computes the repetition count and checks the admitted
supply payload. The successful bit streams biject with the actual branch choices of the
refresh. The width threshold is fixed before the number of blocks or the old widths.


### `termConstant`

 A sufficient word-width constant for this fixed motif, independent of the old state
and the number of its port blocks. 

### `termRows`

 Tightly packed input rows and arbitrarily strided output records, both in block order. 

### `termInputs`

 The supplied numerical rows are read by the exact term compiler. 

### `blockTapes`

 The concrete choice stream supplied to the block's nondeterministic calls. 

### `blockChoicesEquiv`

 The admissible mathematical term families, reindexed in the native scan order. 

### `termAddresses`

 Four public address operands of the native term worker. 

### `termRun`

 The same fixed native program serves every block ordinal. 

### `term_stream_iff`

 A successful complete native stream selects precisely one actual refresh branch,
including when the block needs zero copies and its term takes no bits. 

### `term_pass`

 Each selected branch produces its grid IDs, repetition words and payload coordinates
through native calls. Every term field survives the complete pass. 
