---
{
  "module": "OAI/Computability/VPVNP/PortMatching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PortMatching.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PortMatching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matching ports with prescribed transition counts

In the replacement construction of Section 5.3 of *VP and VNP differ over
every field*, vertex `v` gets `Q` ports. Its ports are indexed by a
destination `w` and an arc number in `Fin (a v w)`. Reversing an arc
keeps this number, so symmetry of the multiplicity matrix gives an
involution, with the ports for self-transitions fixed individually.


### `exists_portMatching`

 A symmetric matrix of natural arc multiplicities with row sums `Q` is
realized by an involution on `Q` ports at each vertex. 

### `replacementArcs`

 The replacement puts the graph on `K` inside each cloud and adds `h`
copies of each port's matching arc. 

### `replacementArcs_degree`

 Each vertex in the replacement has the original degree `2 * h`. 

### `layerArcs`

 The final graph in Section 5.3 takes each old edge across the two layers
and adds `b` vertical arcs at each vertex. 
