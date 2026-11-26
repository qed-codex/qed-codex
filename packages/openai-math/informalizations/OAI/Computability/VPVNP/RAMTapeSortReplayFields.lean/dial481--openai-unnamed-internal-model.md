---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortReplayFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplayFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplayFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical exchange fields as streams of five-word sorting records 

### `recordBytes_fieldWords`

 Decoding one addressed record and writing its five words recovers its original bits,
including for malformed tags and noncanonical payloads. 

### `fieldWords_bits`

 Row-major concatenation of the addressed five-word records exactly recovers the
incident send or receive field selected by this cross-site stride. 

### `fieldPair_eq_blocks`

 The two consecutive streams in the physical schedule carry exactly the rows
of the outgoing and incoming blocks for this stage. 
