---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpChunkDescriptor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpChunkDescriptor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpChunkDescriptor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary-input chunk descriptors from one fixed finite program

Input stacks 0 and 1 hold little-endian binary n and ell. All other stacks
start empty. Output 8 contains framed unary chunk widths; output 9 contains
the matching framed singleton scopes. The positive-ell premise ensures that
every nonempty chunk iteration consumes input.

