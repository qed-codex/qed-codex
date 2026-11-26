---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source lookup starts with the actual canonical CNF body, rather than an
externally supplied table of already expanded hash clauses. 

### `fetch_serialized_runs`

 Mapping here describes the source serialization; it is not a machine
preprocessing step. The lookup scans the supplied original bytes. 

### `fetch_cnf_runs`

 The returned literal-code list is precisely the indexed original clause
of the canonical input, and the complete original input is preserved. 

### `fetch_leaf_runs`

 The same primitive accepts the exact serialized executable leaf formula.
In particular, repeated clauses and repeated literals retain their positions. 
