---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCRTAtZero.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTAtZero.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTAtZero.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Direct evaluation of the explicit Hermite reconstruction at zero. The
algorithm needs only local corrections and scalar Horner evaluations; no
global shifted polynomial or final polynomial division is required. 

### `weightedStep`

 One concrete quartic multiply-add in the outer reconstruction loop. 

### `weightedFold`

 The accumulator used by the outer machine, with each factor and its
local Horner output supplied once. 

### `selectedValue`

 The selected-ring calculation as scalar evaluations of the local CRT
corrections. This is the same ring value as the existing full reconstruction. 
