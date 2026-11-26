---
{
  "module": "OAI/Computability/VPVNP/LayerWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LayerWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LayerWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loop removal at bounded Poincaré cost

Section 5.3 of *VP and VNP differ over every field* removes loops from a
regular graph by doubling its vertex set. Each step moves to the opposite
layer, choosing equally between an old edge and a vertical edge.


### `layerWalk`

 The transition matrix of the loopless double cover. 

### `layerArcs_normalize`

 Dividing the doubled graph's integer multiplicities by its degree gives
the crossing/vertical transition kernel. 

### `layerWalk_hasPoincareBound`

 The loopless double cover of a symmetric stochastic walk inherits a
uniform Poincaré constant. The estimate applies to every metric target. 

### `reachable_of_poincare`

 A Poincaré inequality for a target with two separated points forces the
support of a symmetric walk to be connected. Test with a two-valued map
constant on every component. 
