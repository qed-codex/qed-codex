---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ReconstructionReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ReconstructionReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ReconstructionReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual CRT, canonical whole-word reader and paid cleanup never inspect
or modify the marked-record cursor320 or accumulated mass322. This syntactic
certificate supports exact-time replay while the caller still charges their
retained words in every prefix-space bound. 

### `reader_avoids`

 Only the explicit eight scalar-reader ports can be touched. 

### `move_avoids`

 Both physical transfers avoid the two persistent collector words. 

### `crt_avoids`

 The CRT's entire320-stack bank lies below the collector frame. 

### `lifted_avoids`

 Every actual identity-on-indices embedding, including768 into896, keeps
this no-read/no-write certificate. No execution service is assumed. 
