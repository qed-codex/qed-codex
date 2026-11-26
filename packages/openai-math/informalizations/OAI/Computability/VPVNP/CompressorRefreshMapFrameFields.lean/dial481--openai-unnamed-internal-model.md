---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshMapFrameFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapFrameFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapFrameFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native operand bases and lengths of the refresh motif

The same field descriptor table serves all promoted ports. Old demand endpoints read
their designated old slot, while new endpoints read the appropriate slice of the packed
external word. Supply endpoints read their designated expander slot. Lengths select the
payload part of the incident fields using the port computed from the current site.


### `FieldId`

 A source or target endpoint field of a demand tie or a directed expander supply incidence. 

### `base`

 Local base pointer of a map-row field. The table uses the fixed reverse incidence
of a supply and the stored segment offset at either end of an external demand. 

### `present`

 A present endpoint gives one and an absent endpoint gives zero. 

### `endpoint`

 The port at which the indexed demand or supply endpoint is incident. 

### `storedWidth`

 Recover the stored demand width or chosen supply payload for a fixed motif role.
The grid and repetition headers precede the payload vector. 

### `length`

 Only the endpoint incident to the runtime port contributes a readable slice. 

### `base_eval`

 Every operand expression evaluates to the independent slot or packed-segment base
used by the resident map call, including its unselected fields. 

### `nominal`

 The demand width or supply payload width of a field before restriction to the runtime port. 

### `storedWidth_eval`

 The live reads of the dense demand and strided term columns recover the selected
integer lengths in the fixed coordinate ordering. 

### `length_eval`

 A field at the wrong local port has length zero. At its correct port the stored
demand or payload gives the length of the exact resident buffer of the refresh call. 
