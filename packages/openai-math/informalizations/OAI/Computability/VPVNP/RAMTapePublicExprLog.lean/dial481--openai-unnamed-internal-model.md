---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicExprLog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprLog.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprLog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Padded word code for the public grammar logarithms

A single fixed control computes either binary logarithm in the destination
register. After scanning the bits it converts at most `w` unary marks to a
padded binary word by verified word increments. The other registers, public
words, persistent word and private write log are preserved.


### `code`

 In-place floor or ceiling binary logarithm; no auxiliary architectural
register is required. 

### `bound`

 Quadratic step bound for computing a floor or ceiling binary logarithm in a padded word. 
