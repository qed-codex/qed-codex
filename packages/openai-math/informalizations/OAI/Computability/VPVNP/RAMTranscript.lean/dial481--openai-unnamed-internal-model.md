---
{
  "module": "OAI/Computability/VPVNP/RAMTranscript.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTranscript.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTranscript.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parsimonious distributed RAM transcripts

For a power-of-two number of sites and bucket capacity, the accepting binary
paths of the native RAM are in bijection with joint choices of successor and
sorting messages and one successful local path at each site. The local tests
read the site's header, its adjacent chain fields, and its sorting fields.
They enforce the private instruction clock, per-call cost cap, global cost cap,
and memory read consistency, without a global oracle at any processor.


### `Messages`

 Shared successor cuts and sorting-network messages of one transcript. 

### `Messages.chain`

 Successor cut at each boundary between consecutive sites. 

### `Messages.memory`

 Shared sorting-network data for verifying memory consistency. 

### `localRecords`

 Padded initialization and probe records contributed by one processor. 

### `Validator`

 One site's accepting reports. The header array is consulted only at
`v`, in the initialization record of `localRecords`. 

### `validators_iff`

 The independent tests at all sites, expressed using their unique global
execution and its correctly sorted memory history. 

### `TypedJointPaths`

 Accepted shared messages together with one verified report list at every site. 

### `jointReports_bijective`

 Flattening the local reports is a bijection. The successor messages,
the bucket partition, all pre-comparison blocks, and every last-record field
are determined by the native path, even after an early halt. 

### `transcriptEquiv`

 Lemma 10.1 at the level of typed transcript fields. Genuine paths are
indexed by their binary program choices. A validated read has exactly one
allowed word, and therefore adds no multiplicity. 
