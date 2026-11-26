---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramClip.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramClip.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramClip.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed primitive clipping for sparse keys. The key and both unary limits
are disposable inputs; all four local stacks are empty on return. Callers may
keep master copies outside these ports. 

### `clipIndex_trace`

 Actual machine clipping is exactly the semantic `Index.Kept` predicate. 
