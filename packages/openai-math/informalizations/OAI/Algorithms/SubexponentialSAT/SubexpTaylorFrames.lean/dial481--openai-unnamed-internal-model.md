---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTaylorFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTaylorFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTaylorFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-control conversion of a flat coefficient stream into an ordered
list of framed coefficients. Runtime counters determine the coefficient
width and requested count. Missing high coefficients are actually read as
zero by the existing padded-reader program. 

### `pad_round`

 The reader tests counter presence, so either bit value is a valid tick. 
