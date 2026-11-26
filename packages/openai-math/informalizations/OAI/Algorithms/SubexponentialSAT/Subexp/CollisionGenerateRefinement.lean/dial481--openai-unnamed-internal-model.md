---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CollisionGenerateRefinement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionGenerateRefinement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionGenerateRefinement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The generated collision count is the padded pair count

The actual tuple generator may reverse record order. Its multiplicities,
the fixed-width word encoding, and the collision callback nevertheless give
exactly the successful-leaf count of the explicit padded completion tree.


### `generated_pair_trueCount`

 Reversal of the actual generated records changes neither multiplicity nor
the successful-leaf count used by the subsequent unary tally. 
