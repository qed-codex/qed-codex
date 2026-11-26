---
{
  "module": "OAI/Computability/VPVNP/PairTraversalStageSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalStageSize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalStageSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descriptor storage along the compression schedule

The descriptor arena begins with the cursor input sites, followed by one row
for every output site of every selected elementary pass. The selected pass
origins identify those counts with the actual shrink and refresh outputs.
Neither pass increases the number of sites.


### `levelLayer`

 Read the actual placement of this scheduled term in increasing old-site
order for each output position. 

### `selectedLayers_eq_levels`

 Every row and every child identifier, in scan order, is determined by
the corresponding concrete level of the compressor. 

### `selected_layer_counts`

 The count in each actual layer agrees with the selected state's site count. 

### `selected_layer_count_le`

 Every layer, including the initial leaves and the intermediate shrink
and refresh layers, has at most as many sites as the input. 

### `selected_count_sum_le`

 The leaf stage and at most one stage per elementary compression pass
bound the total number of rows reserved by Appendix E. 

### `selected_words_le_stages`

 The number of words in the selected native descriptor arena, with its
two header words and fixed child-list capacity per row. 
