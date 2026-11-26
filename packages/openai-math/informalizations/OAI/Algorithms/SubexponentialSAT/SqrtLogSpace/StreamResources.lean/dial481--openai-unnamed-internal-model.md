---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/StreamResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/StreamResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/StreamResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform storage rules for concrete streaming loops. A local runtime bound
is used only for one invocation whose entire initial storage is uniformly
bounded; neither bound depends on the number of loop iterations. 

### `halted_trace_steps_eq`

 Deterministic successful traces to halted states have the same length. 

### `eval_steps_eq`

 Structured evaluation has its actual measured length, independent of the
derivation used to establish its concrete execution. 

### `dataBits_le_mul`

 Summing the port bounds counts every simultaneously live buffer. 

### `relocate_trace_stack_frame`

 Every unassigned stack retains its caller contents at every actual prefix,
including prefixes within a relocated subroutine. 

### `relocate_trace_stack_bound`

 Only unassigned caller ports need a frame bound, since assigned ports are
overwritten by the embedded source state. The instruction table and actual
source trace remain explicit. 

### `loop_local_stack_bound`

 A locally bounded body may be repeated arbitrarily often. Its entry bound
includes every persistent caller stack, and its concrete runtime controls only
the temporary growth within that invocation. 
