---
{
  "module": "OAI/Computability/VPVNP/CloudReplacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CloudReplacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CloudReplacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cloud replacement in the bounded-degree amplification

Section 5.3 of *VP and VNP differ over every field* replaces each old vertex
with a copy of a fixed port graph. Half the steps stay in the cloud and half
follow a matching on the ports. The matching realizes an averaged walk on the
old vertices. The estimates below use the same normalization as `walkEnergy`.


### `cloudMatchingEnergy_le`

 The energy between the centers of matched clouds is bounded by the matching energy
and twice the squared displacement to a port's center (§5.3). 

### `portWalk`

 The transition matrix on clouds obtained by following a matching from a
uniformly chosen port. 

### `cloudWalk`

 The internal transition kernel and the matching transition each have weight one half. 

### `cloudWalk_hasPoincareBound`

 The cloud graph amplifies a bound on the induced walk between clouds
using the bound on the internal port graph. 
