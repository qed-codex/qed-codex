---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsDemandOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandOutput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the genuine old-arc inputs of the slot compiler

Starting with the previous level's incidence and the selected layout's placement
columns, scan every directed old port once. The output occupies four consecutive
words per absolute old-arc ID. The CD flag and selected role cells then have exactly
the types and indexing read by the genuine-slot worker.


### `oldCount`

 Number of directed old slots visited in site-major order, counting every base vertex,
packing lane and outgoing port. 

### `absoluteCount`

 Size of the absolute old-arc directory, counting all base arc identifiers across the
residual lanes. 

### `absoluteIndex`

 The bijection that assigns each old arc its absolute directory index with the residual lane
as the least significant coordinate. 

### `regions`

 The old-site port order and absolute arc order are two bijections of the same
finite space. Consequently the four-word output rows are disjoint in memory. 

### `RoleColumns`

 The exact two data predicates consumed by the surviving-slot generator. 
