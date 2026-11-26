---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortDecision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortDecision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortDecision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Order and canonicality decisions from the five scanned word fields 

### `Observation`

 Information retained about one field after scanning both words, including each decoded tag
category and their unsigned comparison. 

### `Observation.left`

 Tag category assigned to the left word, distinguishing zero, one, two, three and larger
  values. 

### `Observation.right`

 Tag category assigned to the right word using the same finite decoder. 

### `Observation.ord`

 Unsigned ordering of the two field words after the scan completes. 

### `RecordInfo`

 One comparison observation for each of the five fields of the paired records. 

### `observe`

 Finish both tag decoders and retain the word ordering from the completed field scan. 

### `expected`

 The five field observations computed directly from two raw records' natural word values. 

### `used`

 Recognize the three occupied record tags, one through three. 

### `chooseOrder`

 Return the left-first verdict for an unequal comparison and use the supplied secondary
verdict to break equality. 

### `leDecision`

 The initialized-address flag is between the address and the timestamp.
The value is consulted only after equal timestamp and kind. 

### `leDecision_eq`

 On an arbitrary five-word tuple the scan compares the parsed slots,
including the parser's empty value for unknown tags. 

### `canonical`

 An occupied tag may carry data fields, while an empty record must have all five fields
zero. 

### `equalDecision`

 Check equality of all five fields of the compared records. 
