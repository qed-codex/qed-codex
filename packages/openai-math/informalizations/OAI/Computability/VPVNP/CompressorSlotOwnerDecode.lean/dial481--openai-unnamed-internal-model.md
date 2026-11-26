---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwnerDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric decoding of shrinking endpoint owners

The old CD arc, role-edge type, subdivision and absolute lane are recovered
by quotient and remainder before any endpoint lookup. This identifies which
entries of the two rectangular owner tables are real and which are holes.


### `oldBaseArcCount`

 Cardinality of the old outgoing arc space with the remaining lane suppressed. 

### `oldArcIndex`

 Dense old arc index with the original absolute lane as the least significant digit. 

### `GenuineDigits`

 Mixed-radix coordinates of a genuine candidate arc, consisting of edge type, old base arc,
subdivision, and absolute lane. 

### `genuineDigits`

 In order, the role-edge type, old base arc number, subdivision and absolute lane. 

### `digitArc`

 Look up the original absolute old arc at the two decoded digits. 

### `isCD`

 CD validity test on an original directed arc, independent of subdivision and type. 

### `decodeArc_genuine`

 Quotient/remainder decoding of a genuine-region candidate, including the
two reasons for an unoccupied address. 

### `decodeArc_genuine_isSome`

 Exactly the proper subdivisions of CD arcs have genuine endpoint owners. 

### `decodeArc_genuine_end`

 Select the endpoint owner directly from the role-edge type and its old CD arc. 

### `dummySourceSite`

 Read the source site and the local dummy number from the address offset
past the genuine interval. The site number is the quotient by the padding
degree and the dummy number is the remainder. 

### `decodeArc_dummy_end`

 In the dummy interval, the selected endpoint keeps the lane and applies
the tag cycle exactly for an incoming field. 

### `dummyOffset`

 The local dummy address for any member of the trailing interval. 

### `endpoint_field_digits`

 The field's two least-significant operations split off its orientation bit. 

### `directory_genuine_destination`

 Numerical directory destination on the entire genuine-field interval.
Invalid addresses occupy distinct rows past all real endpoint owners. 

### `directory_dummy_destination`

 Numerical destination of a dummy field in the second scan. The dummy
source index is the local field divided by two and then by the padding degree. 
