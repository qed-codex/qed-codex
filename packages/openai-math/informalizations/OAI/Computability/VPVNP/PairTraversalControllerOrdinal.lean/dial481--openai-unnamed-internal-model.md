---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerOrdinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerOrdinal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerOrdinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The persistent traversal controller ordinal

Both the role pass and the row pass use the same radix for site ordinals.
The radix reserves one more digit than the initial number of sites, so the
end of any layer is represented even if that layer has the maximum count.
The final return at phase-level twice the number of layers also fits the
word, uniformly over the selected compressor branches.


### `pack`

 Numerical encoding of the phase-level and the current site. 

### `decode_of_fit`

 The site and phase-level reads, including at an empty layer. 

### `decode_stop`

 The terminal sentinel decodes to phase-level twice the number of layers. 

### `one_div_levels`

 A level count of one selects the terminal site's count. 

### `index_words`

 The level, its nonzero flag, and its predecessor with saturation at zero. 

### `next_site`

 Advancing within the current layer adds one to the packed word. 

### `next_level`

 Skipping to the next layer resets the site digit, including the final
transition to the terminal sentinel. 

### `eventually_selected_fit`

 The controller's two full passes and the terminal sentinel fit one host
word at a common threshold preceding all choices of specialization and branch. 
