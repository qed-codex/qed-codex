---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The compact digit schedule of the finite-algebra evaluator

After radix conversion, each column contains one base-`Q` digit for every
label. Processing the columns most significant first produces the same list of
linear maps as the paper's monomial program. Each column starts with a
Frobenius step, then repeats label multiplication according to the binary
counter on that label.


### `Action`

 The two types of matrix queries made by the monomial evaluator. 

### `emit`

 Actions emitted by the digit counters at one position. 

### `columns`

 A compact schedule of digit columns, before expanding any multiplicities. 

### `columns_eq`

 The radix conversion may also compute each column by its position,
using one fixed order for the input labels. 

### `columns_digit_lt`

 Every digit lies below the cardinality of the base field. 

### `actionMap`

 Interpret the streamed query identifier as a linear operator. 

### `actions_eq_digitProgram`

 A column-by-column streaming traversal produces the precise chronological
sequence of Frobenius and multiplication queries in equation (8.2). 

### `action_count_le`

 A compact schedule uses `w*t` digits, and executes at most one Frobenius
and `t*(Q-1)` label multiplications per column. 
