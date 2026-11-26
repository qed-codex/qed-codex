---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramIntegerCache.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramIntegerCache.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramIntegerCache.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid reusable integer-cache initialization. The runtime parameters A, R
and common width remain on20/21/22. Outputs are H-positive0, H-negative1,
binary clearing denominator2, and retained local width19. 

### `program_runsIn`

 No coefficient list or denominator word is an input. Their full setup is
charged, while the three runtime unary parameters remain available. 
