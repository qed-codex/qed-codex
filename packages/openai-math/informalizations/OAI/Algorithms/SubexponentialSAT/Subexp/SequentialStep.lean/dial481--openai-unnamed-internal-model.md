---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SequentialStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SequentialStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SequentialStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete composition of score selection and packed assignment update. 

### `selectAndUpdate_eval`

 The concrete selection/update code needs only a prepared score stream;
every following operation is an actual fixed machine subroutine. 

### `ScoreBuilderRefines`

 The remaining integration boundary is a real execution of the supplied
fixed score-stream program. It preserves the assignment and controller ports
while writing one framed unary score per candidate to stack zero. 

### `program_of_scoreBuilder`

 The complete controller cost is polynomial once the actual fixed score
builder has its bounded execution theorem. All selection and update costs are
already included in the explicit selectionBudget polynomial. 

### `initialData`

 The controller's input encoding: packed alphabet and initial assignment,
unary width and remaining count, and a separate runtime environment. 

### `naturalValues_program`

 Specialization to the actual local natural-number scores. The output is
exactly the encoded word list defining naturalAssignment/computedAssignment. 
