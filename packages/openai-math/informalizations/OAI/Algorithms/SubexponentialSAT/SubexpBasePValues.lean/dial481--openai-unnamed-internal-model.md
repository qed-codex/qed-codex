---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpBasePValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBasePValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBasePValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric specification of the actual fixed-width digit stream

The proved unranking program can preserve arbitrary leading zeroes in its
working rank. Its output digit words nevertheless depend only on the numeric
rank, since each digit has the fixed modulus width.


### `digit_eq_fixedBits`

 One actual remainder word is the canonical little-endian representation
of the numeric remainder at exactly the modulus width. 

### `digitWords_eq_numeric`

 The actual output words are fixed-width encodings of the numeric digit
list, with the least-significant base-p coordinate first. 

### `digitWords_congr`

 In particular, leading zeroes in the scalar-rank register do not change
any local field label or the emitted row semantics. 
