---
{
  "module": "OAI/Computability/VPVNP/PairTraversalArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native traversal arena for a selected compressor branch

The actual level-indexed placement scans feed a fixed leaf worker followed by
a fixed fiber worker. A fixed tag writer marks the same selected layers from
their retained pass origins. The programs share one external memory, and
their writes preserve the final-arc bit words between rows and tags.


### `native_arena`

 Construct the selected descriptor arena in a shared native memory. Its
DFS rows and role words are read back at their actual native addresses and
every final bit remains available. Each worker costs a bounded number of
probes and bursts per selected row, independently of all wire widths. 
