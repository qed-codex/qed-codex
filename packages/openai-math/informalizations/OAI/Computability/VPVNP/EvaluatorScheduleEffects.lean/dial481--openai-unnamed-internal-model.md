---
{
  "module": "OAI/Computability/VPVNP/EvaluatorScheduleEffects.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorScheduleEffects.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorScheduleEffects.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting the matrix steps of the nested digit loops

The machine loops over increasing column and label indices. Its table
starts with the most significant base digit, so column `j` selects power
`Z - 1 - j`. In each column the machine first chooses an index for a
Frobenius step, then chooses one index per repetition of each label. The
finite sums of these branches are exactly the chronological continuation
effects of the digit program.


### `digitAt`

 Value at the machine's row and column indices. The stack supplies a
natural row number, so this definition also covers an out-of-range row. 

### `digitAt_table`

 The unary offset selected by the machine yields the exact multiplicity
for its binary repetition routine. 

### `cellEffect`

 Summation over every index trace emitted by one binary repetition count. 

### `columnEffect`

 One column begins with Frobenius, followed by the repeated label steps
in order of increasing label number. 

### `schedulerEffect`

 Continuation effect of the entire nested machine schedule. 

### `actionCode`

 Physical action number used by the matrix query callback. 

### `columnEffect_eq_emit`

 The fixed loop for a column has the same multiplicities and ordering as
the Frobenius and label actions of `emit`. 

### `schedulerEffect_eq_actions`

 All branch choices of the nested range loops have exactly the same
effect as the chronological action list, for any index update and continuation. 

### `schedulerEffect_eq_actionCount`

 Interpret the physical scheduler's continuation in the counted action
program of `EvaluatorStreamCount`. The interpretation may include fuel and
stack encoding, so the action count may charge a different delay on each
chosen index. 

### `schedulerEffect_eq_digitProgram`

 An implementation of the linear-map effect on all valid action codes
therefore realizes the concrete linear-map list of the algebra evaluator. 
