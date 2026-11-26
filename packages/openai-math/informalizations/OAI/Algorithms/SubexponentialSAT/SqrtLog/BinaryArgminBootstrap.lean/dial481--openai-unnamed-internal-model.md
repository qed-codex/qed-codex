---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminBootstrap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminBootstrap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminBootstrap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Bootstrap the binary argmin from an empty incumbent. The initial candidate
load is paid explicitly, including the empty-input case. 

### `FirstLoadSpec`

 Extra callback obligation for the first load, where the incumbent is empty
and need not have the fixed score width. It requires actual traces as usual. 
