---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorCellEquivalence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorCellEquivalence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorCellEquivalence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Equivalence of the scheduled cell comparisons with a tape transition

The private RAM visits old cells in increasing order. A one-cell move
permutes the output positions cyclically and pairs the old discarded
endpoint with the new blank endpoint. The extra blank check on that old
endpoint makes this exactly the unbounded-tape move.


### `cellDestination`

 The destination paired with old cell `i` in the RAM scan. 

### `cellClipped`

 Whether a nonstationary tape move clips this old cell at the boundary of the finite window. 

### `writtenSymbol`

 The symbol after writing at the head position, using the previous symbol at every other
cell. 

### `cellChecks_iff`

 The RAM comparison at every old cell is equivalent to both the exterior
blank guard and the complete equality of the proposed output tape. 
