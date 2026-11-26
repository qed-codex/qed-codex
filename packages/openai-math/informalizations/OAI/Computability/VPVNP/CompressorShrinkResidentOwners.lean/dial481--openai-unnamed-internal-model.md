---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkResidentOwners.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentOwners.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentOwners.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native generation of the shrinking resident owner columns

A history cursor combines its motif number with either a party ordinal or an
absorbed edge type. The worker uses the sorted absolute-CD column and the
selected layout's A/B/D role words to write the owner at that cursor. It needs
two memory reads and one write.


### `arity`

 The six map parties or four absorbed edge types stored per motif. 

### `roleOps`

 Registers 11, 12 and 13 carry the three bits of the within-motif tag.
Register 8 carries the layout, register 9 is two, and register 14 is the
resulting role offset. 

### `code`

 Native owner-scan instructions for a hidden field or party map. Decode the occurrence, read
its absolute CD identifier and role word, and write the packed owner. 

### `worker`

 Register the resident owner scan as a scheduler pass that returns its advanced occurrence
cursor. 

### `visit`

 Schedule the owner scan from zero to the occurrence count with pointers to absolute CD
identifiers, role records and the owner output, plus the selected layout. 

### `offset`

 Compute the role-word offset within a four-word old-arc record from the selected layout and
the local field or party-map tag. 

### `offset_party`

 Bit decoding agrees with the party-role table in both layouts. 

### `offset_hidden`

 Bit decoding agrees with the owner of each absorbed edge type. 

### `absoluteAddr`

 Address of the occurrence's absolute CD identifier, using the quotient of its cursor by the
number of occurrences per motif. 

### `roleAddr`

 Address of the packed-owner word in the old arc's four-word role record, using the stored
CD identifier and the occurrence's selected role. 

### `report`

 Trace of one owner visit, reading the motif identifier and selected role word, writing that
owner at the occurrence cursor, and returning the next cursor. 
