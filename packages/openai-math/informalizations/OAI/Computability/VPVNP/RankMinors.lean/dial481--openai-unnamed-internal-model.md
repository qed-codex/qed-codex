---
{
  "module": "OAI/Computability/VPVNP/RankMinors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankMinors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankMinors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Support of maximal minors

Appendix D.2 of *VP and VNP differ over every field* uses the fact that the
nonzero minors of order equal to the rank have independently chosen row and
column bases. All minors of larger order vanish.


### `compound_ne_zero_iff`

 At the rank of the matrix, the nonzero minors are precisely the pairs of
independent row and column selections. 

### `compound_eq_zero_of_rank_lt`

 Every minor of order strictly greater than the matrix rank vanishes. 
