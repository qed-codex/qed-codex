---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackEngineSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Bank conventions at deterministic Schur subroutine boundaries 

### `Ctl`

 Abstract control of the evaluator specialized to Schur keys and encoded scalars. 

### `Cfg`

 Abstract configuration of the Schur evaluator, including its stack of pending frames. 

### `live`

 Live register contents for an abstract control, encoding the query, scan count and
accumulator when needed. 

### `output`

 Encoded scalar on the result port of a returning control, and an empty result port during
evaluation. 

### `atControl`

 Assemble live registers, saved frames, condition bits, result and auxiliary stacks at a
control boundary. 

### `label`

 Physical engine entry state corresponding to an abstract enter, scan or return control. 

### `popped`

 Restored live-frame data after the engine has consumed the saved direction tag in field
zero. 

### `Contracts`

 Physical run contracts of the five arithmetic and routing subprograms.
The engine implements the two frame operations itself. A pending state carries
the computed child query in the dispatch output registers. 

### `InRange`

 The active scan count is at most `lim` and each suspended frame's remaining index is
strictly below `lim`. 

### `CursorRange`

 A suspended frame retains a legal child index of its own parent. This
ensures the physical child dispatcher only sees indices in its node's arity. 
