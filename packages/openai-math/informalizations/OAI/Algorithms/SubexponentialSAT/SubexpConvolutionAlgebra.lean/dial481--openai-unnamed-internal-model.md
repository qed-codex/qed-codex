---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionAlgebra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionAlgebra.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionAlgebra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Polynomial semantics of the triangular update schedule used by the
actual convolution controller. This file assigns no execution costs. 

### `run_denote`

 The actual schedule computes the degree-below-D part of the product,
with exactly D stored coefficients, including trailing zeros. 

### `prepared_run_correct`

 The generic refinement specializes to the concrete prepared binary
quartic operations used by the machine controller. 
