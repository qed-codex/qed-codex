---
{
  "module": "OAI/Computability/VPVNP/ExactOneSolutions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneSolutions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneSolutions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The parsimonious conversion from CNF to exact-one constraints

For a satisfying assignment, the selector in each clause marks its first
satisfied literal. This fixes the filler of every implication. Conversely an
assignment meeting the exact-one constraints must use these same selectors
and fillers. Restricting to the input bits therefore gives a bijection.


### `encode`

 The unique extension of a satisfying assignment sets the first-match selectors
and the complementary filler in each active implication. 

### `solutionsEquiv`

 Each satisfying input has exactly one extension to the exact-one formula. 
