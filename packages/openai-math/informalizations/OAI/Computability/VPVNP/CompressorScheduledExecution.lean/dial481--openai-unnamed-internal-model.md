---
{
  "module": "OAI/Computability/VPVNP/CompressorScheduledExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScheduledExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScheduledExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Applying the descriptor induction to the paper's iterated compressor

The actual compression tree and its native table share their chronological
block and pass indices. Partial branches use the proved size bounds on
their current graph, and the completed path gives the native source log
and the retained mathematical levels at the same terminal memory.


### `LocatedRuns`

 The native per-pass constructor is needed only in its true block and
substep and only for graph sizes permitted by the initial allocation. 

### `nativeReaders`

 The term readers for the scheduled execution obtained by repeating the block readers across
all selected blocks. 

### `execute`

 Recursion on the actual chosen compression execution, beginning just
after its four deterministic cursor initialization rows. 
