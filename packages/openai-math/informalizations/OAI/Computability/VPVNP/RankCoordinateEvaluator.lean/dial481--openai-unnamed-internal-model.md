---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From suffix coordinates to the evaluator's linear-step matrices

A step of the counting evaluator starts at the current basis ordinal and chooses
the next ordinal. Its scalar is the coefficient at the *next* ordinal in the
image of the *current* basis vector. This is the entry of the transpose of the
usual column-vector matrix. The indexed Cramer target therefore uses the current
basis monomial, and its queried row ordinal uses the next one.


### `stepTarget`

 The row for the powered monomial obtained after acting on the current basis vector. 

### `stepCoordinate`

 Cramer scalar for the next basis coordinate after acting on the current vector. 

### `minorQuotient_eq_stepCoordinate`

 The packed Cramer quotient has the correct value over the advised ground
field, even when that field is presented through an algebra equivalence. 

### `Operation.linearAction`

 The linear map whose transpose is used in the basis-index transition. 

### `stepCoordinate_eq_transition`

 The encoded ordinal width can present any natural number equal to the computed
slice dimension. The row-column ordering here is the order of evaluator transitions. 

### `readsEntry_of_suffix`

 An actual returning suffix-coordinate program meets the evaluator's entry-reader
contract. Its packed result is identified by its value in the ground field, and its
registers and private bank are restored at the return. 
