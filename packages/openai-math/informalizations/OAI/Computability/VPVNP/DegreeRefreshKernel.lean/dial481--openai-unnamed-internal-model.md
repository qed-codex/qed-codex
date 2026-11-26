---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshKernel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact external-wire contraction in the degree refresh

Section 7.3 of *VP and VNP differ over every field* consumes one port index
per lane and concatenates all port payloads on each old base arc in source
port order. At each block, outgoing and incoming half-wires are tied to their
segments of the appropriate external wires. Summing the external payloads
restores the old network coefficient for every assignment of its half-wires.


### `Arc`

 A block and slot index the external bundle. The final coordinate gives an old source port. 

### `Word`

 A payload of a given bit width. 

### `oldPortMatching`

 Reindex the old matching by its block, slot and source port. 

### `source`

 Each old slot endpoint belongs to its block at the indicated port. 

### `External`

 External strings are concatenated in order of the old source ports. 

### `segment`

 Extract one old payload from the concatenated external string. 

### `segment_offset`

 The bit offset of a segment is the sum of the preceding source-port widths. 

### `segmentsEquiv`

 Ordered concatenation and segment extraction are mutually inverse, including
for bundles containing zero-width fields. 

### `segmentTest`

 A segment tie has coefficient one exactly when its two words agree. 

### `oldNetwork`

 The unexpanded wire tensor on the individual old ports. 

### `outgoingTest`

 The source half-wire is tied to the matching segment at the outgoing slot's port. 

### `incomingTest`

 At an incoming slot, the external segment uses the order of its original source.
Inverting the old slot permutation recovers both its source port and its width. 

### `blockTies`

 All segment ties in a block. For a slot equal to the old port its tie is local. 

### `external_contraction`

 Before the internal demand networks are converted, summing the external
bundle assignments gives the old wire equality tensor entrywise. 
