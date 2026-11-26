---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramGrouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramGrouping.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramGrouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete byte-string deduplication and all-key bucket scans. This file
starts at the explicit labelled-record table, not at an uncharged signature
oracle. Producing that table is the separate dot-product stage. 

### `attained_bucket_representative`

 A representative can always be read as the first stored assignment.
The machine output stores every assignment, so this needs no choice oracle. 

### `keyDedup_runsIn`

 Actual key deduplication, with quadratic measured encoded-input cost. 

### `groupProgram_trace`

 One fixed all-key controller executes actual byte comparisons and emits
all attained buckets. The initial unary minimum is zero and remains zero;
its otherwise-unused legacy accumulator costs are included in the budget. 

### `groupProgram_budget`

 Each record and query is scanned; all resulting costs are polynomial
in the explicit table length and the number of attained keys. 
