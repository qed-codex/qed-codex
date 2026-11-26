---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Well-founded assembly of the actual fixed DFS while command.
The body obligation is the concrete visit theorem; no finite successful run,
termination oracle, derivation tree or precomputed visit list is assumed.


### `execute`

 This intermediate invariant is instantiated by the concrete prepared frame
and the proved per-visit resource envelope, before the final endpoint. 

### `execute_sharp`

 The exact completed count and sharp node budget refer to the same
measured while execution, whose uniform prefix bound is independent of visits. 
