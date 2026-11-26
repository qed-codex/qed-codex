---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteEndpoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEndpoints.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEndpoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the two physical cost endpoints from the site address

Allocate a zero word and remove the public number of cells reserved for the
address and low shift bits. Prepend the address, copy and increment the
padded word, then prepend the low zero bits to both results.


### `Port`

 Ports for the site address, address and bucket exponents, word width, two cost endpoints,
and trimming scratch. 

### `prepare`

 One finite instruction table for every width, site count and bucket size. 

### `steps`

 Step count for allocating, trimming, incrementing, and shifting the two padded
cost-endpoint words. 

### `prepare_runs`

 Compute both cost words, preserve the address and public counters, and
return both scratch stacks empty. The last site's end word is the global cap. 
