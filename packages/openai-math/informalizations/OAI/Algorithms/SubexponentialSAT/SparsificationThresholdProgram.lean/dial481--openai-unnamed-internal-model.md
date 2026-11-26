---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SparsificationThresholdProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationThresholdProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationThresholdProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed arithmetic expressions for the sparsification thresholds

The clause width is fixed before the input is read. Thus the recurrence is
compiled to a finite arithmetic expression; its variables are encoded word
data. No expression size or control table depends on M or the inverse budget.


### `powerExpr`

 A fixed exponent is compiled by finite repetition of multiplication. 

### `cumulativeExpr`

 The cumulative insertion constants, expressed using one input word M. 

### `degreeExpr`

 The per-literal degree cap at one width, including the unit-width case. 

### `occurrenceExpr`

 The complete occurrence bound B=2*sum L_j. 

### `programFor`

 A fixed expression is compiled into a fixed finite Boolean program. 

### `programFor_correct`

 The original input remains available; the output and scratch layout is
exact, and both cost and raw output length are bounded for padded inputs. 
