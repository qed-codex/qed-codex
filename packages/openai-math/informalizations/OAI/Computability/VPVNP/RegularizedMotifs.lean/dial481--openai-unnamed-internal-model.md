---
{
  "module": "OAI/Computability/VPVNP/RegularizedMotifs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegularizedMotifs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegularizedMotifs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The regularized graph of a shrinking step

The graph constructed at the end of Section 7.2 of *VP and VNP differ
over every field* is a lift over the pairs consisting of an old base and a
tag. A motif in its lane-zero section supplies one base identifier for each
surviving type and subdivision. The role-to-role displacement restores the
actual lanes at its ends. The uniform role counts give the common deficit
that the cyclic dummy arcs fill.


### `baseRoleFiberEquiv`

 Each role incidence at an absolute site corresponds to exactly one
lane-zero motif at its packed base. Reindexing by the role's lane handles
both ends of the edge and either layout. 

### `roleBase`

 The packed base of a role of a lane-zero motif. 

### `roleDisplacement`

 Fixed displacement of a role edge on a lane-zero ID. 

### `survivingLaneEquiv`

 Reindex every actual subdivided role edge by its lane-zero ID and its
absolute source-role lane. The inverse recovers the same motif and
subdivision, including when several supply types use the same two roles. 

### `survivingLane_endpoints`

 The reconstructed actual ID has precisely the source and target sites
of the corresponding lifted arc. 

### `card_roleBase`

 Each packed base has the same `dQ` role count among lane-zero motifs. 

### `survivingDegree`

 The uniform in- and outdegree before cyclic padding. 

### `regularizedSlotIndexing`

 A lift of the padded, subdivided surviving graph over the packed bases.
Every genuine ID is numbered in the given order of lane-zero IDs, and the
dummy slots go to the next tag without changing the remaining lane. 
