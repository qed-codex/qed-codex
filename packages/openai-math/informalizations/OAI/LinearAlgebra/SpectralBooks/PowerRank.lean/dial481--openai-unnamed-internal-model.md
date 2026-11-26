---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/PowerRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/PowerRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/PowerRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Powers of asymptotic tensor rank

Flattening a rectangular array of indices identifies iterated powers with a
single Kronecker power. The rank-root limit along the multiples of a positive
integer then gives the corresponding power of asymptotic rank.


### `tensorRank_power_power`

 Iterated tensor powers have the rank of the power at the product of their indices. 

### `asymptoticRank_power`

 Asymptotic rank is multiplicative on powers, including the zeroth power. 
