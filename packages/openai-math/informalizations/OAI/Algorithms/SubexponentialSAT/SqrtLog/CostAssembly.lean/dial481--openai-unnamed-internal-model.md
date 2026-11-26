---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Numerical assembly of the sparse-query costs.  `sparseWork` is an explicit
natural-valued upper cost, not a running-time oracle. Connecting an executable
program to these counters and charging coefficient arithmetic are separate
machine-refinement obligations. 

### `sparseWork`

 All resource counters remain visible. `ordinary` contains the fixed
polynomial work outside support enumeration; `bits` charges primitive
arithmetic. `calls` includes unsuccessful hash candidates and marked counts. 

### `eventually_polynomial_target`

 Fixed polynomial overhead in n is negligible at the target scale. 

### `eventually_counter_target`

 A polynomial-log exponent gives a full exponential cost bound. 

### `high_branch_exponent_le`

 A high-incidence branching exponent n/sqrt(L) costs at most a fixed
multiple of the requested runtime exponent. 

### `sparseWork_le`

 Pointwise assembly. The factor 17 charges the +1 support and the separate
setup. Every exponent is a constant coefficient of the same target scale. 

### `sparseWork_target`

 The explicit cost has a global C*2^(A*runtimeScale) bound once its exact
setup/query counters have polylogarithmic logarithms, its ordinary bit work is
polynomial, and its head/branch exponents satisfy the numerical budgets.
Only finitely many small inputs are absorbed by C. 
