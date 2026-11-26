---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SparsificationConstants.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationConstants.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationConstants.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The constants in the sparsification argument

The definitions below follow Appendix A.3. The polynomial growth bound is an
explicit existential bound by a natural monomial. It is independent of the
formula size. The final admissibility predicate uses only decidable natural
arithmetic, so it can be fed to an effective least-number search.


### `C`

 Cumulative insertion constant through width j. 

### `L`

 The per-literal occurrence bound at width j. Width zero is unused. 

### `z`

 The chosen sunflower threshold at width d ≥ 2. 

### `occurrenceCap`

 Final per-variable clause-occurrence cap. The width-zero summand is zero. 

### `cumulative_insertions_le_bounded`

 The finite-width version needs charging inequalities only through j. 

### `cumulative_insertions_le`

 Equation (A.1) implies the cumulative insertion bound. The zero-width
count is zero; the sum includes it to match the charging interface. 

### `B_choices_mul_le`

 The integral per-width B-choice bound from the cumulative insertion budget. 

### `B_choices_sum_mul_le`

 Summing the per-width budgets retains an integral total-choice bound. 

### `PolynomialBound`

 Both witnesses depend only on the fixed function, never on M. 

### `PolynomialBound.eventually_le_two_pow`

 Fixed polynomial growth is eventually bounded by two to the M. 

### `Admissible`

 Decidable form of the threshold constraints, including (A.2). 

### `Admissible.log_budget`

 The integral predicate implies the natural-log form used by tree counting. 

### `chooseM`

 A decidable, terminating least-parameter search with no input-size argument. 

### `chooseM_finite_execution`

 The least-number search has a finite execution by the explicit Boolean scan.
The bound counts predicate calls, not bit operations. 
