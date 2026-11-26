---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleRankFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleRankFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleRankFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Probe addresses of the absolute-port rank scan

A ranking call reads the owner and pivot, reads the owner's count and then
scans the whole fixed-stride row, including its padding. Its only write is
the rank indexed by the visiting old port.


### `scan_access`

 Accesses in every report of an actual completed native ranking scan. 
