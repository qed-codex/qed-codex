---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ExecutionHashSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native setup from three binary parameter words to the actual
candidate queue and runtime selector counter. The full caller frame remains
available to the eventual mass-evaluation callback. 

### `generate_eval`

 The only inputs supplied to this setup are small binary parameter words
and the initial row stream. The alphabet and all candidate records are
actually generated. Arithmetic producing those binary parameters is charged
by its caller. 
