---
{
  "module": "OAI/Computability/VPVNP/PairTraversalTraffic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalTraffic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalTraffic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native traffic for the shared bits and final history visits

The final-arc writer, the two incidence readers, the DFS control code,
and the component-counter updates have concrete reports. Their costs
are compared here with the same selected branch used in the energy
estimate. A descriptor address and an empty field each retain their
own native loop tests.


### `incidenceEvents`

 All final incidence read events of one vertex, in outgoing then
incoming slot order. 

### `finalControlEvents`

 Native logs of the endpoint reads, ordered DFS control and fixed
componentwise flush. Other private computations occur at the DFS hook. 

### `finalControl_cost_le`

 Count the startup of each final burst, its actual control log, and
every binary write in the genuine final-bit writer's reports. 
