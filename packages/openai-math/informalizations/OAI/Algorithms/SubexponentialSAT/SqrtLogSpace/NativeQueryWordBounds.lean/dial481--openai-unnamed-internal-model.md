---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQueryWordBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQueryWordBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQueryWordBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The authentic factor specification inherits its row and clause bounds
from the actual physical formula, row-stream and width words. These are
length bounds, so they remain valid with leading zeros and repeated entries. 

### `rowBits_length`

 Each stored selector term occupies exactly the fixed positive bit width. 

### `row_length_le_stream`

 An actual row, including repetitions and zero coefficients, is paid for
by its physical framed input stream. 

### `source_clause_length`

 Every original clause is bounded by its actual two-level formula bytes. 

### `marked_clause_length`

 The optional marked clause has the same bound even for an absent mark. 

### `weighted_width`

 Integer lifting assigns a weight to each original clause without
changing its literal list. 

### `spec_words`

 The only physical premises are the three immutable source words. 

### `produced_words`

 These are the row, marked-clause and width bounds for the genuine
produced ring and addressed native-input factor, with no new source service. 

### `produced_weighted_width`

 If the original CNF has width k, the same genuine weighted rows keep
that width; no tuple multiplicity or finite-ring coefficient changes it. 
