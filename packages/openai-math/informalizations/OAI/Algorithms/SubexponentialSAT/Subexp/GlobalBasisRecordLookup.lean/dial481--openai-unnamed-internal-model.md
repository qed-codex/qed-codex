---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRecordLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRecordLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRecordLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving unary-indexed access to framed records

Both the record stream and unary index are copied by real stack programs.
The copied counter controls a fixed loop, each iteration consumes one record,
and the selected payload is decoded into the output.  All temporary stacks
are cleared.  This is used to select a current type group and then a color's
local table; the index is not interpreted by a semantic machine primitive.

