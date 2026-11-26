---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A common clock for the fixed online descriptor program

A finite maximum covers the deterministic workers at every scheduled degree.
The motif workers add their bounds at the actual input length. A larger
outer machine clock gives the same controller, launcher, and source budgets.


### `refreshHeaders`

 Fuel bound for the header publishers of the degree-refresh pass. 

### `fixedFuel`

 Length-independent fuel allowance covering the deterministic workers, including surviving
slices, refresh headers and shrinking bundle scans. 

### `fixedClock`

 Length-independent controller allowance for startup, shrinking headers, greedy scans and
online dispatch. 

### `workerFuel`

 Worker fuel at input length `n`, including shrinking prefix preparation and term selection
at the chosen word width. 

### `small`

 Common online clock obtained by adding the fixed controller allowance to the scan budget at
the current worker fuel. 

### `rate`

 The length dependence is at most quartic in the binary logarithm. 

### `eventually_room`

 A single threshold covers the tag word, the smaller clock, and any fixed
number of further link instructions. 
