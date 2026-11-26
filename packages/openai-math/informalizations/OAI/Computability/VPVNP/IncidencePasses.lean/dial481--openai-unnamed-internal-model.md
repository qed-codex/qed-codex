---
{
  "module": "OAI/Computability/VPVNP/IncidencePasses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidencePasses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidencePasses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Iterating the incidence matrix passes

Between two row checks the head scans to the blank at the right end of the
input. A final pass halts with acceptance precisely when every row check
succeeded. The running-time bound includes all scans across the padded prefix.


### `check_rows`

 If the leftward pass decides row `r`, successive passes decide their conjunction. 
