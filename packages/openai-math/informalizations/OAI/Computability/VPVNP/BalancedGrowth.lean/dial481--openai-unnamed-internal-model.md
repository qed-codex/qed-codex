---
{
  "module": "OAI/Computability/VPVNP/BalancedGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedGrowth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Comparing the exponential growth of finitely many balanced cuts

In Section 4.2 each cut contributes a fixed multiplicative factor times an
exponential in the tensor-power index. Strictly smaller exponents make their
sum negligible compared with the lower bound for the full tensor power.


### `tendsto_weighted_pow_ratio`

 After division by the target power, the finite sum tends to zero. 

### `eventually_weighted_pow_lt`

 At every sufficiently large power the total cut contribution is less than any
fixed positive fraction of the target power. 

### `eventually_weighted_pow_lt_target`

 Strict comparison with the target, in terms of the spectral values themselves. 

### `balancedGrowth_threshold`

 A fixed finite collection of cuts whose base-two exponents are all strictly
smaller than `L` cannot account for growth of `(2 ^ L) ^ h` at unbounded powers. 
