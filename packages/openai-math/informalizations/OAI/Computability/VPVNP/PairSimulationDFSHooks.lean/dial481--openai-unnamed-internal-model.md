---
{
  "module": "OAI/Computability/VPVNP/PairSimulationDFSHooks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDFSHooks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDFSHooks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking final-vertex work to the native traversal

A local vertex routine may consume private choices and update its scratch
arrays, including the histogram above the stack. The dispatcher pops its
descriptor address and gives it control. Its return resumes the stored child
scan. This composition accounts separately for the routine's actual trace
and the traversal's reads, with the same unused stream suffix throughout.


### `Scratch`

 The portion of private memory at word addresses greater than or equal to the exclusive
stack end. Local visit routines use these cells for arguments and accumulated histogram
entries. 

### `scratch`

 Restrict a machine's private memory to addresses at or above the stack end, giving the
scratch state passed to a local visit. 

### `VisitPath`

 One specified path through the site routine. Distinct items can have
the same address and update the same exponent, with their separate traces. 

### `VisitPath.node`

 Descriptor address this visit expects in the dispatcher's node register after the stack
  pop. 

### `VisitPath.trace`

 Chronological RAM events of this local visit. They determine its consumed choice bits,
  instruction count and external probes in the combined traversal. 

### `VisitPath.enabled`

 Precondition on the incoming scratch contents for this particular visit path. Successive
  visits test it after applying the preceding paths' updates. 

### `VisitPath.update`

 Scratch contents produced on successful return from the local routine. The next visit
  reads its prepared arguments and accumulated counts from this state. 

### `Ready`

 The local arguments prepared by one occurrence must enable the next
occurrence. This allows malformed field assignments to reject. 

### `VisitPath.Linked`

 The exact execution contract of an embedded vertex routine. Pending
stack cells are preserved until the dispatcher prepends its child list. 

### `execute_linked_visits_supported`

 For a fixed chosen native path at each visit, control overhead adds no
choice bits and each state update acts on the previous routine's scratch.
The theorem includes the exact length and probe count on the combined path. 

### `execute_linked_visits_framed`

 The framed traversal, forgetting the support of its event list. 

### `execute_linked_visits`

 The original traversal statement, with the scratch, event, and cost
projections used by callers that do not inspect the ending stack register. 
