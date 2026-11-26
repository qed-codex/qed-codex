---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteTiming.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteTiming.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteTiming.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact tick counts for the native routing checker

The geometry and field-mode branches depend on the cursor position and
current system. Each field visits its full width. Adding the fixed loop
instructions therefore yields a trace length determined by the position
and dimensions, independently of the resident bits and scratch registers.


### `clock`

 The complete routing clock, including initialization, width switch and dispatch. 

### `hostFits`

 A host at least as wide as the fitted processor holds its dimension and
both native loop bounds. The processor's address envelope bounds the sorting block. 

### `succTicks`

 Successor calls, offset additions and counted-loop control. 

### `rowTicks`

 The step scan in one sorting phase, including its offset additions. 

### `phaseTicks`

 Sorting phases, with the instruction computing each step bound and the outer control. 

### `routeTicks`

 Exact tick count at the site, from the initial mask clear to the final branch. 
