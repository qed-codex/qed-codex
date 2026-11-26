---
{
  "module": "OAI/Computability/VPVNP/IncidentPathFiniteness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidentPathFiniteness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidentPathFiniteness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finiteness of the private path count for arbitrary incident bits

An accepted binary string is recovered from the reports of the bounded site
simulation. This remains true when the incident bits are supplied independently
of the assignments on the other sites.


### `Machine.validateIncident_boundedReports`

 The accepting site reports fit the bucket and fuel bounds, and their
guess bits recover the entire private branch string. 

### `Machine.finiteIncidentPaths`

 The actual accepting branch strings on a fixed local input form a finite
set, including inputs with inconsistent or malformed messages. 
