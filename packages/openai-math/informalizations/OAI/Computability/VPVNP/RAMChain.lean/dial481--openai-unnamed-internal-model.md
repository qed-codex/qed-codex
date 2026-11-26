---
{
  "module": "OAI/Computability/VPVNP/RAMChain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMChain.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMChain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successive calls with reset private memory and persistent external memory

A path is specified by its list of actual binary choices in each call. The
native run computes reads and addresses itself. A local replay uses the
reported values. Read consistency over the concatenated event log identifies
the two descriptions of a path, including when branches yield identical states.


### `runSegment`

 Native execution of consecutive calls. Each entry supplies just the branch
choices of that call. After a halt a further call rejects. 

### `LocalSegment`

 The local processor validates the sequence of calls using their reported
read answers, propagating the returned persistent word. 

### `endState`

 The persistent state after a sequence of reports, given by the last report's result or the
incoming state for an empty sequence. 

### `branchPaths`

 Extract one list of actual binary branch choices from each call report, in call order. 

### `eventLog`

 Concatenate all calls' events in execution order for replay against external memory. 

### `ActualPaths`

 Accepted native paths subject to a predicate on their computed reports.
This predicate will impose the exact global and per-call cost caps. 

### `VerifiedReports`

 Accepted local call reports, with correct reads over the whole memory
history. The sorted-record check is a local implementation of this last test. 

### `reportEquiv`

 Parsimony before partitioning calls into sites. 
