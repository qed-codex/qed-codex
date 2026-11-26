---
{
  "module": "OAI/Computability/VPVNP/PaddedQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PaddedQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PaddedQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Projections at every length above the table size

The query interpreter addresses the payload from the right end of its input.
A pinned run of zero bits between its self-delimiting table and the payload
therefore leaves all its queries unchanged. This gives the projection at a
specified source length, as needed for tensor powers along an infinite set of
lengths with small circuits.

