---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwnerFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses touched by the endpoint-owner scans

The genuine scan reads from the old arc, selected role and subdivision
tables, then writes the genuine prefix of the owner stream. The dummy scan
reads the cyclic successor table and writes the trailing dummy fields. The
bounds apply to the emitted probes of every call in the two native segments.


### `interval`

 A half-open external array of the given length. 

### `oldWords`

 Size in words of the old arc record table, with three role sites and a CD flag per absolute
old arc. 

### `genuineRead`

 Addresses in the old arc, role, or subdivision tables that the genuine owner scan may read. 

### `dummyRead`

 The cyclic successor table range read by the dummy endpoint owner scan. 

### `genuineWrite`

 The leading scratch interval that receives owner words for genuine candidate fields. 

### `dummyWrite`

 The trailing owner interval, immediately after the genuine fields, that receives owner
words for dummy fields. 

### `genuine`

 For the exact native genuine run, every emitted read and write lies in its
declared physical array. Its eight role offsets remain bounded across the scan. 

### `dummy`

 Every dummy call reads its source site's cyclic successor, even when
the selected side is the outgoing end. Its write lies in the dummy suffix. 

### `of_tables`

 Read and write footprints of the first two reports of a selected shrinking
level. They follow from the actual stored table representation at the level's
initial memory and the five native segments supplied by the level run. 
