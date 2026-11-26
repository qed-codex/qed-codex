---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete inputs and score bytes for the global score builder

The sequential controller's memory invariant determines the assignment,
width, and processed-index stacks. Its high-stack invariant supplies the
encoded alphabet, depth, raw pair plans, and seed tables. These literal
equalities instantiate both inputs of the fixed score builder.


### `preparationContext`

 The preparation context reads the actual processed counter bytes. 

### `context`

 The candidate scorer receives the exact pair table produced by preparation. 

### `environment`

 All persistent high-stack inputs are explicit encodings. 

### `inputFor_of_memory`

 The two subroutine input conditions follow from the actual memory and high-stack invariants. 

### `scoreBytes_eq`

 The actual emitted score bytes equal the sequential controller's exact
natural objective, in the original alphabet order. 
