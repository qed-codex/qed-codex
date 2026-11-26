---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseBudgetProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseBudgetProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseBudgetProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


Concrete finite-control construction of the Appendix A dyadic search.
The input budget is `1 / s`; the search uses only exact binary arithmetic.
This file separates command construction from theorems about its execution.


### `replaceCmd`

 The temporary is emptied before returning; the destination may be an operand. 

### `hornerStep`

 One Horner step for `sum (3*M)^j`, using data 12 for `3*M` and data 5 for one. 

### `horner_eval`

 Horner's recurrence is unrolled in the finite control. The summation below
counts its actual arithmetic traces, with no unit-cost natural multiplication. 

### `budgetTest`

 Computes `clog 2 (4*C*M)`, multiplies by Gamma and s, and tests `M < Gamma*h*s`.
Horner evaluation and all arithmetic are finite binary programs. 

### `budgetTest_eval`

 Exact execution of the expensive test, including its arithmetic costs and cleanup. 

### `test`

 First test the constant lower bound; the expensive logarithm is evaluated only
when `M >= Gamma`. Both branches return with every temporary word empty. 

### `loop_eval`

 Termination follows from the proved first-passing index; every loop iteration
is an actual doubling trace followed by the concrete test trace. 

### `initCmd`

 These constants are part of the fixed instruction table chosen from k. 

### `search`

 The actual dyadic search. The natural-number minimizer appears only in its
specification, never as a machine instruction or a supplied runtime service. 

### `searchCost_polynomial`

 Constants are chosen before the binary input. This is polynomial in encoding
length, not in the integer represented by the input word. 

### `boundPowers`

 Fixed-k multiplication computes the safe occurrence bound `4*M^(k-1)`. 

### `command_eval`

 The two parameter words are returned in ports one and two; the input in port
zero is preserved for the calling algorithm. All remaining 29 stacks are empty. 

### `program_execution`

 One finite Boolean/stack instruction table is chosen from k before the input.
The returned configuration exposes both full parameter words for the caller. 

### `program_execution_space`

 The polynomial-time local parameter search has polynomial storage at every
source prefix, including every arithmetic temporary and every one of its stacks. 
