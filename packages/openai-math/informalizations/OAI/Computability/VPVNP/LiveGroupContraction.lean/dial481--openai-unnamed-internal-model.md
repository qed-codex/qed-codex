---
{
  "module": "OAI/Computability/VPVNP/LiveGroupContraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveGroupContraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveGroupContraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Contracting the evaluation mode of the live chain

For a fixed first-half cut assignment, each pair reads the exterior bits at
its two adjacent cuts and checks its outgoing counters. Each tail group then
reads two adjacent configuration fields and checks one transition. Summing
the products of these local counts eliminates the forced counter fields and
configuration strings, leaving the actual evaluator path multiplicity.


### `exteriorOf`

 Exterior primed bits are read from the first-half cuts. The initial cut
has width zero. 

### `firstCheck`

 One pair checks the canonical outgoing fields and the increment over
its incoming counters. Both sides of each counter comparison are natural
numbers, so overflow cannot create additional paths. 

### `pairCount`

 The local count of evaluation-mode paths through a first-half group. 

### `tailCount`

 Number of branch bits yielding exactly the two specified adjacent tail
states. Distinct choices count separately even at coincident successors. 

### `evaluation_contraction`

 The evaluation mode contracts to the sum over exterior assignments,
nomination vectors and local pair paths, followed by a single evaluator on
the componentwise sum of their increments. 

### `pairCount_mode`

 A successful first-half group sets the literal first bit of its outgoing cut. 

### `tailCount_mode`

 A successful tail group with an outgoing cut sets its literal first bit. 

### `halves`

 The two contiguous halves, in order of their physical group indices. 

### `contract_halves`

 Product and sum reindexing for a per-group evaluation-mode count on raw cuts. 
