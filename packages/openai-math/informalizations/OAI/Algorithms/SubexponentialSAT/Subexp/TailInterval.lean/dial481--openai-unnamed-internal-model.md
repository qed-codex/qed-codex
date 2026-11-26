---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/TailInterval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/TailInterval.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/TailInterval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A computable centered interval for the multicolor binomial tail

The swap mean is between (Q - 1) / 4 and (Q - 1) / 2.  Taking the natural
floor of mean - R / 2 gives an interval of R consecutive integer weights.
The rounding error is at most one, absorbed by R ≥ 4.


### `mean`

 The mean of the Q - 1 independent swap signs. 

### `centeredStart`

 A rational-floor computation, with no choice or search oracle. 

### `intervalStart`

 The concrete interval start used for the multicolor matrix. 

### `centeredStart_deviation`

 The floor rounding error preserves distance at least R / 4 outside
the interval.  This holds for every natural weight, not just weights ≤ Q - 1. 

### `intervalStart_end_le`

 The interval fits within the available weights 0,...,Q-1. 

### `intervalStart_deviation`

 Required geometric hypothesis for the exact swap-probability tail bound. 

### `interval_contains_near_mean`

 Every integer weight within R / 4 of the mean belongs to the chosen interval. 

### `exists_interval`

 A fully explicit interval, including its endpoint and geometric guarantees. 

### `interval_tail_bound`

 The numeric budget now implies the tail estimate without an additional
interval-location hypothesis.  The probability argument is reused verbatim. 
