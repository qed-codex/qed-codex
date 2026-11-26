---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native dispatch for the two trivial formula cases. The classifier
reads the immutable bare clause-list payload at784; the sole final answer
port is787. The nontrivial branch is the actual caller-supplied command. 

### `empty_clause_run`

 An actual empty clause immediately writes UNSAT, without invoking the
nontrivial program or depending on the ambient variable count. 

### `empty_formula_run`

 An empty formula immediately writes SAT, including at ambient n=0. 
