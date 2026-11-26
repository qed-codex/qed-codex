---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermAllocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermAllocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermAllocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Allocation of the shrinking term phase

Following the sorted width and field-start tables, reserve a pair of
words per motif for the inputs and a strided row for each selected term.
One bound on the end of this last region certifies both native segments
and preservation of the six earlier columns.

