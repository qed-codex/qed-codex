---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticResidual.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticResidual.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/AsymptoticResidual.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform transport from the original dimension to a residual dimension
between one half and all of it. No lower bound on arbitrary residuals is
assumed: callers must supply the displayed half-dimension condition. 

### `eventually_uniform_half`

 Eventual assertions are uniform over every residual dimension in the
half interval; in particular the residual may depend on a branch. 

### `eventually_residual_polynomial`

 A fixed polynomial bound in the original logarithm is still a fixed
polynomial bound in every half-size residual logarithm. 
