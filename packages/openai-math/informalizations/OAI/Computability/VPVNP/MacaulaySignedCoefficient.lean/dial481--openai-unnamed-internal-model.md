---
{
  "module": "OAI/Computability/VPVNP/MacaulaySignedCoefficient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySignedCoefficient.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySignedCoefficient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Original-equation coefficients on the native matrix-reader bus 

### `preload`

 Install the signed coefficient routine's initial layout and empty input and output stacks
at the embedded payload ports. 

### `callSpace`

 Stack-length bound for one signed coefficient lookup, covering the Boolean checker,
coefficient bank and local scalar operations. 

### `callTime`

 Tick bound for one signed coefficient lookup, including both witness counts and the local
scalar operations. 

### `coefficient`

 On a divisible original row the decoded index and exponent buffer yield
the encoded coefficient of the integer system after base change to the
evaluation field. All scan buffers and the leaf advice survive the call. 
