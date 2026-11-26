---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorLocalScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLocalScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLocalScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete private execution through the next external action

The bounded scan executes the instruction table repeatedly. It retains the
exact local event prefix needed to identify the corresponding native report.
Only an actual read, write, finish or rejection returns control to the caller.


### `Yield`

 Result at the boundary of a private instruction scan, including its callback,
configuration, remaining fuel and choices, and chronological event prefix. 

### `Yield.exit`

 Callback reached by the scan. The scan also returns the rejecting callback when it
  exhausts fuel or a required choice bit. 

### `Yield.cfg`

 Private program counter, registers, persistent state and write log at the scan boundary,
  before the caller handles the callback. 

### `Yield.fuel`

 Instruction fuel left after the scan. Fetching the instruction that requests an external
  action consumes one unit. 

### `Yield.bits`

 Unused suffix of the binary choice stream after the private branches in this segment. 

### `Yield.prefixEvents`

 Ticks and chosen branch bits from the private instructions preceding the callback, in
  execution order. 

### `Yield.prepend`

 Add an earlier instruction event to the front of a scan's chronological prefix. 

### `scan`

 Run private instructions up to the next read, write, return, accept or reject callback.
Follow jumps and consume branch bits while recording their events, and reject on exhausted
fuel or choices. 

### `scan_run`

 The physical controller reaches the declared exit with the exact bank
and suffix, including when fuel or choices run out. 
