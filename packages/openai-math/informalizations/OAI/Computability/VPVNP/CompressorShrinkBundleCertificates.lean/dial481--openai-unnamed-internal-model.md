---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkBundleCertificates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundleCertificates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundleCertificates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native shrinking source packets with their cursor and data certificates 

### `Certified`

 The scheduled bundle stage has the stated source run and cursor limit, and its external
reads and writes stay within the respective shrinking regions. 

### `certified_sources`

 The sources and their actual footprints have the same report boundaries
throughout the eleven workers, including both prefix scans. 
