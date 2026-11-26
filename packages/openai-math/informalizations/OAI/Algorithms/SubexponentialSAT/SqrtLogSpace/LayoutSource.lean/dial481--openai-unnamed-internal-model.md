---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/LayoutSource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/LayoutSource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/LayoutSource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete original-variable layouts with every produced integer row retained.
The rank basis is used only to count attained signatures. 

### `canonicalData`

 Universal rows are assembled on incidences and then summed along the
original owner fibers. No Boolean variable is introduced by this construction. 

### `data`

 The producer's raw matrix has one row per incidence, including zero and
repeated rows. Its constraints determine exactly the required foreign values. 
