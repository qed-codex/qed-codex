---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafFieldSources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFieldSources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFieldSources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scalar sources for initializing the virtual verifier's private stacks

Every scalar stack is either a width-bounded binary word or a unary tally.
Only the incident bit vector needs the field-copy subroutine. Addresses,
caps and bucket endpoints are the words actually seen by the auxiliary
site verifier.


### `source`

 The loading mode, bit count and source word for each scalar input field of a virtual site.
The incident port starts empty for the later half-wire copy. 

### `SourceFit`

 The slot tally and choice-stream length fit in machine words when staging the site's scalar
fields. 
