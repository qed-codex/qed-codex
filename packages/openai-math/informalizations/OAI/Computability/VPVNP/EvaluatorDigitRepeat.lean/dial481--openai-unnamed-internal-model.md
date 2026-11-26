---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitRepeat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitRepeat.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitRepeat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Repetition by a binary field digit

The evaluator multiplies by one label as many times as specified by its
current base-`Q` digit. Its finite control decrements a little-endian bit
stack, using a second stack to save the trailing zeros. A positive digit
decreases by one before calling the matrix-step routine. The two digit
stacks together occupy at most the width of the digit throughout the scan.


### `State`

 Finite control for decrementing a binary digit, restoring the digit stack and invoking the
scheduled callback once per decrement. 

### `repeatRoutine`

 The callback returns to the scan for the next unit of the digit. 

### `frame`

 Assign both digit stacks while carrying all other registers through. 

### `count_zero`

 On a zero digit the control returns directly to the continuation. 

### `count_positive`

 A positive digit with `l` trailing zeros costs `4*l+3` control instructions
before entering the callback on the decremented digit. This equality retains
every nondeterministic branch of the callback. 

### `value_decrement`

 The positive branch implements subtraction of one, at the same bit width. 
