---
{
  "module": "OAI/Computability/VPVNP/SlotTranslation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotTranslation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotTranslation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Translation on the unconsumed lane

In the last part of Appendix C, a common layout commutes with translation
in the remaining lane. Each orbit of actual motifs is represented uniquely
by the motif whose original wire starts at lane zero. A surviving role edge
over that representative lifts with one fixed lane displacement.


### `translateSite`

 Move a packed site in its remaining lane, retaining the old base and tag. 

### `translatePosition`

 Move the packed-site component, retaining the slot label and color bits. 

### `translateArc`

 The action on original arc labels is given in outgoing numbering. 

### `translateMotif`

 Translation on actual arcs restricts to the wires indexing the motifs. 

### `sourceLane`

 Unconsumed lane of the old wire in its original outgoing numbering. 

### `BaseMotif`

 Finite orbit labels for motifs, indexed by representatives at source lane zero. 

### `baseMotif`

 The representative obtained by translating the source back to zero. 

### `motifLaneEquiv`

 A motif is specified by its lane-zero label and the remaining lane. 

### `roleLaneEquiv`

 Reindex an orbit by the lane of any chosen source role of a surviving edge. 

### `roleLane_endpoints`

 The lift of a surviving edge, enumerated by its source-role lane, has
displacement equal to the difference of the two lane-zero role coordinates. 
