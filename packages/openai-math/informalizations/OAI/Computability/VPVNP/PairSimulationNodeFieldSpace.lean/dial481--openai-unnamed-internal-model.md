---
{
  "module": "OAI/Computability/VPVNP/PairSimulationNodeFieldSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationNodeFieldSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationNodeFieldSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word capacity of the private DFS argument frames

Section 13 indexes a private argument interval by the absolute address of its
DFS row. The row lies in the selected branch's descriptor region, while the
stride only needs to accommodate the two sets of half-wire fields of a single
site. Bounding both before choosing the branch gives a live-word bound on the
product of row address and stride, including all offsets used by the map
entry readers.


### `packed_length_le`

 All the independent half-wires at a vertex fit in two degree-sized rows
of maximum-width slots. 

### `field_end_le`

 Even an empty field has its start and exclusive end inside the full
argument interval. 

### `frameStride`

 Reserve both sets of numbered half-wires using the fixed schedule's
maximum degree and an upper bound on every selected width. 

### `ReadEndsFit`

 The four kinds of map-reader endpoints, including cumulative payload
offsets even when a selector sequence later fails its total-width check. 

### `eventually_sparseFrame`

 Polynomial bounds may be fixed independently for the first private
address, the *absolute* row address, the stride and an additional scratch
suffix. Every address up to the resulting end supports the map's reads. 

### `Arena.scratch`

 Start shared map scratch beyond the reserved frame for the last possible
node. Frames at all smaller absolute node addresses precede this workspace. 

### `eventually_global_map_scratch`

 The same address bound applies to a common scratch arena above *all*
private argument frames, for every address in its reserved suffix. 

### `SiteFits`

 The total argument interval and every individual native slot endpoint
lie below the word modulus. The map read bound is specialized to the actual
`fieldAddress`, independent of the guessed bits. 

### `eventually_selected_node_fields`

 For the actual selected cursor history, all frame and slot endpoints fit
on every intermediate input and on the final state. The threshold precedes
the coefficient specialization, the branch, the visited DFS node and the
old half-wire values. 
