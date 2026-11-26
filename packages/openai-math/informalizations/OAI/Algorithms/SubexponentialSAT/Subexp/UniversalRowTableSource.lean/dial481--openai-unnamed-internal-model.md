---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowTableSource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowTableSource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowTableSource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexed cache tables and the represented interpolation row

The physical producer reads natural-number indexed lists. This adapter
identifies those reads with the finite-indexed row specification, including
the mismatch filter and the cardinality guard. Its premises concern only
individual input cache entries, the delta word, and the limit's length.


### `row_eq`

 The actual count guard and filtered natural-index reads produce the
same row record as the finite-indexed represented construction. 

### `row_eval`

 Decoding the physical row record gives the full represented row
polynomial. Only local input-cache and scalar-decoder laws are assumed. 

### `map_factors_eq`

 Individual cache words may use any valid representation of their
scalars. No equality of the raw representatives is needed. 

### `row_eval_of_decode`

 A scalar-by-scalar decoder refinement suffices for the full polynomial.
The concrete input words need not equal a separately generated canonical
representative of the same field element. 
