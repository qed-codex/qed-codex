---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorSiteLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Following the physical loop through all calls of a cost bucket

Every successful start decreases the site allowance. In particular, when
the native call-count bound is exhausted the next attempted start has zero
credit and physically rejects. A failed call retains its actual halting
row even when earlier calls have already returned.


### `startLabel`

 Select the first-call label at bucket entry or the new-call label for a later iteration. 

### `StartRuns`

 The two startup labels have the same charged call specification.
The first one additionally initializes the global allowance. 

### `iteration_loop`

 From the iteration test through the entire remaining bucket. The
singleton progress returned by each native call composes into the complete
ordered list of reports and emitted probe records. 
