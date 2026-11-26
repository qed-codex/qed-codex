---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/FiniteExtensionRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/FiniteExtensionRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/FiniteExtensionRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Tensor rank under finite scalar extension

Expand two sites of a decomposition in a fixed basis of the extension.
A linear retraction of the field inclusion contracts the third site.
The dimension cost is constant across tensor powers.


### `power_scalarExtension`

 Kronecker powers commute with entrywise scalar extension. 

### `rankAtMost_of_finiteExtension`

 A finite extension of degree `d` saves at most a factor of `d²` in tensor rank. 

### `asymptoticRank_le_of_power_bound`

 A constant factor in a tensor-power rank bound disappears under roots. 

### `asymptoticRank_le_of_finiteExtension`

 Any exact decomposition over a finite extension bounds the asymptotic rank
over the original field. 
