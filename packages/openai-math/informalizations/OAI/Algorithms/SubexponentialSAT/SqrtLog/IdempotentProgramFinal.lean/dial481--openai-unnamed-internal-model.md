---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramFinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramFinal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramFinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete native Newton lift and the exact degree-three coefficient output.
The input-state contract includes prepared scalar constants and the cached
H-adic table; native preparation is a separate remaining construction. 

### `nativeLiftWords_run`

 An actual fixed finite bit program computes every Newton iteration and all
array arithmetic from the supplied prepared state. 

### `binaryLiftWords_indicator`

 The words computed by the native lift have exactly the required indicator
semantics. Degree below three is structural via `digitPolynomial_degree`. 
