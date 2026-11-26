---
{
  "module": "OAI/Computability/VPVNP/CompressedRAMDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressedRAMDegree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressedRAMDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Total exponent of each compressed RAM path

The accepting choices of the initial validators have exponent zero. Each
subsequent kernel contributes the degrees of its resident template entries.
On the selected branch the number of occurrences and the degree of every
individual entry obey the bounds of Theorem 7.1.


### `expandedRAMStateCount_degree`

 Every expanded validator path has a selected term chain whose recorded
degrees bound its total parameter exponent. 

### `compressedRAMCount_degree`

 The actual path of (12.2) selects a final network. Its total parameter
degree is bounded by its number of sites, the maximum number of local
occurrences, and the largest degree of an individual map entry. 
