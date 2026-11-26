---
{
  "module": "OAI/Computability/VPVNP/CursorBranchCommunication.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorBranchCommunication.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorBranchCommunication.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External accesses for the compressed pair

The site burst follows its placement history and reads both of its
incidences. Summing these reads charges each final arc exactly twice,
including when its endpoints coincide. The global allowance accounts
separately for the descriptor scans, the writes of shared bits and
the final vertex visits.


### `incidentBits`

 Total number of incident payload bits at one site, summing all incoming and outgoing
half-wire widths. 

### `sum_incidentBits`

 The two endpoint reads at all vertices together have cost twice
the total actual width. 

### `siteAccesses`

 The per-site external charge, allowing a fixed number of probes per
incident bit, and a fixed polylogarithmic cost per history occurrence. 

### `branchAccesses`

 Descriptor scans use old positions, final guesses use actual wire
widths, and each final-site charge uses that site's own incidences. 

### `eventually_pairAccesses`

 The threshold precedes every choice of branch. The total charge
fits any positive fraction of the live group, while each site's burst
is bounded by the square root of the input length. 
