---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyUniform.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyUniform.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyUniform.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform bounds over every input at a fixed size.  The cutoff depends only
on fixed numerical exponents, never on a chosen sequence of formulas. 

### `linear_jet_envelope_with_neutrals`

 Include up to n additional neutral factors in the literal jet-order
parameter.  They need not be removed from that parameter by the evaluator. 

### `Bounds`

 All input-dependent premises are pointwise.  None is hidden in the
threshold used by `eventually_assembledWork_bound`. 

### `eventually_assembledWork_bound`

 A single threshold works for every resource record, hence every formula
and every retained-half branch satisfying the displayed numerical estimates.
Small inputs are deliberately left to the actual finite-fallback machine. 

### `nativeEnvelope`

 Explicit closure for native algorithms that are polynomial in the
assembled counter.  In particular quadratic bucket grouping pays for its
second factor of `2^headSize` here, never inside a polynomial in n. 
