---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriorityPrimitives.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriorityPrimitives.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparsePriorityPrimitives.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete record-count and emission primitives extracted from supplied sources.
No sparsification schedule or formula evaluator is imported. Provenance is recorded
in verification/counting-draft/worker04/extraction.json. 

### `toBinary_eval`

 Convert an input-sized unary record count to binary. The cost comes from
the actual header parser and dynamic binary length counter. 

### `numericEq_eval`

 Numeric equality tolerates leading zero padding in the supplied bound.
Both comparisons consume only real copies of the preserved operands. 

### `countTest_eval`

 Count the actual records, convert the count, compare it with a supplied
binary word, and clear every temporary. Only the scanned input is consumed. 

### `literalService`

 The first seven labels are the actual relocated frame parser. The remaining
labels rebuild the escaped payload from its reverse and add the list cons tag. 

### `escapeBits`

 Escaped data without the final false delimiter. 

### `emitRecordProgram`

 Enter the proved frame writer directly at its fixed encoding entry. 

### `emitIfSelected_eval`

 An actual measured branch: the kept record is encoded, and an omitted
record is consumed. Both paths leave the callback ready for the next record. 
