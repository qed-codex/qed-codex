---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafStatisticsSemanticsFactor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafStatisticsSemanticsFactor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafStatisticsSemanticsFactor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The exact native neutral ID is the rank of its uncovered original owner.
This is an explicit indexing equivalence, not just equality of cardinalities. 

### `neutralAt`

 The `j`th neutral factor is attached to the `j`th uncovered free owner. 

### `factorCodeEquiv`

 Encode a semantic factor by its actual native ID: original IDs are retained,
and an uncovered owner gets `q + idxOf owner` in the forward owner list. 
