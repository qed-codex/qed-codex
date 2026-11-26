---
{
  "module": "OAI/Computability/VPVNP/SlotBundleNumbering.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotBundleNumbering.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotBundleNumbering.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lane-independent combinatorial orders of the packed wires

For each base arc and source tag, order the old thick wires and the assigned
motifs at source-site lane zero. The order at every other lane is the transport
of that order. Thus the combinatorial identifiers used for Appendix E's scans
agree under translations even when the actual field widths vary by lane.


### `translateBundle`

 Preserve the bundle's base arc and tag while translating its remaining lane. 

### `translateThickWire`

 The old thick–thick wires also form complete translation orbits. 

### `laneBundleNumbering`

 Transport the chosen order of CD demands at lane zero to every bundle. 

### `laneThickNumbering`

 Transport the common endpoint order of the old thick wires from lane zero. 

### `laneBundleNumbering_translate`

 The translated motif occupies the same piece number in the translated bundle. 

### `laneThickNumbering_translate`

 Each original wire keeps its rank in the translated concatenation order. 

### `thickFiberIndex`

 At fixed source site and arc, the old thick wire is specified by its
color word and slot-coordinate label. 

### `motifFiberIndex_injective`

 The relative motif key distinguishes every old CD wire in a fixed bundle.
The role-A lane recovers the missing absolute coordinate from that bundle. 

### `sortedBundleNumbering`

 Order the CD demands of each bundle by their relative integer keys. The
order at an arbitrary lane is the transport of the same lane-zero list. 

### `sortedThickNumbering`

 Use the same integer-sorted list of old wires at both bundle ends and in
every translated lane. 
