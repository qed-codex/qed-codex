---
{
  "module": "OAI/Computability/VPVNP/SurvivingSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SurvivingSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SurvivingSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Incidences of the surviving slots in a shrinking step

Section 7.2 of *VP and VNP differ over every field* splits each surviving
supply edge of type `t` into the same number of slots at every motif.
Each of the packed roles A, B, D occurs equally often at every site.
Counting by type gives the same incoming and outgoing degree at every site.


### `PackedRole`

 The three packed positions of one motif, with D denoting the placed D*. 

### `roleMap`

 Apply one of the three role maps of the chosen layout to a motif. 

### `sourceRole`

 Orient the surviving wires in the order of their party names. Layout
`false` retains BC, BN, CN, DM and layout `true` retains AC, AM, CM, DN. 

### `targetRole`

 Destination roles after identifying ACM and DN in the first layout,
or BCN and DM in the second layout. 

### `Id`

 The type, original CD arc (motif), and index of a parallel slot. 

### `endpoint`

 The source or target of a surviving slot, determined by the role at
that end of its supply type. 

### `endpointFiberEquiv`

 Counting the incidences at a vertex can be done separately for each type,
then independently for the motif and the subdivision index. 

### `card_endpoint`

 The uniform degree formula applies to either orientation. Here `r` is
the common number of occurrences of each role at any site. 

### `endpoint_ne`

 Distinct roles give distinct endpoints, including after projection to the
base when the three projected roles are pairwise distinct. 

### `injective_roleMap`

 The three pairwise inequalities of Appendix C imply role injectivity. 

### `survivingRole`

 The three role maps of the actual packed layout. 

### `survivingSlot_bases_ne`

 Each surviving slot has distinct packed bases for its source and target,
including parallel slots of the same supply type. 

### `survivingSlot_degree`

 Before filling the deficit, every packed position has exactly
`d * Q * ∑ t, subdiv t` outgoing and incoming arcs in either layout. 
