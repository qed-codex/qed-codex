---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanTripleLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanTripleLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanTripleLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-control streaming contraction of arbitrary many scalar triples. 

### `tripleScan_eval_suffix`

 The streaming controller is fixed. Its input stream and unary count may
have any finite size. Every scalar multiplication/addition and each scan is
included in the bound. 
