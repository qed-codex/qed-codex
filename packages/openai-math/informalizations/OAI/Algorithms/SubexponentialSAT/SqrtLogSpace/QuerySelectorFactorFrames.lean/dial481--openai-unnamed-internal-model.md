---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QuerySelectorFactorFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QuerySelectorFactorFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QuerySelectorFactorFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Every concrete source, factor, head, and preparation access avoids the
retained selector bank768..831. The certificates concern reads as well as
writes and therefore permit replay with unchanged steps and arbitrary selector
contents. All lower768 calls and relocated source calls are checked by their
actual physical stack maps. 

### `head_avoids`

 Every head-controller access is accounted for, including losing gates,
all binary counter tests and decrements, and final reclamation. 

### `accepted_avoids`

 The accepted path is instantiated with the actual source-table assignment
and dense addition/reset programs, with no callback footprint premise. 
