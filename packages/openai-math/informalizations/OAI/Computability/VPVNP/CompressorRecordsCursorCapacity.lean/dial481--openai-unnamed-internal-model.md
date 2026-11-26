---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorCapacity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorCapacity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorCapacity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word space for initializing the cursor records

At fixed degree, the number of rows is polynomial in the input length and
independent of where the physical address is split into base and lane blocks.
The same word accommodates the initial width, the six arrays and a timestamp
for every probe of the scan. A polynomially bounded starting offset can be
chosen before the eventual length threshold.


### `rowCount_eq_positions`

 Splitting the virtual address does not change the number of actual ports. 

### `bounded_positions`

 The number of actual cursor positions is polynomially bounded for fixed address exponent. 

### `eventual_word_room`

 A fixed polynomially bounded natural address fits strictly below the word modulus. 

### `eventually_cursorCapacity`

 All capacity conditions for the first descriptor scan. Seven words of
cost per row account for one call and its six probes. The threshold works
for every split of the virtual address at each sufficiently large length. 

### `scan_probeRecords_fitsWord`

 Every chronological RAM record of the native scan has a word-sized
address, timestamp and ordinal as soon as the scan's ending cost fits. 
