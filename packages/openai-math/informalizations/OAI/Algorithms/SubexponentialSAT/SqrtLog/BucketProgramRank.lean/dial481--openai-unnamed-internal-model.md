---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Rank bounds the number of actual stored buckets. The primitive machine
still processes all rows and its serialization costs use their full count. 

### `storedTable_length_le_rank`

 This is the exact list passed to the stored bucket encoder by Controller:
all labelled assignments in forward order, with deduplicated keys obtained
from reverse record order. Its length obeys the rational rank bound. 
