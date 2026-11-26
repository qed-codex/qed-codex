---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackInterpretation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackInterpretation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackInterpretation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rank over the advised field from native scalar words

Interpretation commutes with the weighted Gram coefficients and the
reverse characteristic polynomial. This identifies the numerical rank
returned by the packed-word machine with matrix rank in the advised
finite extension.


### `computeRank_interpreted`

 Correctness of a rank scan in an executable ring embedded in a field. 

### `rank_correct`

 Compute in binary coefficient words and interpret the output rank in the
advised irreducible extension. Only the input matrix entries are read. 
