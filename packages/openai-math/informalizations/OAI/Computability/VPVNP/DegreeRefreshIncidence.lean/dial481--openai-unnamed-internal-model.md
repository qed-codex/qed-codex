---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the incident external wires of a bundle matching

When an arc matching sends whole bundles to whole bundles, the incoming
segments at a port all come from one external wire. Their offsets are still
determined by their order within the original source bundle.


### `incidentPortSegments`

 Read all segments at a port using just the two external half-wires there.
The inverse matching recovers each incoming segment's source-port index. 

### `incidentPortSegments_external`

 On a global assignment of external words the local reader agrees with
direct extraction from each arc's original bundle. 
