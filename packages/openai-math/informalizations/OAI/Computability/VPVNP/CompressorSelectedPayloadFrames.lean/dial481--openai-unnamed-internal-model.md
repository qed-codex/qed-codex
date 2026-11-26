---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedPayloadFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedPayloadFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedPayloadFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frames of the native groups used by the selected payload history

The old incidence bank remains readable during scalar publication,
scratch-array scans, and the final term/data header writes. Consecutive
group frames compose in the actual intermediate memory.


### `InputFrame`

 The two regions shared with all previously emitted parser data. 

### `InputFrame.below_array`

 Readback below the scratch allocation, as supplied by the shrink slot
group and its successor copies, suffices for both history regions. 

### `InputFrame.of_writes`

 Workers can also publish scalar fields of their own input level.
The pointer words and old incidence still agree in the two images. 

### `InputFrame.of_array`

 A scratch worker can write any word starting at the input's array base.
Its scheduler may also update the low control area. 

### `InputFrame.metadata`

 The old metadata packet and the two successor scalar writes preserve
the input pointer bank and canonical incidence, as well as earlier levels. 

### `InputFrame.refreshCopies`

 The six copies install the output graph after the current level, so the
input pointer bank and all previous levels retain their actual words. 

### `InputFrame.refreshPlacement`

 The refresh's singleton placement scan writes only its packed table. 
