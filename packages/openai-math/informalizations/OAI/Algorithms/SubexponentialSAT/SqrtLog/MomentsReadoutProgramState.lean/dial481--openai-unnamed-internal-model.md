---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsReadoutProgramState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsReadoutProgramState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsReadoutProgramState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed forty-stack workspace for the two runtime readout counters. 

 Actual stack construction of the sparse key (u,z,empty support), followed
by the paid query cleanup and unary-index increment. 

 One concrete (u,z) coefficient fetch, addition, and index advance. 

 The U loop is driven by a real unary stack. Every visit invokes the
concrete key builder and dictionary scan; no callback is left abstract. 

 Seed one Z accumulator from the cached zero vector and append the
completed coefficient to the output, paying for every copy and reversal. 

 Runtime Z enumeration. Completed fixed-width coefficients are prepended
in reverse and are restored once by the final output transfer. 

 Build the all-false support mask from the actual ambient shape stack.
The loop length is the ambient number of variables, including unused ones. 
