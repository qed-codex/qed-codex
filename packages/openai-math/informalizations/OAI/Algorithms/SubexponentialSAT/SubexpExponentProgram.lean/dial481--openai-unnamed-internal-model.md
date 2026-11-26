---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpExponentProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpExponentProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpExponentProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite Boolean programs for exponent keys

The key adder below has one fixed sixteen-instruction table.  Its two input
words contain unary-delimited exponents; a third input is a unary output-width
counter.  Each round consumes one counter bit and emits one result bit.  Once
the source adder has ended, further rounds emit zero padding.  It therefore
implements truncation and padding without interpreting a dimension as control
code, and without converting an exponent to an unbounded machine register.


### `padTake`

 Prefix of a word, padded by false bits to exactly the requested width. 

### `Advance`

 One semantic round, used only to state the refinement of the instruction
table.  All four actions below are implemented by literal stack instructions. 

### `Result`

 Exact result and instruction count of the width-controlled rounds. 

### `keyAddProgram`

 Stack 0: left input; 1: right input; 2: width counter; 3: reversed output.
Both registers are scratch bits.  The table is independent of every input. 

### `keyAdd_trace`

 Exact execution of the concrete table, including its final halt. 

### `keyAdd_runsIn`

 Uniform linear instruction bound; arbitrary accumulator contents survive. 

### `normalizedBits_fixedKey`

 The retained input bounds ensure the full product key fits the output
width; normalization therefore loses no coordinate or U/Z exponent. 

### `keyAdd_primitive`

 Refinement all the way to primitive stack-machine transitions.  The
compiler overhead is a constant of the single sixteen-instruction table. 
