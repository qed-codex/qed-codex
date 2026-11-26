---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/OneHotAlphabetProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/OneHotAlphabetProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/OneHotAlphabetProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Runtime one-hot alphabet generation

The unary input length r is data. Each loop iteration constructs one r-bit
one-hot word using the checked repeated-copy program and prepends its frame.
The final order is the decreasing order of the hot bit's position.

