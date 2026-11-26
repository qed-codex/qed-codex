---
{
  "module": "OAI/Computability/VPVNP/CompressionDegreeAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionDegreeAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionDegreeAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degree coverage for the fixed iterated compressor

The shrinking and refresh records use the two parts of the common template
alphabet. At every site and on every branch of the actual repeated block,
the degrees in these records bound the degree of its chosen kernel monomial.


### `execute_degreeCovered`

 The actual repeated witnesses in the kernel history obey the degree
bound given by the corresponding repeated records. 
