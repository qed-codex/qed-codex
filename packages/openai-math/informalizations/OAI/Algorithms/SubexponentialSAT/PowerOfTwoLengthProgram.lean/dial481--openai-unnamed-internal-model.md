---
{
  "module": "OAI/Algorithms/SubexponentialSAT/PowerOfTwoLengthProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PowerOfTwoLengthProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PowerOfTwoLengthProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A power-of-two word from an input length

For a compile-time constant c, this fixed program consumes a word w and writes
c + 2 * length(w) zero bits followed by one true bit.  The runtime loop consumes
one Boolean cell per iteration; no natural-number register or semantic length
instruction occurs in the machine.


### `fixedPush`

 Only this compile-time recursion changes the number of control labels. 

### `program`

 There are c+9 control labels; c is a compile-time constant. 

### `run_trace`

 Complete clean input-to-output execution, with an exact linear cost. 
