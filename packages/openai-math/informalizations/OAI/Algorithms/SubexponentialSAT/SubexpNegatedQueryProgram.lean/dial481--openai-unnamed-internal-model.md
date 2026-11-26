---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNegatedQueryProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNegatedQueryProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNegatedQueryProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving complemented-literal queries

The clause iterator supplies a literal's unary word in reverse order. This
fixed program preserves that query on stack 0 and writes the reversed unary
word for the opposite literal on stack 1. Stacks 2 and 3 are empty workspaces
on entry and return. All costs below count actual finite-program transitions.


### `slots`

 The four ports are original query, result, work, and scratch. 

### `negatePorts`

 Only the work and result ports are assigned to the unary complementer. 

### `command`

 The syntax, register count, stack count, and label count are independent
of the encoded literal's value. 

### `steps`

 Exact complete execution count, including the final halt. 

### `program_runsIn`

 Linear time in the actual query's bit length; the original query remains
available to the caller and both work stacks are empty on return. 

### `primitive_execution`

 The proved source trace compiles to actual primitive-tape execution. 
