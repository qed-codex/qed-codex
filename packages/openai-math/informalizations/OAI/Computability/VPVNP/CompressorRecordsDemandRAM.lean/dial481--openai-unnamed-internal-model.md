---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsDemandRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Materializing the selected roles of each old shrinking arc

The scan cursor uses the old physical outgoing-port order. The output record address
uses the old arc's absolute ID in the surviving-slot directory, which moves the tag
and port ahead of the mask and keeps the residual lane least significant. Read both
thickness bits, follow the thin C endpoint for A and B, and read the opposite
endpoint's chosen owner for D. All arcs have a CD indicator, including thick–thick
arcs that occupy unused addresses of the genuine slot range.


### `Ops`

 Straight-line instruction lists for the demand worker, which uses 24 registers and 11
public operands. 

### `visit`

 Degree, residual/tag/mask radices, an unused offset, the actual outgoing,
thickness, owner, assigned and target columns, and the absolute arc-record base. 

### `address`

 Address of an old arc's four-word demand record, obtained by permuting the scan index into
absolute arc order and adding the output table base. 

### `endpoints`

 Order the physical source and target according to the source's thickness bit, putting the C
endpoint first on a CD arc. 

### `Roles`

 The demand record of an old arc, storing its packed A, B and D site numbers and the CD
indicator. 

### `Roles.A`

 Packed source site of the bundle assigned to the thin C endpoint on a CD arc. 

### `Roles.B`

 Packed target site of the bundle assigned to the thin C endpoint on a CD arc. 

### `Roles.D`

 Packed site selected by the placement for the opposite, D endpoint on a CD arc. 

### `Roles.cd`

 The CD indicator, set to one unless both endpoints of the old arc are thick. 

### `roles`

 Read the placement data at the two endpoints to compute A, B and D, and use their thickness
bits to compute the CD flag. 

### `events`

 Trace of one demand visit, reading the old target, endpoint thicknesses and selected
placement data before writing the four demand fields. 

### `store`

 Write the computed A, B, D and CD words to the four consecutive cells of the old arc's
demand record. 
