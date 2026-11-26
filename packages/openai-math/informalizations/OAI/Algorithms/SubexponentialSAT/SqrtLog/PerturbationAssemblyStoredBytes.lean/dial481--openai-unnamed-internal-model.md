---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyStoredBytes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyStoredBytes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationAssemblyStoredBytes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact byte order of the physical row scan. No sparse normalization or
deletion of zero coefficient records is used by this bridge. 

### `originStored_data`

 The high-coordinate branch's single physical record, even when zero, is
exactly the existing constant Stored representation at positive precision. 

### `fullScan_dictionary`

 Typed endpoint of the actual scan, with a supplied computed beta. 
