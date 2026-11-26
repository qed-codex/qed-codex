---
{
  "module": "OAI/Computability/VPVNP/ShrinkPayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkPayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkPayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared payloads of the shrinking step

Each surviving motif wire in §7.2 is divided into contiguous strings. Its
subdivision labels are numbered at the base by lane-zero motif IDs and then
lifted at the absolute lane of the source role. A padding slot has a unique
empty string. Thus summing shared output-slot assignments is equivalent to
summing one shared word on each original surviving motif wire.


### `sliceBits`

 In subdivision order, the bit coordinates of the slices exhaust exactly
the input wire. This includes zero-length slices. 

### `sliceWords`

 Extract all slices of the shared wire word. The inverse concatenates
them in subdivision order. 

### `sliceBits_offset`

 The start of a slice is the sum of the preceding slice widths. 

### `classWidth`

 Classify output widths before outgoing slot numbering. 

### `classPayloads`

 Split all genuine wires and insert the empty word on each padding ID. 

### `shrinkArcEquiv`

 An actual outgoing arc label is its source site (base and lane) and
slot number. The genuine label retains its motif, type and subdivision,
and the lane of its source role fixes the copy of the numbered base arc. 

### `shrinkArcEquiv_genuine`

 Read a genuine numbered outgoing arc in source-lane coordinates. 

### `shrinkArcEquiv_padding`

 Each dummy ID is repeated at every remaining lane. 

### `shrinkArc_endpoints`

 Both ends of the numbered genuine wire coincide with its placed motif
roles, including the destination's translated lane and the incoming slot. 

### `shrinkSlotWidth`

 The actual lifted widths, indexed by outgoing base port and source lane,
as in `LiftedSlots.actualTarget`. 

### `shrinkSlotWidth_genuine`

 At a genuine arc the width is the designated subdivision of the
actual motif wire, including its lane-dependent width. 

### `shrinkSlotWidth_padding`

 All padding arcs have zero width. 

### `shrinkPayloadsEquiv`

 One shared word per original surviving motif wire is equivalent to one
shared word per numbered arc of the padded output graph. Specializing
`outgoing` to `dyadicSurvivingSlots.outgoing` gives the graph of Lemma C.1. 

### `shrinkPayloadsEquiv_genuine`

 Looking up a genuine arc in the encoded assignment returns precisely
its slice of the original motif word. 

### `sum_shrinkSlotWidth`

 Numbering and zero-width padding preserve any additive charge on the
widths with zero charge on a dummy. Taking the charge to be squared width
divided by slot mass identifies the actual graph energy in (7.2). 
