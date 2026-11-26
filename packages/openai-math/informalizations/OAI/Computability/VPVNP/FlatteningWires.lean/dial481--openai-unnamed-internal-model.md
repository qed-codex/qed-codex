---
{
  "module": "OAI/Computability/VPVNP/FlatteningWires.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FlatteningWires.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FlatteningWires.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Identity wires across a flattening cut

Flattening at one party gives the cut-rank examples of Section 2. A crossing wire
contains a full identity minor. A wire among the other parties contributes one row.


### `flattening_rank_wire_endpoint`

 The cut through one endpoint of a wire has an identity minor of its full dimension. 

### `flattening_rank_wire_away`

 If the cut party meets neither endpoint, a wire of positive dimension has
one row and contains a nonzero entry. 

### `flattening_rank_wire`

 A positive-dimensional identity wire has its full rank across the cut
and rank one when both endpoints lie on the same side. 

### `flatteningPoint_wireDistance`

 Binary wires give exactly the cut distance at the flattening spectral point. 
