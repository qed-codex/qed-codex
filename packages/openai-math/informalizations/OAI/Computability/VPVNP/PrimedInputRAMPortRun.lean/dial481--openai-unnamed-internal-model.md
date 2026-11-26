---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMPortRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMPortRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMPortRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private register execution of the primed transcript port block

The triangular scan stops at the unique phase containing the exchange ordinal.
Every executed instruction produces a tick and leaves external memory untouched.


### `Ticks`

 The port block executes for exactly `k` private ticks, takes the given initial registers to
the specified final registers and preserves external memory. 

### `scan_exec`

 With `gap` rows still to remove, the loop uses exactly `3*gap+1`
instructions. It preserves every register outside its two counters. 

### `program_exec`

 The actual fixed register program reaches its normal exit with the
calculated raw address. Its event trace contains private ticks only. 

### `program_preserves`

 All registers below the return registers retain their entry values. 
