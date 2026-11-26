---
{
  "module": "OAI/Computability/VPVNP/RAMSuccessor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSuccessor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSuccessor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successor messages and local RAM call validation

In Lemma 10.1, a successor message carries the cumulative cost and either
the running state or a halt. The last processor checks acceptance locally.
The site predicate reads its own reports and its two incident cuts. Its
unique consistent assignments recover precisely the bounded accepting call
chains, with read values still to be checked by the sorting network.


### `Cut`

 The status and persistent state form a tagged option. A halted state has
one representation, independently of the last persistent word. 

### `Cut.cost`

 Cumulative cost of the computation up to this boundary between site segments. 

### `Cut.state`

 Persistent state at the cut while the computation is running, or the empty option after
  an accepting halt. 

### `Cut.advance`

 Advance the cut through the given call reports by adding their call-and-probe costs and
taking the resulting persistent state. 

### `SiteRun`

 Local processing at site `v`. A running continuation must have reached
the next bucket. All reports are validated using the incident running state. 

### `SiteCheck`

 At an internal cut the outgoing message must be exactly the local result.
At the last site the send is clamped and the actual local result must be halted. 

### `inputCut`

 Internal wires are indexed by the site that sends them. 

### `outputCut`

 Look up the successor message sent by this site if it has a successor, returning the empty
option at the final site. 

### `SitesPass`

 Only the initial site substitutes a fixed incoming status. 

### `canonicalCuts`

 Accumulated cost and state determine all internal cuts, independently of
the accept/reject decision. 

### `ChainChecks`

 Recursive semantics for proving the equivalence with the independent
site tests. The cost and state are recomputed at each boundary. 

### `sitesPass_wire_cost`

 The cumulative cost sent on each internal edge is representable whenever
the global cap fits in a word. 

### `withinCaps`

 The bounds used for accepted paths in Lemma 10.1. 

### `successor_unique`

 Every bounded accepting call chain has a unique grouping and assignment
of the internal successor wires. Read consistency can be imposed independently. 
