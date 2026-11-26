---
{
  "module": "OAI/Computability/VPVNP/IncidenceScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One pass of the incidence-matrix machine

A row scan reads the tagged column records from right to left and finishes on the zero
end marker. Exactly one selected incidence advances the search to the next row.


### `rowBits`

 A zero after the column tags terminates each scan. 

### `rowHits`

 Count the selected columns incident with the specified row. 

### `runRow`

 One row consumes one transition per serialized bit, including the terminating zero. 
