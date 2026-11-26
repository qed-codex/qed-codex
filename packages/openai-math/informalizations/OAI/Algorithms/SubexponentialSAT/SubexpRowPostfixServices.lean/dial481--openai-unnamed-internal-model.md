---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRowPostfixServices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowPostfixServices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowPostfixServices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Framed arithmetic calls for source-row postfix expressions

The physical interpreter keeps its operand list on stack 27. These fixed
commands read two framed operands, call a dense polynomial service on
240/241, and frame its result from 244. All temporary stacks are restored;
the caller's remaining operands and every other stack are preserved.


### `move`

 Move a runtime word in its original orientation, using the shared copy
scratch stack 120. The source and destination are fixed program ports. 

### `command`

 The supplied arithmetic command is installed as actual finite code. 

### `program_runsIn`

 Exact framing around any checked dense-array arithmetic service.
The service hypothesis is a trace of the inserted command on the actual
prepared stores, and is later discharged by the concrete add/multiply tables. 
