---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/TagWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/TagWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact finite word fibers for the tag inequality

Length-`N` words over `s` letters are grouped by their occurrence counts.
The ambient count-vector space has exactly `(N + 1)^s` elements. Finite
distributivity gives the total weight, so one fiber has at least the average
weight. There are no tensor, asymptotic, or factorial assumptions here.


### `occurrences`

 Number of positions occupied by the specified letter. 

### `countVector`

 Every occurrence count lies between zero and the word length. 

### `fiber`

 The finite set of words having exactly this count vector. 

### `wordWeight_eq_countWeight`

 Grouping positions by their letters identifies the common weight of a
count fiber. This is an exact finite product identity. 

### `fiberMass`

 Fiber mass is its actual cardinality times its common word weight. 

### `sum_wordWeight`

 Finite distributivity over all length-`N` words. 

### `sum_fiberMass`

 The fibers partition all words, including empty fibers without changing
the total mass. 

### `exists_fiberMass_ge_average`

 Exact polynomial-overhead bound, before any limit is taken. 

### `exists_nonempty_fiberMass_ge_average`

 A positive total gives a genuinely nonempty selected word fiber. 
