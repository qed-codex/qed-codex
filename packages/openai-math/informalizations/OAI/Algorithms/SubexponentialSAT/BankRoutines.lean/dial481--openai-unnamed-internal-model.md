---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BankRoutines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BankRoutines.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BankRoutines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed finite banks of stack-copy and stack-clear routines

The port lists below are part of the finite program syntax.  Word contents and
word lengths remain runtime inputs.  Each call is justified by an actual trace
of the existing stack routine, including its return instruction.  A final clear
of an already empty temporary gives a uniform reset of the two read registers,
including when the port list is empty.


### `fillStacks`

 Fill each selected port with the original source word. 

### `clearBankStacks`

 Empty the selected bank, preserving every other stack. 

### `fillCmd`

 One copy per static destination, followed by a read-register reset. 

### `clearCmd`

 One clear per static bank port, followed by a read-register reset. 

### `fill_eval`

 Exact execution of the static fill list.  The original source word and the
empty temporary are preserved, as are all unlisted stacks and unread registers.


### `clear_eval`

 Exact clearing cost in terms of the original word lengths.  The temporary
may also occur in the bank: its initial emptiness makes the final clear cost
exactly three instructions in either case. 

### `clear_eval_uniform`

 Equal-width bank cleanup has linear cost in that runtime width. 

### `reset_frame`

 Explicit register frame supplied by both execution theorems. 
