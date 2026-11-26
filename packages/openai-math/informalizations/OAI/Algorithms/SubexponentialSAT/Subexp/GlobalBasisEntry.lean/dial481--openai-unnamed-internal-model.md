---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisEntry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisEntry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisEntry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual global-matrix entry callback. Descriptor bytes are parsed and
compared at runtime. Matching local entries invoke the persistent scalar-cell
reader; the other branches copy the canonical zero or one frame. 

### `command_eval`

 The input table, canonical zero/one frames, and descriptor are actual
stored bytes. Bounds are needed only when the local descriptor matches. 
