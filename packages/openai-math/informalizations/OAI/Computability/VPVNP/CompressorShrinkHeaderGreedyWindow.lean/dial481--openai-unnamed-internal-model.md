---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkHeaderGreedyWindow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkHeaderGreedyWindow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkHeaderGreedyWindow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The nine initial visits in each shrinking substep

The three header workers and six greedy workers occupy a contiguous window
of the full native block. The static phase and the repeated calendar ordinal
are recovered from the lengths of the actual preceding substeps.


### `headers`

 The three scheduled visits that publish the shrinking substep's input scalars, output
scalars and directory heads. 

### `greedy`

 The six greedy visits for this substep, using its old degree exponent and the first scratch
arena of its level. 

### `visits`

 The first nine visits of the shrinking substep, with the three header publications
preceding the six greedy visits. 

### `window`

 Locate the nine header and greedy visits as a consecutive segment of the full block script
at shrinking index `i`. 
