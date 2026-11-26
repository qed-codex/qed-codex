---
{
  "module": "OAI/Computability/VPVNP/ExactOneFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneFamily.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial-size exact-one presentations of VNP families

The weighted CNF for a VNP summand can be replaced by exact-one clauses
without changing its generating polynomial. Clause normalization bounds the
number of clause vertices used by the graph reductions. A fixed false bit
gives every instance at least one variable.


### `exists_family_of_isVNP`

 The Boolean variables carry only projection labels. Variable count,
clause count and literal-occurrence count are all polynomially bounded. 
