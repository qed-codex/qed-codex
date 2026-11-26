---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFieldRowValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldRowValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldRowValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric row values for the concrete field-candidate program

This specification records both order conventions: the first scope coordinate
is the least-significant base-p digit, and the enumerator prepends each Boolean
value to its output. Leading zeroes in the current-rank word are immaterial.


### `command_eval`

 A concrete row execution with an output specified solely by numeric rank.
There is no remaining callback execution or semantic-test hypothesis. 

### `program_runsIn`

 The corresponding run of the finite instruction table. 
