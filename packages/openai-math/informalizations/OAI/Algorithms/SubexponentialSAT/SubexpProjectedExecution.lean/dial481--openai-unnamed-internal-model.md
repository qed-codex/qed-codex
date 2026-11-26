---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpProjectedExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpProjectedExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpProjectedExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Projected postfix execution

The compiled source contains the original raw literals. Each complete push
calls the finite projection table; the resulting value is therefore
`(e.map project).eval`. The induction tracks the entire remaining source and
operand list, and charges actual service trace bounds at every node.


### `LoadImplements`

 A unary load is implemented by actual instructions on the top framed
operand. The rest of the operand stack and arithmetic context are preserved. 

### `ImplementsOn`

 Binary services are required only on values produced by projection and
previous arithmetic. Raw literal keys need not satisfy this predicate. 

### `Validity`

 Pure closure facts for the values accepted by the arithmetic tables. 

### `exprCost`

 Interpreter cost includes original literal byte length, its projection,
and the dispatcher overhead on both binary operations. 

### `compile_runsIn`

 Every source literal is projected, including a single-literal expression.
All source suffix bytes, lower operands, and fixed context are unchanged. 

### `complete_runsIn`

 Complete execution initializes the list marker and ends after the real EOF
halt. The final singleton contains the evaluation of projected literals. 
