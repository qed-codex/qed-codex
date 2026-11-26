---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderUnique.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderUnique.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderUnique.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniqueness of the native header path

A successful call with the empty choice string executes no binary-choice
instruction. All surplus choices are therefore rejected. Repeating this
argument along the verified header stages proves exact path uniqueness,
including the position of the accepting call.


### `execute_empty_forces`

 A successful empty-input call forces both its branch input and its report. 

### `accepted_empty_unique`

 If the empty choice list succeeds at each call and the last call accepts,
this is the sole accepting path at that start state, memory and fuel. 

### `accepted_path_unique`

 The physical header table admits exactly one accepted native path when
the scheduled source reports are produced by deterministic microcalls. 
