---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete outer count execution. The final canonicalization and marked
return consume the entire accumulated binary count. Their compact boundary is
proved separately from the transient workspace used by the query. 

### `canonicalize`

 The actual unsigned normalizer is run once after all high assignments. 

### `canonicalized_bound`

 No transient query cap is fed back into the retained-word bound. 

### `markedReturn`

 The whole-count readback does not use the count head as a SAT bit. 

### `returned_stacks`

 Cleanup preserves exactly the caller words in the fixed marked-query ABI.
The high accumulator is first normalized and copied in full, then reclaimed. 

### `markedReturn_trace_space`

 Actual canonicalization and cleanup on the same run, with an independent
all-prefix cap. This local suffix has no evaluator or successful-layout input. 

### `returned_record`

 The canonical marked result has the exact parser presentation consumed by
all-mark accumulation. 

### `installAccepted`

 Reuse the complete cleanup, then physically put the canonical word back on
788 for the final unmarked query. The temporary marked-output word is erased. 

### `accepted_stacks`

 The accepted-query ABI returns only788. All marker, high-iterator and
query-owned scratch ports have paid cleanup instructions. 

### `acceptedReturn_trace_space`

 Final unmarked readback uses the same actual canonicalization and paid
cleanup, then a measured copy and clear. The transient cap is uniform. 
