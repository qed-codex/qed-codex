---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutInterface.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutInterface.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutInterface.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact integer-bucket interface for the new incidence layout

This interface does not assert existence or a running time. Concrete
construction is assembled from the new packing, integer numerator, and
incidence-pullback modules. Unlike the old residue-only interface, its
locality conclusion is an exact equality in the coefficient ring.


### `localValue_eq`

 A foreign local contribution is constant on its actual integer bucket,
with equality in the entire coefficient ring, not only its residue field. 

### `nodeValue_eq_of_buckets`

 Keeping the owned head fixed and all other bucket labels fixed keeps
the actual incidence-row evaluation fixed. 
