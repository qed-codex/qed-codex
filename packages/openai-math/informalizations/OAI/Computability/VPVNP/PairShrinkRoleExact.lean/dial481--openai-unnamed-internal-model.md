---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Joining the child, hidden and resident-map stages of a shrinking visit

A directory load before each stage prepares its input registers. The native
reads pass the exact remaining tape through these loads and through the
deterministic resident maps. The join accounts for every private-memory write
and preserves the pending DFS stack on successful returns.


### `visitReader`

 Trace, scratch and stream decoder for the actual three scans. The
directory loads receive the values chosen by all preceding stages. 

### `native_exactOn`

 Exactness of a shrinking visit in the DFS machine. The operand loads
supply the required register values before each native reader; the resident
entry callbacks check the selected matrix occurrences on the prepared scratch. 
