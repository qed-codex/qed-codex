---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CounterNormalizeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterNormalizeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterNormalizeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual normalization of a positive binary counter word

The logarithm preparer reverses its input and removes high zeroes together
with the leading one. This wrapper physically restores that one and reverses
the remaining word. Positive inputs therefore retain their exact value and
have width log2(value)+1. All three registers and both work stacks are clean
at return, even when the incoming registers are arbitrary.

