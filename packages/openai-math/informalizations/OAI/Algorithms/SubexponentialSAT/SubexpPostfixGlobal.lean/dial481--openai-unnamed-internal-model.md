---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPostfixGlobal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPostfixGlobal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPostfixGlobal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared-machine port adapter for the concrete postfix interpreter

The shared machine uses code/depth/operand/scratch stacks 26/28/27/29.
A fixed permutation installs the proved interpreter there while accepting
arithmetic service tables already written for the shared 16-register,
128-stack machine. Port renaming adds no machine transitions.


### `ports`

 Four disjoint swaps; all other physical stack indices are unchanged. 

### `reindexCfg`

 Reindex physical stacks without changing their contents or control state. 

### `localService`

 The input arithmetic table already uses shared physical ports. 

### `global_complete_runsIn`

 Shared-port execution of the exact serialized compiled expression. The
only arithmetic assumptions are local traces of the supplied finite tables. 
