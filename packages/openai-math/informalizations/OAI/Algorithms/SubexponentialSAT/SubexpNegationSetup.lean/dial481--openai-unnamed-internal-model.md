---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNegationSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNegationSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNegationSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual runtime preparation of the modular-negation constant. 

### `setupProgram`

 Builds the reusable constant, preserving both the input and its modulus. 

### `preparedNegationProgram`

 One complete call also prepares its own negation constant from the modulus. 

### `unreduced_fourteen_mod_thirteen`

 A noncanonical input exercises reduction before interpreting negation. 

### `zero_mod_sixteen`

 Zero at the full-capacity modulus exercises the B+1-bit setup path. 
