---
{
  "module": "OAI/Computability/VPVNP/EvaluatorChronologicalSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorChronologicalSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorChronologicalSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Storage and stopping bounds for both evaluator cursors

The table, index tallies, and callback registers account for the storage
between calls. Address lookup and initialization use polynomial scratch
space. The binary digit can trigger many callbacks without increasing the
cursor storage between them.


### `bankSpace`

 Maximum length of a single stack between callbacks. 

### `schedulerSpace`

 A polynomial allowance for addressing, fetching, and both cursor loops. 

### `stackFits`

 The storage condition that every named evaluator stack has length at most the given limit. 

### `column_bounded`

 The unary copy that starts a column and the subsequent label scan respect
the same space bound as the supplied matrix callbacks. 

### `traverse_bounded`

 Every branch of the complete nested traversal respects the clock and peak
storage, including branches that reject within a matrix query. 
