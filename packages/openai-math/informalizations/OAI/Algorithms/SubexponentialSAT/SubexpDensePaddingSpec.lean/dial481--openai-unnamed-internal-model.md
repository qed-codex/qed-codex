---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDensePaddingSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDensePaddingSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDensePaddingSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-width bit padding and dense polynomial coefficients

The literal loader pads or truncates a flat payload to a whole number of
coefficient cells. This file identifies that operation at the cell level.
Preservation of a complete polynomial requires its degree to be below the
number of retained cells; this condition is explicit before any Taylor shift.


### `padTo_flatten`

 The actual bit-loader operation agrees with truncation/padding of whole
coefficient cells, including zero-width and empty-input cases. 

### `padTo_encoded`

 Specialization to an arbitrary fixed-width coefficient encoding. 

### `denote_padCells_of_degree_lt`

 A full-row denotation is preserved only after the retained cell count
has been shown to exceed the complete row's degree. 

### `evalWith`

 Value-level execution with the same literal/add/multiply operations that
the postfix services refine. No denotation function is used during execution. 

### `evalWith_correct`

 Truncated arithmetic is sound even if intermediate expressions have
higher degree than the final row. The local invariant can be fixed cell
length, so arithmetic laws are needed only on well-formed operands. 

### `evalWith_full_row`

 The final degree bound restores the full row, without a degree bound on
every intermediate product and without commuting the residue section with
field arithmetic. Coefficientwise lifting follows this theorem. 
