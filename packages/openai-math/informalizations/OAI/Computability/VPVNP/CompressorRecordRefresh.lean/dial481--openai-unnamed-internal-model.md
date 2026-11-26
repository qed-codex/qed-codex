---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefresh.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefresh.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefresh.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Directly indexed records of the degree-restoring step

A source bundle specifies the old base arc and the remaining lane. Its numbered segments
are in source-port order. At the destination the incoming slot and translated port index
the same segment. We relate the emitted offset and width records to the bit indices of the
actual refresh kernel, including local diagonal checks and the two copies of the off-diagonal
demand. We also give the endpoint and width tables for the external, expander and dummy slots.


### `SegmentRecord`

 Both endpoint identifiers and one interval in the external word. An endpoint consists
of its block, its slot and its old port. Its first two components also locate the external
slot at which this interval is read. 

### `SegmentRecord.outgoing`

 The outgoing segment identified by its source bundle and numbered port. 

### `SegmentRecord.incoming`

 The same segment's incoming bundle and translated port at the destination. 

### `SegmentRecord.offset`

 Starting bit offset of the segment in the concatenation ordered by source port. 

### `SegmentRecord.width`

 Number of bits contributed by this segment to its external bundle. 

### `outgoingRecord`

 Generate the record of an old actual arc in source-bundle coordinates. 

### `incomingRecord`

 Destination slot lookup inverts the remaining-lane translation and then the port
translation. In particular, it retains the prefix total of the *source* ordering. 

### `incoming_unique`

 Every actual incoming half-slot receives exactly one of the emitted rows. 

### `old_slot_endpoints`

 The emitted old endpoint slots are those of the original lifted network. 

### `segment_in_scan`

 The prefix scan of the widths writes the exact record, also when its interval is empty. 

### `port_bit_reads`

 For any chosen external payload the record's bit addresses recover the actual outgoing
and incoming segment arguments, as read by the local kernel. 

### `local_bit_reads`

 The same interval addresses work on arbitrary incident half-wires. The incoming and
outgoing external slots are distinct, so the two independently chosen words extend to a
single test assignment without imposing any extra equality. 

### `demandRecord`

 Off-diagonal motif demand references the old half-slot at `tieSource` and its external
segment at `tieTarget`. The flag in `Tie` selects the outgoing or incoming records. 

### `NewSlot`

 Both numbered endpoints of one refreshed arc. Widths may vary across lanes and terms. 

### `NewSlot.src`

 Source site and outgoing slot number of a refreshed actual arc. 

### `NewSlot.dst`

 Destination site and incoming slot number of the same refreshed arc. 

### `NewSlot.width`

 Number of bits carried by this refreshed external, expander, or padding arc. 

### `slotRecord`

 Append the sole external slot, the expander slots in expander order and the dummy slots
in padding order. The same expander edge table supplies the incoming slot number. 

### `slotTable`

 A full output slot table at a physical port, generated in slot-number order. 

### `visit_counts`

 The number of segment visits and slot records is linear in the number of positions
for the fixed degrees of this substep. 

### `numbered`

 The source-major index is invertible by quotient and remainder with divisor `D`. 

### `translated_index`

 The numerical destination of a segment uses the bundle number, degree and translated port. 

### `visit_destination`

 With the target and shift supplied by the old slot table, the address computed by
`visit` is the number of the actual translated incoming half-slot. 
