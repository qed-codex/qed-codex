---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Sharp storage bounds for binary head-assignment controllers. Only the
counter's retained word length enters the local controller budget; every other
caller stack retains the same envelope throughout arbitrarily many visits. 

### `ripple_space`

 Increment and decrement use only a two-stack local footprint. 

### `zero_space`

 The restoring zero test has the same bound independently of its counter value. 

### `test_space`

 Adding the one Boolean negation changes no stack. 

### `advance_space`

 The complete countdown transition preserves one caller envelope. 

### `visits_space_next`

 Every binary-counted visit keeps one fixed bound, including caller frames.
Only the counter word width enters the controller-local side condition. 

### `for_space_next`

 The initial restoring test and final halt preserve the same bound too. 

### `head_program_resources`

 The actual head loop scans all `2^h` assignments with a fixed polynomial
per-visit cost, while its binary fuel retains exactly `h+1` bits. The concrete
accepted-factor command must instantiate the measured body proof. 

### `head_fold_resources`

 Exact accumulator fold and all-prefix storage refer to the same head run. 

### `body_space`

 Sharp composition of the actual gate, selected factor computation and
cursor increment. The concrete gate and accepted command supply local prefix
proofs; retained caller words never enter a summed-data estimate. 

### `seed_power_space`

 Constructing exponential fuel scans its linear-width witness and retains
one unchanged caller envelope. 

### `seed_space`

 The complete actual seed preserves one stack envelope, including an old
accumulator which is cleared by real instructions. 

### `body_space_gate`

 The native staged full-key/correction gate discharges the gate part of
the per-assignment resource contract. 

### `scan_fold_resources`

 Paid seed, all head assignments, and actual controller reclamation are
bounded on one trace. Initialization does not retain an assignment family. 

### `scan_resources`

 Relational dictionary invariants pass through the actual complete scan.
The invariant may contain existential representations and decoded partial sums;
no canonical executable evaluator is assumed. 

### `scan_budget_le`

 The complete scan cost is a fixed polynomial factor times `2^h`. 
