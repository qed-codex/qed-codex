---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQuerySpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQuerySpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQuerySpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Separate the retained caller envelope from each physical local input cap.
The local transient bound is never recycled as the next iteration's input. 

### `overlay_command_space`

 Caller words are charged once. The only local size cap is on actual
head/mask/baseline and the two preserved local context words. 

### `overlay_trace_space`

 Repeated candidate calls retain one polynomial envelope on every source
prefix, including paid cleanup of arbitrary old work words. 
