---
{
  "module": "OAI/Computability/VPVNP/GreedyBasis.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GreedyBasis.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GreedyBasis.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The isolated minimum-weight basis in the rank query

Appendix D.2 of *VP and VNP differ over every field* assigns a row or column
its one-based index as a weight. Keeping exactly the vectors that increase the
span on a left-to-right scan gives the unique minimum-weight basis. The proof
uses prefix ranks and applies over every field, also when the rank is zero.


### `weight_lt_of_prefix_dominance`

 At fixed cardinality, domination of every prefix count strictly lowers the sum of
one-based indices unless the two sets coincide. 

### `greedyIndices`

 Retain a row exactly when it increases the span of its predecessors. 

### `greedyIndices_prefix`

 On each prefix the retained rows form an independent spanning family. 

### `exists_isolatedBasis`

 Among all independent rank-sized subsets, the first basis selected in index order is
uniquely of smallest total weight. Its indices span the entire family. 
