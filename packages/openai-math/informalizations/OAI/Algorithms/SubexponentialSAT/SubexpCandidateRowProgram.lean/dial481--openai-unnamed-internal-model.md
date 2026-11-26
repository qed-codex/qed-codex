---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCandidateRowProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCandidateRowProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCandidateRowProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finish a materialized local candidate with an actual clause evaluation

The input is a packed bit array, a unary declared-variable count, the accumulated
label-validity bit, and a preserved encoded clause. The program checks trailing
padding, evaluates the clause by actual indexed reads, combines the two results,
and clears the working assignment. No semantic predicate is an instruction.


### `command_eval`

 End-to-end execution, including invalid-label and trailing-padding rejection. 
