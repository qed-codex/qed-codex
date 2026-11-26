---
{
  "module": "OAI/Computability/VPVNP/CursorRouting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorRouting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorRouting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Routing the transcript fields on the cursor graph

In §12 of *VP and VNP differ over every field*, each site address traverses the cursor cycle
once per message system. It flips the current bit exactly when the system's mask specifies
that bit. At intermediate cursors every field comes from a unique sender. Unused arcs are
clamped, used arcs carry equal payloads at consecutive positions, and the returning arc
supplies the receiving validator. These local checks preserve the contraction exactly.


### `Site`

 A binary word of width `D` used to address a site. 

### `routePos`

 Location at cursor `k` under the route that flips the bits set in `mask`. 

### `stepSite`

 One arc of the cursor graph, either staying at `x` or flipping bit `j`. 

### `successor_mask_eq`

 Incrementing a binary address changes exactly its trailing ones and the zero preceding them. 

### `successorMasks`

 The masks of all nonwrapping successor messages in a graph with `D` address bits. 

### `card_successorMasks_le`

 Section 12's partition of successor messages uses at most one mask per address bit. 

### `ArcFields`

 Fields on the two outgoing arc choices of every processor and cursor. Each
communication system gets its own instance of these fields. 

### `arcTarget`

 Both outgoing arcs advance the cursor cyclically. The flip arc additionally
changes the current cursor bit of the processor. 

### `LocalTies`

 The pointwise equalities checked at the routing vertices. Unselected arc choices
are clamped to `blank`. A message can itself be blank when its sender is inactive. 

### `routedFields`

 Pull each used field back along the prefix permutation to its unique sender. 

### `LocalTies.field_at`

 Following the local equalities from the sender determines each used field. 

### `existsUnique_fields_iff`

 Prescribed sends and receives extend uniquely exactly when their endpoints match. 

### `contraction_eq`

 After assigning a separate routed field to each mask system, summing over all
route bits and checking their ties leaves the original contraction unchanged. 

### `routedContraction`

 Sum over the routed fields, giving zero to a setting that fails to carry
any consistent source assignment. 

### `routed_contraction_eq`

 When the send fields recover the old assignment, the contraction can be indexed
solely by routed arc fields. The clamps and ties discard all invalid settings. 

### `RAMSystem`

 A successor mask class, or a cross-site layer of the sorting network. 

### `ramFieldBits`

 Every system uses its own field on both choices of arc at each cursor. 

### `cursorPositions_card`

 Exact number of processor-cursor positions before compression. 

### `ramArcWidth`

 Width of one of the two cursor arcs when both reserve a field for every system. 

### `systemMask`

 A successor class flips a low-bit prefix. A sorting layer flips one site bit. 

### `successorClass`

 The unique mask class of a nonwrapping successor edge, computed from its sender. 

### `ramSend`

 At an active successor source the route uses the corresponding physical
send. At the last site and in other classes its source is the all-zero field. 

### `ramReceive`

 An arrival reads the source identified by the inverse cursor permutation. 

### `ramSend_injective`

 Restricting the source arrays to all routed systems preserves every physical send. 

### `RAMFields`

 Route-bit assignment, with separate payload bits for each system on every
cursor arc. These are the shared variables in the expanded contraction. 

### `readSends`

 Recover each physical send directly from its outgoing field at cursor zero.
At a successor boundary only its own mask class is consulted. 

### `carries_iff_readSends`

 A routed field assignment can be checked using the directly addressed sends
read at cursor zero. No search over a compatible original assignment is required. 

### `ramContraction`

 Unweighted contraction on the cursor graph, summing over its actual bit fields. 

### `ramContraction_pathCount`

 Applied to the local validators, the routed tensor network still counts precisely
the capped accepting RAM paths, including all their private branches. 
