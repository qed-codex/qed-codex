---
{
  "module": "OAI/Computability/VPVNP/SlotTags.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotTags.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotTags.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Greedy coloring and tag offsets for a finite base

In Appendix C of *VP and VNP differ over every field*, the color and
offset scans apply to any finite base. Choosing enumerations of the
base and tags gives the two existence statements used for wire packing.


### `exists_baseColor`

 The two ends of every base arc have distinct colors using `2d + 1`
colors. The bound counts both incoming and outgoing slots. 

### `exists_tagOffsets`

 The unary and binary conditions on the offsets at all incidences can
be satisfied simultaneously with the indicated tag cardinality. 
