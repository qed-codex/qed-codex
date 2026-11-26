---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalRootGatherScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Execution of both terminal slot scans

The slot cursor counts empty slots as well as positive-width slots. It reads
the shared directory, copies exactly one external word per wire bit, and
preserves the private memory outside its destination interval.


### `Cost`

 Certifies the exact event count and external probe count of a gather trace, together with
preservation of external memory and an empty choice-bit trace. 

### `Cursor`

 Slot-loop invariant for the next field to gather. It records the private write cursor, the
unit increment, and the current, first and exclusive-end slot indices. 

### `Headers`

 Postcondition for the two straight-line directory-read blocks. 

### `HeadersReads`

 Directory-read postcondition including the addresses of the same execution. 

### `field_run_reads`

 A nonempty slot scan iteration, including its cursor comparison and increment.
The bit loop still performs an exit comparison when the selected width is zero. 

### `suffix`

 The remaining fields of one half of the argument packet. 

### `reset_run`

 The intermediate row returns the slot counter to the site's first slot,
leaving the destination cursor immediately after the outgoing payloads. 
