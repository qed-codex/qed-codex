---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEmptyClauseProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEmptyClauseProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEmptyClauseProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A preserving empty-clause test on the actual encoded leaf

The fixed program searches for the one-bit encoding of an empty clause.
The leaf on stack 9 and every other caller word are preserved.  Only the
five empty membership work ports and one empty copy port are used.


### `command_eval`

 A real membership search, including the preserving copy and all cleanup.
No clause-order, width, or nonempty-clause premise is needed. 
