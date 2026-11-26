---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNormalizationPrefixProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNormalizationPrefixProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNormalizationPrefixProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

+# Actual literal cleanup followed by tautology removal

This is a fixed program on the original declared variable universe. Its two
stages use the same input/output port and restore empty work stacks. The exact
list order and the length bound are retained for subsequent clause absorption.

