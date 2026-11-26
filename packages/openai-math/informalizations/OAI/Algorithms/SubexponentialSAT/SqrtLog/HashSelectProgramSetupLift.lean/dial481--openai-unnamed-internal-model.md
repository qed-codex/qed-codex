---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSetupLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSetupLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSetupLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Only setup is lifted into the caller. The mass callback and selector are
compiled in the caller's full state space, so they can access its context. 

### `setup_eval_lifted`

 Mapped setup leaves all formula/ring context outside its ports unchanged.
The subsequent callback is a command on the full caller state space. 
