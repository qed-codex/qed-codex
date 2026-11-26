---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramSerializationBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramSerializationBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramSerializationBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical length bounds for the six paid serialization operations. The
input length vector remains explicit; no arbitrary padding bound is assumed. 

### `guarded_lengths_le`

 Applies in particular at the frontend's actual canonical input-length
vector. The bound changes with that vector, rather than quantifying it away. 

### `uniform_guarded_lengths_polynomial`

 One fixed polynomial bounds every serialized port whenever the eight
actual source values and their chosen physical length caps are bounded. 
