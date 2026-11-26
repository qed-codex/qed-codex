---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/RankLimit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/RankLimit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/RankLimit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The limit defining asymptotic tensor rank

Splitting Kronecker powers gives a submultiplicative sequence of natural
ranks. Applying Fekete's lemma to their logarithms identifies the manuscript's
limit with the infimum of the positive-index rank roots.


### `tendsto_root_of_submultiplicative`

 The positive-index root infimum is the limit for a natural-valued
submultiplicative sequence, including sequences with a zero term. 

### `tensorRank_power_add_le`

 Splitting each site's words into a prefix and suffix shows that the
rank of Kronecker powers is submultiplicative. 

### `tendsto_tensorRank_power_root`

 The tensor-power rank roots converge to asymptotic rank. 
