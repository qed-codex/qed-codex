---
{
  "module": "OAI/Computability/VPVNP/LiveStageLinkPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLinkPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLinkPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Consecutive calls and overhead of the linked program

The component interpreter reads the stage tag at each call boundary, runs its
own instruction table, and updates the shared memory from its report. It agrees
exactly with the linked finite instruction table on every path, including
malformed tags, unused branch bits, and calls after termination.


### `linkedReport`

 The full external trace, including the deterministic dispatcher and transfer. 

### `linkedReport_choiceBits`

 The linker never guesses an additional bit and never merges two paths with
identical computed states but different original branch choices. 

### `linkedReport_probes`

 Each call adds the tag read and at most one transfer write. 

### `linkedReport_length_le`

 At most `2d+5` extra instruction dispatches per call. The difference
in report lengths equals the difference in total dispatches, since both
computations use one final instruction after their logged events. 

### `linkedReport_after`

 The external memory transition is exactly that of the component, followed
by the one tag write when its accepting exit is connected to a further stage. 

### `stageCall`

 Replay a single call directly in its source component. Fuel remaining after
dispatch is charged for any transfer as well as the original component trace. 

### `execute_linked_of_stage`

 An ordinary successful component call can be used directly at any linked cap
with `2d+5` units of slack. Its exact branch string and computed report are retained. 

### `stageSegment`

 Path composition of the individual source stages, resetting private data
on every call and using the exact post-state and memory of its predecessor. 

### `runSegment_eq_stageSegment`

 The source-stage path composition and the native linked machine accept
precisely the same per-call branch strings and produce identical reports. 
