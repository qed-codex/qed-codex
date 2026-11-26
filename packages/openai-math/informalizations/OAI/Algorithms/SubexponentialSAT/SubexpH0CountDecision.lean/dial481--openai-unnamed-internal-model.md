---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpH0CountDecision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpH0CountDecision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpH0CountDecision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decode the single quartet returned by reconstruction at zero

The concrete CRT implementation returns H(0), so its output is one quartet.
No equality to a full reconstructed coefficient list is needed. The preceding
CRT trace must still establish the returned quartet's stated denotation.


### `firstWord_mod`

 The modulo word is derived from the selected reconstruction at zero.
The actual CRT producer supplies `computed`, not a count oracle. 

### `main_execution`

 Physical main-state execution on the singleton output. Other persistent
fields are framed; the cost is quadratic in the represented word width. 

### `primitive_execution`

 The standalone finite decoder also has a primitive-machine trace on the
single quartet; earlier reconstruction work is excluded from this bound. 
