---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCleanLiteralsProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCleanLiteralsProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCleanLiteralsProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual clausewise literal cleanup

Each framed clause is decoded, passed to the fixed literal-deduplication
program, and framed again. An outer record reversal restores clause order.
The finite control is independent of the input formula and its clause sizes.


### `clean`

 One fixed program maps literal cleanup over every clause and restores
the original clause order. No formula-dependent control table is used. 
