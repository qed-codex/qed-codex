---
{
  "module": "OAI/Computability/VPVNP/MotifOrdinarySum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifOrdinarySum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifOrdinarySum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From a restriction by a direct sum to an ordinary sum of images

The base identities in Theorem 6.1 use one local linear map per party for
each summand. A restriction from the direct sum supplies these maps by
restricting the original matrices to each summand's coordinate block.


### `ordinary_sum_of_class_le_finset`

 A finite direct sum dominating the demand yields an ordinary sum identity
with exactly the same indices, in the demand's given coordinate spaces. 

### `ordinary_sum_of_class_le`

 The direct-sum restriction in the fixed-motif comparison gives one
ordinary summand for each supply tensor. 
