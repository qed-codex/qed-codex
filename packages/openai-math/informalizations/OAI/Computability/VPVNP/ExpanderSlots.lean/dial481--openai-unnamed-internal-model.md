---
{
  "module": "OAI/Computability/VPVNP/ExpanderSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExpanderSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExpanderSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numbering the arcs of a regular expander

The graph supplied by Theorem 5.1 has paired arcs. The wire construction
uses one outgoing and one incoming slot for each arc. At the destination
we use the outgoing number of its reverse as the incoming slot number.


### `RegularArcGraph.toSlotGraph`

 Use paired arcs as the outgoing and incoming slots of a directed graph. 

### `exists_expanderSlots`

 A loop-free symmetric multiplicity matrix with constant degree admits a
slot numbering with exactly its specified arc counts. 

### `sum_outgoing`

 Group a sum over the outgoing slots of a vertex by destination. This
also applies when the cost depends on the source, by fixing the source. 
