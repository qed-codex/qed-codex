---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshActualStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshActualStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshActualStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The degree refresh on the actual lifted slots

The blockwise contraction uses source-port order within each bundle. The
isomorphisms below restore the original and refreshed slot coordinates,
including their lane translations, without identifying parallel arcs. The
actual widths are those charged to equation (7.3).


### `actualWireGraph`

 The word network on a lifted graph. Its edges are actual outgoing slots,
and widths are indexed by a base arc and source lane. 

### `originalSites`

 Old positions in bundle coordinates have their original port as the
last component, separate from the remaining lane. 

### `originalEdges`

 Restore the outgoing slot number and the source lane of an individual
old segment. 

### `groupedWidths`

 The regrouped old width is exactly the field carried by the original
arc in its original lane. 

### `originalIso`

 Reindex the old wire tensor by its actual directed slots. Both endpoint
maps and the full alphabet on every arc are preserved. 

### `promotedSites`

 Promote the port to part of the new base vertex while retaining the
remaining lane. 

### `promotedEdges`

 All copies of the grouped external, expander and cyclic padding arcs
biject with the numbered outgoing slots of the refreshed graph. 

### `promotedIso`

 The grouped output is isomorphic to the actual lifted graph with the
widths charged in (7.3). The selected motif may use any alphabet with the
specified word encoding at each expander slot. 

### `actualRefreshStep`

 The exact degree-refresh step on actual slot coordinates, with one
motif choice per block and the selected word widths on the refreshed graph. 

### `actualRefreshStep_output`

 In each branch the output network uses the stated refreshed slot graph
and its corresponding actual widths. 

### `actualRefreshStep_place`

 Each original vertex factor stays whole at the same physical position
after promoting its port to a base label. 
