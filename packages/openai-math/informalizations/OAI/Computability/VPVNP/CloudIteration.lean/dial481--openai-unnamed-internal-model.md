---
{
  "module": "OAI/Computability/VPVNP/CloudIteration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CloudIteration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CloudIteration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iterating cloud replacement at a fixed degree

Section 5.3 of *VP and VNP differ over every field* iterates the replacement
starting at a single vertex. All targets in the given family share the same
sequence of integer adjacency matrices. For a port graph with bound `β ≥ 1`,
the explicit bound `444 * β` is preserved when `t ≥ 1776 * β`.


### `hasPoincareBound_equiv`

 Poincaré bounds are independent of vertex labels. 

### `normalize_replacementArcs`

 Normalizing the integer replacement by its degree gives the equal mixture
of internal moves and matching moves. 

### `exists_cloudStep`

 One amplification step on integral regular multigraphs. The matching,
hence the resulting graph, works simultaneously for every target. 

### `exists_iteratedCloudGraph`

 Starting with a single vertex and `2h` loops, repeated cloud replacement
gives orders `Q^j`, keeping both degree and Poincaré bound independent of `j`. 

### `exists_looplessCloudGraph`

 The double cover of each iterated graph has no loops and has a common
Poincaré bound for the entire target family. Its order and degree are twice
those of the iterated graph. 
