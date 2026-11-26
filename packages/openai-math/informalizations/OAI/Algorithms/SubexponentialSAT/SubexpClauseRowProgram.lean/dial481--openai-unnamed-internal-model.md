---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpClauseRowProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpClauseRowProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpClauseRowProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# An actual clause-row program

The input clause uses `Encoding.encodeList Encoding.encodeNat`. The stored
assignment is an explicit word of the declared length, one bit per variable.
The program parses each literal, decodes its unary index and polarity, performs
a preserving indexed read, and accumulates the disjunction. No semantic test is
an instruction. All auxiliary ports and all input requirements are explicit.


### `tapes`

 Array 0; temporary value 1; unary index 2; width 3; array scratch 4--7;
clause source 8; reversed literal payload 9. 

### `program`

 Each pair of unary payload bits adds one bit to the index counter. An odd
last bit is the positive-polarity flag. The leading reversed delimiter is consumed. 

### `trace`

 Exact trace from the reversed canonical natural payload to a unary index
and Boolean polarity. All assignment, clause, and accumulator data are preserved. 

### `recordPorts`

 The parser uses only value/present and preserves sign and disjunction. 

### `readBit`

 Persistent single-bit indexed read, with the index represented by its
unary length. The complete source word is restored by the actual array code. 

### `combine`

 One real pop and four Boolean register operations combine a looked-up
variable value with its polarity and the current disjunction. 

### `literal_eval`

 Full literal pipeline: framed bytes to index and polarity, then an actual
restoring array lookup and Boolean evaluation. 

### `row_loop_eval`

 Every input literal is visited; the loop cost includes each actual branch.
The complete stored assignment is preserved through all indexed reads. 

### `command`

 The fixed command prepares its width counter, traverses the clause, and
emits exactly one Boolean result. The assignment and trailing source are framed. 

### `trace`

 A complete finite instruction trace, including halt. 

### `clause_trace`

 In particular the exact finite-set clause semantics is computed, even if
the supplied literal list has duplicates. 

### `rowCost_le`

 The bound is polynomial in the explicit declared variable count and
number of input literal records, including unary index parsing and lookup. 

### `control_size`

 The whole evaluator has fixed control independently of `n`, clause size,
and the values of its literal indices. 

### `wordAssignment`

 Interpret an explicit word of the declared length as an assignment. 

### `eval_word`

 Convenient execution contract for an already materialized assignment word.
The four caller register values are unrestricted. 

### `factor_trace`

 The fully indexed row program computes the actual constructed clause
factor on valid encoded chunk labels. Its input assignment is the materialized
concatenation specified by `positions`; building that word is a separate trace. 
