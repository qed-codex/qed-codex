---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderFieldState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory invariants for the sixteen incident-field stages

Each incident field has a descriptor stage and a consumer stage. All six
nonpadding payloads occupy disjoint public ranges. An unoccupied part of
an array retains its original scratch value, including the initial zero
exponent vector at the first group.


### `key`

 Enumerate the four incident fields on the left and then the four on the right in extraction
order. 

### `descId`

 The stage number of the descriptor computation for the given incident-field ordinal. 

### `scanId`

 The stage number of the bounded field scan immediately following its descriptor
computation. 

### `startId`

 The descriptor stage that begins the indicated remaining field, or no stage once all eight
fields have run. 

### `interval`

 The source offset and length of one incident field for the group's actual width, phase, and
mode. 

### `Sources`

 Scalar and packed source words surviving from the earlier header stages. 

### `Protected`

 Addresses read by later stages may contain any value at entry. All words
except the handoff tag, the descriptors, and the actually occupied payloads
must retain that value through the field suffix. 

### `Image`

 All nonpadding fields with index below the cursor have been copied. The
frame retains zero in each unused part of a payload array. 

### `ValidPadding`

 Physical zero padding selected by the actual descriptor shape. 

### `FieldEffect`

 Writing a descriptor and consuming that one field cannot change any
other payload. Only the tag and descriptor words change on handoff. 
