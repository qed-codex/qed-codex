---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramFixed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramFixed.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramFixed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-length coefficient-array carriers for the local CRT/Horner loops.
The multiplication service obtains its zero array and length from protected
caches192/193. The relocation is in the finite instruction table, so no tape
copy is charged or hidden by the change of physical port names. 

### `mul_spec`

 No high cache invariant is assumed by the service: only the protected
low workspace, encoded operands, and its two empty output buffers. 

### `add_spec`

 The fixed-length addition instance uses the same restored native frame. 
