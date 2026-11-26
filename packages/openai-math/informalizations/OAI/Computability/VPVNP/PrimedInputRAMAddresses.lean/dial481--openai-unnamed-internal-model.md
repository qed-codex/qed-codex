---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMAddresses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMAddresses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMAddresses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the scratch read from a raw incident bit position

The pair counter in Section 11 enumerates input bits by position. A local
offset in the sorting region determines an exchange number and a direction.
At most `d` triangular-prefix comparisons recover the site's XOR mask.


### `layerBitLoop`

 Look for the phase containing the given exchange ordinal. Each iteration
evaluates a triangular prefix and compares it with the ordinal. In the
identified phase two subtractions give the XOR bit. 

### `rawSource`

 Compute a source row and offset from the public site and local position.
The work counter charges arithmetic and comparisons. The final read, when
there is one, is a separate single external probe. 

### `rawSource_offset`

 At every actual incident port the linear-address algorithm gives the
same source as the typed endpoint calculation, including both end clamps. 

### `rawSource_at`

 Correctness for an enumerated linear input position, without an input
slot supplied by the caller. 

### `rawSource_eq_self_iff`

 The enumerator makes a binary choice precisely when this source lookup
returns the input position itself. 

### `rawSource_work`

 A raw offset lookup uses at most a linear number of word operations in
the site-address width, irrespective of any scratch or message value. 
