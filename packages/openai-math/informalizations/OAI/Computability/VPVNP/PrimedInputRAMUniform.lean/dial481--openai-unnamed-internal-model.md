---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMUniform.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMUniform.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMUniform.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A single burst-RAM program for both primed input passes

The first half of the public cursor range enumerates the designated scratch writes.
The second half enumerates all output writes, using the memory left by the first
half. The final halt contributes one extra unit to the calls-plus-probes bound.


### `TwoPass`

 Public data for the two passes, indexed by the rectangular tape positions. 

### `TwoPass.own`

 Indicate which rectangular positions choose a shared bit in the first pass. 

### `TwoPass.scratch`

 Distinct scratch address for each rectangular position, used for the first-pass choice
  writes. 

### `TwoPass.dest`

 Distinct output address for each rectangular position assembled in the second pass. 

### `TwoPass.source`

 Literal word or memory address supplying the second-pass copy at each position. 

### `ops`

 The cursor visits both full arrays in order. 

### `assignmentEquiv`

 Owners are exactly the original designated cells, at their first-pass cursors. 

### `reports_split`

 Native data-call reports coincide with the first-pass and second-pass reports,
including all fetched values after the scratch writes. 

### `completeReports`

 Full report list, including the explicit halt after the copies. 

### `after_completeReports`

 Replaying the genuine RAM events produces the original two-pass memory. 

### `completeReports_cost_le`

 One call and at most one write at each first-pass position, one call and at most
two probes per copy, and one final halt. 

### `scheduledMemory_eq`

 Memory at the terminal cursor, before the explicit halt. This is the memory
available for a subsequent computation on the assembled tapes. 

### `flatten_assignmentCalls`

 Flattening the per-call histories recovers the original first-pass choice
stream in the order of the designated cells. 

### `run_completeReports`

 A completed two-pass run on a branch assignment computes exactly its reports. 

### `scheduledCost_le`

 The cap depends only on the number of cells, uniformly over bit assignments,
memory contents, and the number of fetches among the second-pass cells. 

### `actualPathEquiv`

 Bounded accepting paths of the single program enumerate precisely the original
designated-cell assignments, also when two branches encode the same memory word. 

### `run_actualPath`

 For the assignment recovered from any accepted native path, the computed report
list is the canonical one with its observed choices and memory reads. 
