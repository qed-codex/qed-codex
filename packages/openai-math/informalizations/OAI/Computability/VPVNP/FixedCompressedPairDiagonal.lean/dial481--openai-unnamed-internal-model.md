---
{
  "module": "OAI/Computability/VPVNP/FixedCompressedPairDiagonal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedCompressedPairDiagonal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedCompressedPairDiagonal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reducing the final native compiler obligation to the compressed pair

The actual evaluator tail handles the second half of the diagonal chain.
A sufficiently large address multiplier makes its physical frames and
per-call budgets fit. Thus only the compressed first-half pair computation
enters the compiler premise below.


### `PairCompiler`

 For arbitrarily large address multipliers, one fixed pair table realizes all sufficiently large input lengths. 
