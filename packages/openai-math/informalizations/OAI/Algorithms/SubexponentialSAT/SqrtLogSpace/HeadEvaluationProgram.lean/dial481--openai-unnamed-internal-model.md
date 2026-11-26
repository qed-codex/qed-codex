---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadEvaluationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadEvaluationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadEvaluationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete correction-mask checking for a head rescan. This local routine
preserves its input masters and charges every stack at every source prefix. 

### `correction_scan`

 The correction test is an actual fixed bit program; the whole prefix
storage bound is polynomial in the ambient assignment and scalar word sizes. 

### `command_eval`

 An actual preserving Boolean correction test. Its result is a Boolean
register, so the following conditional does not inspect a coefficient low bit. 

### `command`

 Every candidate pays for the complete key comparison and correction scan.
Only the final Boolean register selects whether its factor value is added. 

### `budget_signature_le`

 Both losing and successful candidates satisfy the same fixed polynomial
bound, including every full raw matrix row and both complete signature words. 

### `run_space`

 The complete key, E mask and head mask are tested by a fixed actual
program. Every temporary is cleared before the next candidate is visited. 

### `flag_exact_iff`

 Byte equality is exactly equality of the full integer signature, and the
other Boolean conjunct is exactly the original-coordinate correction test. 

### `command_eval`

 The concrete leaf-ABI wrapper reads cursor859 and persistent metadata864..868,
clears its low scratch bank, and preserves every stack of the caller. 

### `run_space`

 One actual fixed program tests a cursor without changing any caller stack.
Its all-prefix bound includes the entire persistent query state. 

### `run_space_frame`

 One actual fixed program tests a cursor without changing any caller stack.
Its all-prefix bound includes the entire persistent query state. 

### `gatePolynomial`

 A fixed degree-six polynomial charges the full raw matrix and key words. 

### `budget_uniform`

 Uniform over every candidate, including losing checks. The desired key
may be any retained word; the current complete integer key is computed and charged. 

### `gatePolynomial_le`

 A simple monomial envelope with a degree independent of every input. 

### `bodyBudget_uniform`

 Every candidate, successful or losing, is charged within one fixed
polynomial plus the separately charged accepted factor calculation. 

### `command_space`

 The staging and cleanup copy tables preserve the caller envelope exactly;
only the local32 computation needs the separate polynomial allowance. 
