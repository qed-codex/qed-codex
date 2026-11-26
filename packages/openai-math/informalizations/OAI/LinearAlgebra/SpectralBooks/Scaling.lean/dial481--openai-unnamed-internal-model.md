---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/Scaling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Scaling.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Scaling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Logarithmic scaling of rectangular wire dimensions 

### `wireDimension`

 The integer wire dimension at scale `N` and weight `w`. 

### `wireDimension_le`

 For positive scales and nonnegative weights, rounding costs a factor of at most two. 

### `wireDimension_log_le`

 Rounding a wire dimension up adds at most one bit for nonnegative weights. 

### `tendsto_log_wireDimension_div`

 The normalized logarithmic dimension converges to the wire weight. 
