---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpAlphabetProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpAlphabetProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpAlphabetProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical scalar alphabet by an actual binary countdown

At each positive counter value the program copies and decrements the copy,
then prepends its fixed-width word as a record. The controller decrements the
original counter afterward. Thus descending visits produce ascending records.


### `body_eval`

 Every body call is a concrete copy, decrement, reverse, and record emit. 

### `loop_eval`

 The actual countdown visits each lower integer exactly once. Prepending
the emitted records gives ascending order, including the zero word. 

### `program_runsIn_clean`

 Starting with only a binary counter word, emit the complete ascending
fixed-width alphabet below its value. 

### `selected_program_runsIn`

 The canonical prime-field alphabet is an actual program output, in
exactly the same order as the vector and node specifications. 
