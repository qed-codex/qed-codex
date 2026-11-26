---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Rank semantics for the native all-visits Boolean odometer. These maps are
proof-level reindexings; the machine changes its physical tuple in place. 

### `sum_original_by_rank`

 Every original assignment occurs once in the outer rank sum and inner
free-coordinate sum. This is the exact count bridge, including unused vars. 
