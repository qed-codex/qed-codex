---
{
  "module": "OAI/Computability/VPVNP/CompressorExecutionTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorExecutionTrace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorExecutionTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Complete descriptor paths indexed by the mathematical compression tree

An internal node has the native cut for its single compression pass. Its
children begin in the memory and control state returned for the selected term.
At a leaf the last deterministic native segment halts. Recursion gives an
exact bijection with complete accepting streams of the one fixed table,
retaining its actual reports, final memory and optional resource predicate.


### `ExecutionTrace`

 One local pass on the native machine and recursive executions on its
actual outputs. The only terminal case is a forced native halting segment. 

### `cut`

 The native prefix is the concatenation of the chosen passes and the
terminating segment on that very branch. 

### `acceptedEquiv`

 Complete accepted paths with a report predicate are exactly the terms
whose actual descriptor execution meets that predicate. 

### `allEquiv`

 Every mathematical branch meets the allotted resource predicate. 
