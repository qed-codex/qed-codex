---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorTags.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorTags.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorTags.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning the small integer tags of a successor message

Status and record-kind words use the values zero through three. Scanning a
little-endian word, the control remembers its low two bits and tests whether
any higher bit is set. The same scan tests whether a padding or clamp word
is zero. It works on arbitrary lists, including empty and malformed words.


### `Tag`

 Successor word classes for unsigned values zero through three and values at least four. 

### `Tag.ofNat_large`

 The enumeration maps all values of at least four to its final constructor. 

### `State`

 States for remembering the low two bits and detecting set higher bits during a
little-endian tag scan. 

### `advance`

 The transition on one actual bit. 

### `finish`

 The tag when the source word has been exhausted. 

### `finish_fold`

 The width-independent scan classifies the full unsigned word. 

### `code`

 On the empty pop, return the classification in finite control. 

### `run`

 The designated stack is emptied in one pop per bit plus one empty pop. 
