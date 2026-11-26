---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed control for the universal-block finite search

The commands in this file scan runtime framed lists. Their finite control
depends on the supplied finite predicate program and fixed ports, never on
the block dimension, field size, or list lengths. Predicate specifications
are measured `StructuredCalls.Eval` contracts for actual finite code.


### `negateResult`

 Negate the predicate-result register using two actual instructions. 

### `allCommand_eval`

 A real short-circuiting universal quantifier over encoded records. 

### `anyCommand_eval`

 The existential quantifier uses the same measured framed-list iterator. 

### `selected_of_visits`

 The semantic history identifies the successful record stored by a concrete
predicate callback. It does not assume a truth oracle or a chosen witness. 

### `searchCommand_eval`

 First-success control, with an actual stored successful payload. 

### `SavedPorts`

 The saved enumeration is copied for each quantifier invocation. 

### `savedAllCommand_eval`

 Repeated universal scans preserve the saved enumeration and consume their
working source even when a failed predicate stops the scan early. 

 A full-dimensional candidate needs only universal scalar tests. 

### `coefficientTest`

 Two concrete matrix-vector products and three zero comparisons suffice
for one coefficient tuple. 

### `fullPairTest`

 An equivalent complete finite checker that replaces the nested spanning
search by injectivity between spaces of the same dimension. 

### `framedCode`

 A scalar frame is itself a fixed-width injective token for the tuple
generator. Its payload still uses the supplied field-word representation. 

### `coefficientRecords_all_iff`

 Every actual generated coefficient payload is tested, with exactly the
same truth condition as quantifying over the two coefficient spaces. 
