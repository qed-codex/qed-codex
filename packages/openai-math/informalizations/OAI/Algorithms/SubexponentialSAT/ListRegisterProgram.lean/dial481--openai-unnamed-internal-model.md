---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ListRegisterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ListRegisterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ListRegisterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Unbounded Boolean-list registers implemented by finite programs

Logical words are Boolean stacks.  Three fixed scratch stacks suffice for
alias-safe word assignment, prefixing, and appending; all are restored empty.
The programs below contain only the existing finite Boolean/stack instructions.
Every stated cost is proved by an actual execution trace.


### `Run`

 A complete execution retaining an arbitrary surrounding data store. 

### `port`

 Logical registers occupy the first `v` stacks. 

### `temp`

 Scratch allocation is fixed, independently of all register contents. 

### `assignProgram`

 Snapshot the source before modifying the destination, so all aliases work. 

### `State`

 Only two Boolean flags are bounded data; all words remain unbounded lists. 

### `time`

 This exact cost is justified by `run` below, not supplied as an annotation. 

### `program`

 The executable table depends on the operation and its fixed port indices,
not on the contents or lengths of any word. 

### `call_eval`

 Direct use inside the verified structured compiler's loops and branches. 

### `time_le`

 A uniform linear bound on each implemented word operation. 

### `emptyProgram`

 The empty script still has one real halt instruction. 

### `scriptProgram`

 A fixed script is compiled once by joining its actual finite tables. 

### `script_run`

 All word-operation costs are connected to the single generated program.
Intermediate word values affect execution length, never program construction. 

### `scriptLabels_le`

 This static size bound has no dependence on word lengths. 
