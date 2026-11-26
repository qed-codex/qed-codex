---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorFormat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorFormat.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorFormat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite control test for an eight-word successor field

The bit-stack machine retains the small tags of the eight words and a separate
unsigned cost comparison. These finite data decide exactly the canonical
encoding test, or the all-zero clamp at a missing edge.


### `Tags`

 One small integer tag for each of the eight words in a successor message. 

### `recordOK`

 Empty record padding is fixed in all five words. 

### `valid`

 The zero clamp is separate from a regular, present message. 

### `wordTags`

 Classify the unsigned value of each successor word by its small integer tag. 

### `valid_present_iff`

 A present field passes exactly when all eight saved words have the unique
canonical encoding. Acceptance at the cap is allowed and has state word zero. 

### `valid_present_bits`

 Equality with the word-level validator on every bit pattern. 
