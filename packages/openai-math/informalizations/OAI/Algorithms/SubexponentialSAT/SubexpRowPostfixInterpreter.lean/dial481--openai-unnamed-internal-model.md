---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRowPostfixInterpreter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowPostfixInterpreter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowPostfixInterpreter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The source-row postfix interpreter on the fixed 256-stack workspace.
Only port names change; the checked dispatcher and all service transitions
are retained. Parameters such as R and the field remain encoded data. 

### `localService`

 The input arithmetic table already uses shared physical ports. 

### `ImplementsOnGlobal`

 Arithmetic tables act only on values reachable after projection. 

### `LoadImplementsGlobal`

 The actual unary service acts on the newly pushed raw operand. 

### `global_complete_runsIn`

 Execution of original raw-literal source, with a concrete projection call
at every literal. The three hypotheses concern the supplied finite tables. 
