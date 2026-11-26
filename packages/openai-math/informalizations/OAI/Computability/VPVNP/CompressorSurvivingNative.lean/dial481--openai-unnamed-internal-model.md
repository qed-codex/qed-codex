---
{
  "module": "OAI/Computability/VPVNP/CompressorSurvivingNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed native surviving-slice visit for one subdivision

Each of the four role passes has a constant public bank. Its ordinal gives
the dense motif number and subdivision index. Four reads obtain the absolute
arc number, the common layout, the repetition word and the selected payload.
The call writes the balanced width and both endpoint directories directly.


### `Public`

 The eleven public operand words shared by the visits for a surviving role. 

### `params`

 The fixed role and subdivision count accompany the level's array heads. 

### `Data`

 All dynamic fields of a single call, in machine-word arithmetic. 

### `Data.rank`

 Zero-based index of the subdivision visited within the motif and role. 

### `Data.count`

 Number of subdivisions into which the role's width is split. 

### `Data.width`

 Full role width obtained by adding the selected payload to the repetition contribution. 

### `Data.total`

 Address of the total-width cell at the start of the motif and role's interval record. 

### `Data.dst`

 Base of the output width row for this absolute arc and role. 

### `read`

 Decode the motif and subdivision from the cursor and read the arc ID, layout, repetition
count, and payload to form the visit's data. 

### `readAddresses`

 Absolute ID, common layout, repetition word and selected payload word,
in the order in which the instruction table reads them. 

### `Data.piece`

 Width assigned to this subdivision, including one extra unit for the first subdivisions
that share the remainder. 

### `Data.offset`

 Starting offset of this subdivision in the balanced split of the role's width. 

### `Data.live`

 Number of positive-width subdivisions in the balanced split. 

### `Data.addresses`

 The thirteen destination cells for the total, piece width, interval metadata, copy frame,
and endpoint references. 

### `Data.values`

 The thirteen field values to store, ordered to match the visit's destination addresses. 

### `Lines`

 A list of register assignments for the worker with 64 private registers and eleven public
operands. 

### `lines`

 Assignments that read the term, compute the balanced piece, and form the addresses of its
output fields. 

### `destinations`

 Registers containing the destination addresses of the thirteen scatter writes. 

### `sources`

 Registers containing the values for the thirteen scatter writes. 

### `writes`

 Ordered address-register and value-register pairs consumed by the scatter worker. 

### `ops`

 Native instruction sequence that evaluates the assignments and performs all thirteen
writes. 

### `pass`

 Schedulable surviving-piece worker returning the next subdivision cursor from register 44. 

### `report`

 Event report and return word for a surviving-piece call at the supplied cursor and memory. 

### `stores`

 Ordered address and value pairs describing the surviving-piece call's effect on memory. 

### `Heads`

 Planner heads for four passes, with one runtime ordinal per live piece. 

### `Heads.motifs`

 Recipe expression for the number of dense motifs scanned at this level. 

### `Heads.terms`

 Recipe expression for the base address of the selected motif records. 

### `Heads.termStride`

 Recipe expression for the spacing in words between successive selected motif records. 

### `Heads.absolute`

 Recipe expression for the base of the table mapping dense motif numbers to absolute arc
  IDs. 

### `Heads.layout`

 Recipe expression for the address of the common layout word used to select payload
  columns. 

### `Heads.selectors`

 Recipe expression for the selector width contributed by each repetition. 

### `Heads.widthBase`

 Recipe expression for the base of the output width rows indexed by absolute arc and role. 

### `Heads.intervalBase`

 Recipe expression for the start of the interval records indexed by dense motif and role. 

### `visits`

 Schedule one role's surviving-piece pass with one call per motif and subdivision. 

### `phases`

 List the four surviving-piece visits in role order. 

### `visit_fields`

 Evaluate the four fixed visits against the allocation's actual heads.
Only the phase stop depends on the number of dense motifs. 
