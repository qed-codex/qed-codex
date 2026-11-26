---
{
  "module": "OAI/Computability/VPVNP/PairTraversalWorkerMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalWorkerMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalWorkerMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing a descriptor header before the identifier scan

The site's source identifiers lie below the header, and the translated row
starts immediately after the two header words. Thus the header writes and
the scan can be interchanged, even if the count was read from a header word.


### `headers_then_scan`

 Writing the two saved header values first gives the same complete external
memory as publishing them after the scan. 
