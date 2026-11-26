---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `controller_lower`

 The explicit old controller pays every scored candidate, independently of
whether the candidate wins. 

### `rounds_le_square`

 All actual seed and streamed candidate attempts are paid. The retained
payload count can be exponentially large, but appears only in time. 

### `attempt_polynomial`

 Paid preparation, every marked query, and full score padding have a fixed
polynomial overhead in retained parameters and the uniform query cost. 

### `attemptBudget_polynomial`

 The named actual attempt includes the all-mark mass collector and the
common-width score padding after the native normalizer. 

### `family_square_le_polynomial`

 The old explicit family-generation term alone dominates the square of
its original ternary candidate count. 

### `rounds_le_polynomial`

 Replacing materialized candidates by the complete binary stream costs a
fixed square of the old worst-case budget. No successful-run time is used. 

### `actual_rounds_le_fifth_power`

 Complete actual attempts, including all marked queries and padding,
fit a fixed fifth power of the old explicit controller budget and input
parameters. The power is independent of every runtime input. 

### `linear_budget_substitute`

 A fixed power substitution into a nonnegative linear measured cost stays
a fixed power, including a zero loop coefficient. 

### `polynomialBudget_affine`

 The original explicit hash budget is affine in its paid mass-query cost. 

### `polynomialBudget_substitute`

 A fixed polynomial increase in the per-query measured cost can be charged
inside the original explicit hash budget without an input-dependent power. 

### `linear_budget_substitute_with_input`

 A fixed power substitution into a nonnegative linear measured cost stays
a fixed power, including a zero loop coefficient. 

### `polynomialBudget_substitute_with_input`

 A fixed polynomial increase in the per-query measured cost can be charged
inside the original explicit hash budget without an input-dependent power. 

### `attempt_with_staging_polynomial`

 The actual staging and cleanup bound is linear in the retained entry
cap, so it fits the same fixed cube as the normalizer and marked mass. 

### `staged_rounds_le_fifth_power`

 Paid staging, complete marked mass, padding and final cleanup
fit a fixed fifth power of the old explicit controller budget and input
parameters. The power is independent of every runtime input. 

### `named_staged_rounds_le_fifth_power`

 The measured budget belongs to the actual normalize, stage, marked-mass,
cleanup and padding command, not an unstaged query service. 

### `staged_rounds_space_le`

 The actual staged selector retains polynomial space independently of all
candidate and round counts; only the separately proved query prefix cap appears. 

### `originalBudget_le_polynomial`

 Every old explicit setup/controller term is a fixed polynomial of the
actual retained scalar and word bounds, candidate count, and paid query cost. 

### `family_le_hashCalls`

 The candidate factor in the real explicit budget is bounded by the old
all-trial/all-mark call counter, for its exact ternary alphabet and depth. 

### `canonical_originalBudget_le`

 The numerical representative of the unary round counter is canonical
binary; its value and length are both charged, without reading the unary
word as a binary number. 
