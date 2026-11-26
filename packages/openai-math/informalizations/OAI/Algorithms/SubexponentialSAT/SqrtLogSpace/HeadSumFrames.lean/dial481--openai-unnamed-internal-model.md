---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical frames for the native head rescan. Read-and-restore source words
are framed at command endpoints. The pair accumulator has the stronger static
property that no controller, overlay or dense-add instruction writes it. 

### `initial_frame`

 Initial cleanup, copying and the first fuel test restore every retained
word outside the actual workspace and three initialized arrays. 

### `advance_frame`

 The native cursor increment and fuel decrement change only their two
words and shared empty scratch; all semantic metadata survives this boundary. 

### `final_frame`

 The final physical reclamation restores every off-controller word. 

### `gate_frame`

 Full-key checks copy and temporarily consume their source words, then
restore all of them. This is an endpoint statement about the actual gate. 

### `overlay_frame`

 The concrete overlay restores all source masks, baseline and query words
outside its precisely named assignment/output scratch. 

### `overlay_pair_not_mem`

 No instruction in the actual overlay writes the pair accumulator. 

### `accumulate_pair_not_mem`

 Dense head addition and cache reset never write the pair accumulator.
The source and output arrays remain the actual854 and853. 

### `head_pair_not_mem`

 Static composition for the head controller. Its final concrete use supplies
the footprint of the named assignment program, rather than a semantic oracle. 

### `head_pair_prefix`

 The unchanged physical pair word transports any decoded meaning without
recomputing it, at every source prefix of the head command. 
