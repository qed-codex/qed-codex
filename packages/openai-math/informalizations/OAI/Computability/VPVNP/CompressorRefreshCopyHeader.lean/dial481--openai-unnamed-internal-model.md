---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshCopyHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshCopyHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshCopyHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Planner operands of the six native refresh column copies

The input header supplies the old vertex count, residual lanes and scratch origin.
The output header supplies each canonical destination pointer. The first three scans
copy one word per promoted base port and the last three copy one word per actual slot.


### `eval`

 Stop and parameter words at the actual copy visit. The count equalities identify
its two scan lengths with those of the refreshed state. 

### `reads`

 Support in a general preserved memory region follows from the old header cells,
the new pointer cells, and the single pitch read. 

### `operands`

 The six installed scans use the native parameters and only read cells permitted
by the physical calendar. The old and new publications are read at this visit's memory. 
