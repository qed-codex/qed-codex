---
{
  "module": "OAI/Computability/VPVNP/ShrinkStateInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reindexing the actual input of a shrinking pass

The state network numbers an outgoing edge by a full site and a slot.
Appendix C writes the same edge in color, slot-label, tag and remaining-lane
coordinates. The following relabelling identifies both incident sites and
the entire payload of each directed edge, including parallel edges.


### `packingInputSites`

 Reassemble all lane fields of a packed input position. 

### `packingInputEdges`

 Reassemble the outgoing edge in the original state network's site-first
numbering. The local slot index is retained at both ends. 

### `packingData`

 Color and tag the base vertices in their stored numerical order. 

### `packingWidth`

 Old widths in the field order of the shrinking construction. 

### `packingInputIso`

 An isomorphism of the old wire tensor in the proof with the tensor of the
input state. On each word alphabet it is the identity. 

### `packingHalfEquiv`

 The independent incoming and outgoing half-words at each state site
correspond to the packed half-words at its preimage. 

### `reindexPackingStep`

 Transport an entire packed identity, including its local kernels, to the
actual input coordinates. Every output keeps its original numbering. 

### `positions_packing`

 Packing the input coordinates preserves the count of processor sites. 

### `energy_packingWidth`

 The old sum in the shrinking estimate is exactly the input state's energy. 
