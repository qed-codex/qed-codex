---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/Flattening.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Flattening.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Flattening.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Flattening lower bounds in finite rectangular formats

Each flattening contains an identity minor. Applying the argument to powers,
whose wire indices are tuples, preserves the lower bound on taking roots.


### `matrixCoefficients_flattenings`

 A rank decomposition bounds the cardinalities of all three local bases. 

### `matrix_power_rankAtMost`

 Reindexing the three sites of a tensor power by tuples of wire indices
turns it into a single larger matrix multiplication tensor. 

### `matrix_flattening_le_tensorRank`

 The largest local dimension bounds ordinary rank from below. 

### `matrix_flattening_le_asymptoticRank`

 The largest local dimension bounds asymptotic rank from below over every field. 
