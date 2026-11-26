---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionIteration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionIteration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionIteration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Unary runtime-loop execution used by both convolution loops. The body
obligation contains actual executions; the loop invariant concerns physical
stacks and may include decoded coefficient arrays and their lengths. 

### `unaryBudget`

 One branch test per iteration plus the final failing branch. 

### `unaryRun_eval`

 The initial physical peek is included in the bound. The body may change
all registers because the next peek establishes the loop guard anew. 
