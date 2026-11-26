---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseFiltersProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseFiltersProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseFiltersProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact-order clause filters on encoded formulas

The relation scanner occupies stacks 0--12. The outer record pass uses stack
13 for unread records, stack 14 for the reversed output record list, and stack
15 for the reversed current payload. Two stack transfers put a clause into the
scanner and return it to the existing frame emitter.


### `callback_eval`

 A complete encoded clause-selection callback, including the actual
relation scan, result cleanup, and framed output emission. 
