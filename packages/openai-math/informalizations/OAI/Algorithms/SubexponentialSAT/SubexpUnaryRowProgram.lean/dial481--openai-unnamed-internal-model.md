---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpUnaryRowProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpUnaryRowProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpUnaryRowProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

+# Actual unary-validity table rows

Each scalar rank is padded to the modulus word's width, then tested by the
checked unary-validity program with the actual chunk-width word. The callback
preserves the rank, fuel, modulus, and chunk width, and emits one Boolean bit.

