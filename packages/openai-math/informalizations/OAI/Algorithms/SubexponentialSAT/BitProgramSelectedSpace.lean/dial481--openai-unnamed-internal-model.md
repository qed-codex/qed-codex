---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BitProgramSelectedSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BitProgramSelectedSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BitProgramSelectedSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stack-bit growth inside a fixed set of ports

Every actual instruction adds at most one bit to any fixed set of stacks.
These bounds exclude unselected persistent stacks, whose contents may be
arbitrarily long. The list corollaries require distinct ports, as used by the
physical workspace cleanup program.


### `trace_listStackBits`

 List form matching the exact cost of clearing distinct selected ports. 
