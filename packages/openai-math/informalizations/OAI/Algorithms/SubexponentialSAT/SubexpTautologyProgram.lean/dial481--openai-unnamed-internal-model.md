---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTautologyProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTautologyProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTautologyProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual encoded-clause tautology testing

The outer iterator reads unary literal records. For each literal, a concrete
program builds its opposite's query, copies the preserved clause, and runs the
proved encoded membership program. All data-dependent repetition is in those
finite programs and the record iterator.


### `copyClauseProgram`

 The current literal uses stack 7, so stack 4 is the copying scratch port. 

### `initializeProgram`

 Copy the input clause once, before the destructive outer scan. 

### `tautology_eval`

 Complete clause testing, including its actual initialization and cleanup.
The clause remains on stack 2, and stack 1 contains the Boolean answer. 
