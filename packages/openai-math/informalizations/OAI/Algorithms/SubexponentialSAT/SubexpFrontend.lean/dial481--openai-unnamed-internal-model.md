---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFrontend.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFrontend.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFrontend.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Syntactic frontend for the variable-parameter SAT algorithm

The external input declares `n` Boolean coordinates. We first normalize the
finite CNF, then enumerate only its syntactically appearing coordinates in
increasing order. The resulting coordinate set is retained through all later
branching; this frontend is not reapplied at sparsification leaves.

All constructions inspect finite syntax. No satisfiability test, choice of a
satisfying assignment, or noncomputable enumeration is used by `prepare`.


### `allLiterals`

 Explicit finite universe of signed literals, including the empty-variable case. 

### `pullClause`

 Pull a clause back along a variable map by scanning the finite new literal universe. 

### `appearing`

 The variables appearing in an explicit finite formula. 

### `activeEquiv`

 Increasing enumeration, implemented by finite sorting and index lookup. 

### `compress`

 Dense renaming, without another semantic simplification. 

### `eval_compress`

 Evaluation commutes with the inverse coordinate map. 

### `extendAssignment`

 Extend an assignment to the old declared coordinates, setting unused ones false. 

### `numVariables`

 The number of coordinates retained by the actual frontend. 

### `prepare`

 Canonical preprocessing. The first component is the post-normalization
appearing-variable count, not the possibly larger declared input count. 

### `prepareCode`

 No answer bits are attached: the prepared input is exactly the existing
canonical structural encoding. 

### `prepareNumbers`

 Signed literal codes are `2 * index + polarity`, matching the parser and
finite-list sparsifier interface. 

### `codeTruth`

 Executable semantics for the existing signed natural-number literal code. 

### `negateCode`

 Flip the polarity bit, retaining the variable index. 

### `RetainedCNF`

 Later sparsification leaves use this fixed coordinate type, even if some
coordinates stop appearing. It deliberately does not recompute `numVariables`. 

### `shortcut`

 Direct syntactic exits: reject an empty clause, accept an empty formula. 

### `prepareCode_length_le`

 The actual output encoding is bounded by a fixed polynomial in input
length and width. This is a length bound, not a machine runtime claim. 

### `prepareCode_length_quadratic`

 Standard polynomial-overhead shape for composition with the solver's
input-length bound: coefficient `8*k+8` and fixed degree two. 

### `prepareCode_stack`

 Raw Boolean program input is already a width-one stack encoding. 
