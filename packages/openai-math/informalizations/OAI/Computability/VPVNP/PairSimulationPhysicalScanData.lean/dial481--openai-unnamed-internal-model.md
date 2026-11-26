---
{
  "module": "OAI/Computability/VPVNP/PairSimulationPhysicalScanData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPhysicalScanData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPhysicalScanData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Wire assignments of the terminal scan in a nomination trace

The earlier data scan makes one singleton choice per wire bit in descending
address order. The terminal worker appends one empty closing call and writes
those same bits to the selected physical bank. The construction includes
empty banks and zero-width edges.


### `assignment`

 Enumerate each successful data scan by its complete assignment in the state's address order. 

### `payload`

 Grouping the flat assignment by outgoing arc gives the payload used by
the nomination's vertex witnesses. 

### `index`

 Physical ordinal of a bit within one edge's payload. 

### `physical`

 Transport nomination data directly to a completed shared-bit record of
the terminal program, allowing independent word sizes and base addresses. 

### `physical_payload`

 Physical readback from the chosen phase yields the bit of the actual
payload supplied to both incident vertex witnesses. 
