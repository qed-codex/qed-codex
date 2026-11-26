---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionRuntime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionRuntime.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionRuntime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Numerical closure lemmas for the actual cutoff and identifier wrappers.
These assign no running time to an unimplemented operation. 

### `ceil_runtimeBound_le`

 Rounding is used only for a proof-side time bound, never to supply code. 

### `cutoff_source_bound`

 Exactly the source time paid by ExecutionCompletion, including the real
small-input scanner and a rounded bound on the large-input controller. 
