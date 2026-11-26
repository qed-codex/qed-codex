---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramContext.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramContext.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PolynomialExecutorProgramContext.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Persistent native arithmetic context for the source-row postfix machine.
The dispatcher owns26/27/28; neither coefficient-array service touches them. 

### `Ready.prepared_arithmetic`

 The native metadata is invariant under source, operand-stack, and binary
argument changes. This is stronger than the shared all-low-ports frame. 
