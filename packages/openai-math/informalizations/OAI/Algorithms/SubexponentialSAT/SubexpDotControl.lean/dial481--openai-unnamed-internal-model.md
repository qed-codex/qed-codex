---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDotControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDotControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDotControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control dot products on serialized field elements

The multiplication and addition interfaces below are actual finite-program
trace contracts. The concrete endpoint instantiates them with flat quartic
arithmetic at modulus p. Stack 77 is the accumulator and stack 78 is the stream
of row/input pairs; both remain outside the 77-stack multiplication service.

