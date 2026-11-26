---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutRankSignature.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutRankSignature.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutRankSignature.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime signatures may retain every raw integer row.  A row basis is
used only in this cardinality proof, never computed by the bucket program. 

### `card_range_boolSignature_le_rank`

 Rank-sensitive bound for the FULL attained raw-signature set.  The
existential basis contributes no runtime selection or minor enumeration. 
