---
{
  "module": "OAI/Computability/VPVNP/LiveConfigGatherImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveConfigGatherImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveConfigGatherImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory image of gathered configuration words

A contiguous cut holds one zero-or-one word per bit. Each scheduled gather
call reconstructs one little-endian field word in a disjoint bank. Replaying
the reports installs the checked decoder's entire array of words.


### `ArrayBitImage`

 Every cut bit occupies one full machine word. 

### `bitImage_word`

 Restricting a complete cut to a single word gives the exact input image
expected by the native gathering call. 

### `ArrayBitImage.after_write`

 A write to the disjoint destination bank leaves the complete source bit
image available to every later cursor. 

### `replay_reports`

 The ordered destination writes from the actual native reports. 

### `gathered`

 Packed words after all destinations have been visited. 

### `configAt_iff_words`

 The memory image characterizes every field of the checked decoder,
including every padding cell of a halt. 

### `gathered_configAt_iff`

 For arbitrary cut bits, the packed memory is the image of a configuration
exactly when the checked binary decoder returns that configuration. 

### `gathered_decode_none_iff`

 A malformed cut cannot realize any canonical configuration in the destination bank. 
