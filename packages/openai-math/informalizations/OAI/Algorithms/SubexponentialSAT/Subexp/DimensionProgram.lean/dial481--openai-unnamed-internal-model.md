---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/DimensionProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/DimensionProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/DimensionProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed generator for all unary dimensions from zero through a runtime bound

The input bound is a unary stack, and the output is a framed list of unary
payloads. The program has no bound-dependent control labels.


### `Ready`

 Stack 0 is the remaining unary bound, stack 1 the current unary value,
stack 3 the accumulated framed records; stacks 2 and 4 are empty scratch. 

### `dimensionRows`

 Descending unary records, including both endpoints. 

### `loopCost`

 Exact cost of the bound-consuming loop, excluding its final endpoint. 
