---
{
  "module": "OAI/Computability/VPVNP/GreedySuffixIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GreedySuffixIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GreedySuffixIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Querying basis ordinals after a prescribed row prefix

Appendix D keeps the independent monomial rows following the equation rows.
Their dense indices are the ordinals of the greedy rows of the full matrix
offset by the rank of the equation prefix.


### `suffixDimension`

 Number of independent monomial rows after reducing modulo the preceding rows. 

### `suffixBasisIndex`

 Read the original index of a selected monomial by its ordinal among the
independent monomial rows. The prefix rank scan always uses the original rows. 
