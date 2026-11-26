---
{
  "module": "OAI/Computability/VPVNP/PackedShrinkStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackedShrinkStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackedShrinkStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quadratic energy bound for the actual shrinking step

The degree threshold in Section 7.2 works for every packed graph with the
same old degree and number of color bits. Each list of admitted six-party
terms determines a single layout. With the paper's floor subdivisions, the
energy of its numbered outgoing arcs (including the zero-width dummies)
satisfies equation (7.2), with a constant independent of the old widths and
of the number of positions.


### `subdivisions`

 Parallel slots assigned to each of the four surviving supply types. 

### `Ready`

 The same integral subdivision profile is used on all motifs and all lanes. 

### `eventually_ready`

 In particular, all sufficiently large power-of-two degrees can be used. 

### `shrinkFactor_lt_one`

 Strict contraction of the leading term under the chosen loss allowance. 

### `termWidths`

 All eight supply widths at each occurrence, for the selected term list. 

### `packed_energy_from_terms`

 The energy of the genuine, subdivided arc identifiers before reindexing. 

### `shrinkSlotWidth_energy_le`

 Equation (7.2) on the numbered outgoing arcs of the graph passed to the
next compressor step. Dummy arcs carry zero payload at every remaining lane. 
