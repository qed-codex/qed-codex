---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyVisitAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyVisitAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyVisitAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Addresses accessed by the greedy record reader

Every forbidden operand is fetched in two reads, first from the pointer row
and then from the addressed cell. The search repeats those reads from the
same first pointer. At the end it reads the two header words and writes the
chosen value to the destination named in the header.


### `visit_access`

 Read and write support of the native visitor, including the indirect
operand reads of every search pass. Addresses advance in word arithmetic. 
