---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsSquarefree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsSquarefree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsSquarefree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact coefficient extraction in the Boolean squarefree algebra, including
both formal scalar variables. No total-degree truncation is substituted for
support union. The final U coefficient sum is only an additive operation. 

### `squarefree_eval_eq_sum`

 Retaining a finite superset of the actual support preserves evaluation. 

### `SquarefreeJet`

 U is outermost, Z next, and Boolean squarefree X coefficients innermost. 

### `sumUCoeff`

 Sum the retained U coefficients, after the complete head moment product. 

### `squarefree_head_moments`

 The concrete U/Z/squarefree head identity. `hweight` is supplied by the
actual coordinate partition, and `hbounded` by positive-Z support control. 

### `squarefree_head_moments_coeff`

 Only the coefficient currently being extracted needs its support bound. 

### `squarefree_head_moments_trunc`

 The actual retained U/Z computation only enumerates supports of size <J.
Admissibility of the untruncated factors proves this bound at every stage. 
