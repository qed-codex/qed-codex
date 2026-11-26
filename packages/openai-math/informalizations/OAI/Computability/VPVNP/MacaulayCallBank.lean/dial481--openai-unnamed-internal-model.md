---
{
  "module": "OAI/Computability/VPVNP/MacaulayCallBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayCallBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayCallBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Staging and cleaning the fixed banks of coefficient-query subroutines

A call copies selected read-only words into its private registers. On return
it prepends selected output stacks to the caller's ports and erases its
private bank. The time bound of the called routine and its space bound
enter the resulting estimates separately.


### `Port`

 Stack addresses for the caller's words, the callee's private registers and the scratch
stack used during copying. 

### `frame`

 Combine caller and callee stacks into a single call frame with an empty copy scratch stack. 

### `clean`

 Initial or returned frame containing the caller's stacks and empty private and scratch
banks. 

### `filled`

 The private inputs after staging a call. Each selected register holds a copy of its
designated caller stack. 

### `saved`

 Caller stacks after prepending the specified callee outputs, in order, to their destination
stacks. 

### `machine`

 Stage the selected input words, execute the private routine, copy its outputs back and
erase the specified private registers. 

### `overhead`

 Cost of all copies and clears around the called program. 
