---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSVisit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSVisit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSVisit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One complete native DFS visit. The leaf callback below is an intermediate
implementation contract for a fixed finite command, not a final theorem premise.
The actual streamed leaf program must instantiate it at integration.


### `LeafContract`

 The bound is uniform over all actual leaf inputs; time is separate. 

### `body_refinement`

 All branch construction, failed selector scans, accumulation and cleanup
are part of the same actual body evaluation. No elapsed traversal time enters
its source-space bound. 
