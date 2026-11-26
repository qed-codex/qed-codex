---
{
  "module": "OAI/Computability/VPVNP/TensorFlatteningSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorFlatteningSum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorFlatteningSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Direct sums in one-party flattenings

Across a nontrivial cut, the pure columns form the block diagonal matrix of
the two summands. A column using both summands on the complementary parties
vanishes, so the full flattening and the block matrix have the same column span.


### `flattening_directSum_rank_block`

 Mixed columns are zero, so deleting them from the direct-sum flattening
preserves its rank. 

### `flattening_directSum_rank`

 Flattening rank is additive under direct sum when there are at least two parties. 
