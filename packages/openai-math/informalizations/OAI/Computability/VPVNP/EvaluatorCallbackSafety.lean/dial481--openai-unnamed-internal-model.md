---
{
  "module": "OAI/Computability/VPVNP/EvaluatorCallbackSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCallbackSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCallbackSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Storage specification of the coordinate-entry readers

The streamed determinant queries may take exponentially many ticks. Their
workspace bound records the peak height of each stack independently.


### `ReadsEntryWithin`

 Correct coordinate readback, with a peak bound on every stack throughout
the deterministic call. Row and column use the scheduler's path orientation. 

### `ReadsEntryWithin.readsEntry`

 The same exact run supplies the count computation's readback law. 
