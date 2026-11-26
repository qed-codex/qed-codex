---
{
  "module": "OAI/Computability/VPVNP/EvaluatorScheduleBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorScheduleBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorScheduleBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Time allowance for native radix conversion and the chronological scheduler

The clock includes the initial reversal of the RAM's exponent array, the
restoring divisions that prepare all digit rows, and the two nested tally
loops. For fixed field, label count and callback allowances it is quadratic
in the input exponent width. Polynomial growth of the callback allowances in
that width is also permitted.


### `scheduleBudget`

 Exact deterministic preparation time followed by the scheduler's reserved
clock. The two callback allowances cover one label and one Frobenius query. 

### `coefficient`

 A polynomial multiplier independent of the exponent width. 

### `scheduleBudget_le`

 Uniform in the exponent words and the chosen sequence of matrix indices. 

### `scheduleBudget_le_exp_poly`

 When all fixed parameters are at most `2^a` and callbacks take at most
`2^a * (Z+1)^k`, the coefficient stays singly exponential in `a` and the
degree in `Z` grows by at most two. The same `a` and `k` may be used across
any collection of fields, dimensions or advice parameters with those bounds. 
