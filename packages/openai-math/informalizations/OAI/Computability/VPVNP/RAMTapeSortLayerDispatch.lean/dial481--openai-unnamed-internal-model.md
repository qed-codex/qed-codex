---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortLayerDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Choosing the local or cross-site sorting layer

A layer with stride exponent `j` uses the incident stream precisely when
the site holds `2^h` rows and `h ≤ j`. The finite control compares the unary
exponents before any stream is split. It removes one mark from each exponent
per round and saves the number of rounds above a delimiter. It restores the
two exponents and consumes the delimiter before entering the selected branch.


### `Port`

 Unary block-width and stride exponents together with the scratch stack used to compare and
restore them before layer dispatch. 

### `routine`

 The branch callback receives the full caller store, with both exponents
and the previous contents of the temporary stack restored. 

### `cross_runs`

 Cross-site stride, including the equality boundary. 

### `local_runs`

 Strides strictly below the site's row width use its materialized block. 
