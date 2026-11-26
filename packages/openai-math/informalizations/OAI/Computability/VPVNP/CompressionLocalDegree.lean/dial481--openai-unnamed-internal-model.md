---
{
  "module": "OAI/Computability/VPVNP/CompressionLocalDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionLocalDegree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionLocalDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parameter degrees of the local compressor maps

Every accepted shrinking map reads one label per base repetition, and every
resident occurrence of that map contributes its own record. The refresh
reads the labels of a single motif entry after its two diagonal checks.
This identifies the total parameter multiplicity with the sum of the
degrees stored in the actual records of each selected substep.


### `shrinkStateKernelWitness_degree_eq`

 The recorded resident maps account for all labels of a shrinking-site witness. 

### `dyadicRefreshKernelWitness_degree_eq`

 The motif entry supplies the full recorded degree of an accepted refresh port. 

### `left_totalExponent`

 Using the shrinking summand preserves the total degree. 

### `right_totalExponent`

 Using the refresh summand preserves the total degree. 

### `shrinkPass_degreeCovered`

 At the scheduled lane count the tagged shrinking witnesses fit their actual records. 

### `refreshPass_degreeCovered`

 Each tagged refresh witness fits the records of its chosen port and branch. 
