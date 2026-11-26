---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMRunEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMRunEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMRunEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choice histories of the scheduled primed-input RAM

A native RAM path records one list of branch choices per call. A choose item
contributes a singleton and every other item contributes the empty list, as
does the final accepting call. Reading the singleton at each owner recovers
the chosen assignment even when several branches write equal words.


### `assignmentCalls`

 The exact choice lists supplied to the item calls and the final call. 

### `decodeAssignmentCalls`

 Read the first choice of the call at each owner. The defaults make the
decoder total on malformed streams, which are excluded from `ActualPaths`. 

### `assignmentCalls_restrict`

 Restricting a total bit vector to the choose items produces the same
choice lists, since deterministic items consume no bits. 

### `Item.probeCount`

 The external probes of each scheduled item, fixed independently of the bits
and the words fetched from memory. 

### `scheduledCost`

 Cost of the data calls and the final one-unit halt. 

### `scheduledReports_withinCaps`

 Both caps used by the parsimonious transcript construction hold whenever
the public cost fits the global budget and each site permits three units. 

### `scheduledPathEquivOfCap`

 The native paths respecting a cap are in bijection with the independent
bits when all generated report sequences fit the cap. 

### `scheduledPathEquiv`

 With no cost filter the interpreter enumerates every assignment once. 

### `scheduledPathEquivWithinCaps`

 Exact enumeration by paths under the global and per-call RAM caps. 
