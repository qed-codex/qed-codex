---
{
  "module": "OAI/Computability/VPVNP/ShrinkingSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkingSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkingSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shrinking step's slot construction

Lemma C.1 of *VP and VNP differ over every field* for a directed input
slot graph with arbitrary binary displacements. `dyadic_slot_packing`
counts the thick wires, CD demands and placed role incidences on the actual
input. `dyadicSurvivingSlots` constructs the indexed, regularized output
lift. The lane-zero labels preserve parallel edges and subdivisions.


### `dyadic_slot_packing`

 The multiplicities and distinct-endpoint assertions of Lemma C.1, for
the construction obtained directly from the given input graph. 

### `dyadicSurvivingSlots`

 Number the actual surviving arcs by their lane-zero motif IDs, padding
with dummy arcs to any admissible output degree `d'`. The resulting graph
has packed bases `(old vertex, tag)` and the original remaining lane. 

### `orderedDyadicSurvivingSlots`

 The supplied vertex numbering determines both the greedy scans and the
integer keys for sorting the local incoming and outgoing incidence lists. 
