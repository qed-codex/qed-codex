---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteRange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteRange.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteRange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concatenated fixed-width field ranges in the cursor checker

Successor fields have one common width, as do the steps of any sorting
phase. At the return from each field the scheduler advances the running
offset. The final mask expresses the conjunction of all tests in the range.


### `Frame`

 Registers retained by the range, and its unmodified memories. 

### `Field`

 One field's returned mask and untouched registers, before advancing
the offset and loop index. 

### `Partial`

 Prefix of the range, after the first i fields have been visited. 

### `run_exact`

 A range visit executes the proven native field call at each index and
counts the actual offset addition and counted-loop instructions. 
