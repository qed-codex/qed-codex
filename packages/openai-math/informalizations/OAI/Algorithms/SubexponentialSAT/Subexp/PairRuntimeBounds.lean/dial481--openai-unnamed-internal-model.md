---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PairRuntimeBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairRuntimeBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairRuntimeBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform bounds for the executed pair scorer

The polynomial parameter bounds physical input lengths.  The exponential
factor is the actual number of tuples emitted by each generator call.


### `sourceBudget_le`

 A fixed polynomial in physical input size times the actual per-pair
tuple count.  This bounds the exact source budget of `program_run`. 

### `physicalSize`

 Only physically stored lists occur in this parameter. 
