---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `sparse_clause_size_le`

 Sparse clauses have only logarithmic binary length. The upper bound here
is intentionally elementary; it is enough for the linear precision budget. 

### `linear_jet_envelope`

 This includes a trial row and a marked clause. With the actual loop cap,
a conservative fixed coefficient 30 bounds the jet's precision/factor term. 
