---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshPrepareAllocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshPrepareAllocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshPrepareAllocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing a refresh in its packed allocation

The six old incidence columns end before the seven new scratch columns. The gather reads
a permutation of the old actual slots and the directory reads the two old base columns.
The demand table and every strided term record begin after the last scratch column.


### `gather_index_lt`

 Transposing port and residual lane in the gather index stays inside the old
site-major width table, including when the dimensions are powers of two of size one. 

### `PrepareLayout`

 The exact inputs for `prepare_demands` and the term reader. The term row intervals
are disjoint from all segment descriptors, so their native writes preserve the endpoints. 

### `prepare_layout`

 Packed prepass allocation. The six scalar end bounds on the old columns and one
total allocation bound replace all the per-cell separation conditions of the native scans. 
