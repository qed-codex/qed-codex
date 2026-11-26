---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact fixed-high query count for the code-derived shared-order target. 

### `violates`

 Empty clauses have violation one, as in the actual clause interpreter. 

### `queryPolynomial_origin`

 Local idempotent correctness is required only at the source value. The
  shared truncation is discharged here by nilpotent divisibility. 

### `computedDigits`

 The digits here are exactly the finite Newton program's returned array. 
