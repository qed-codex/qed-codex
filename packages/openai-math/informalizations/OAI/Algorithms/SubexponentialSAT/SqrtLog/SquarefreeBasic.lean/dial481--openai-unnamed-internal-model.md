---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Sparse squarefree polynomials. The index monoid multiplies by support union,
so the coefficient algebra imposes X_v^2 = X_v without enumerating all supports. 

### `Support`

 A type tag prevents the support-union multiplication leaking to all finsets. 

### `evalHom`

 Evaluation at idempotent values is a ring/semiring homomorphism. 

### `Bounded`

 A support-cardinality bound, with no finiteness assumption on the ambient variables. 
