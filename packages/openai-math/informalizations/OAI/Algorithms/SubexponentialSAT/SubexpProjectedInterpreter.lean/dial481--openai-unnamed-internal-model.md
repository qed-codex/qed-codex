---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpProjectedInterpreter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpProjectedInterpreter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpProjectedInterpreter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite postfix interpreter with a real literal-projection call

The literal bytes are parsed and pushed by the concrete loader, then passed to
an actual finite projection service before dispatch resumes. Arithmetic and
projection contracts refer to traces of supplied Boolean instruction tables.


### `program`

 All three services are installed as finite instruction-table regions. 

### `program_literal_code`

 The loader's final halt now jumps into the supplied projection table. 

### `raw_push_trace`

 Parse all literal bytes and enter projection with its raw payload on top. 
