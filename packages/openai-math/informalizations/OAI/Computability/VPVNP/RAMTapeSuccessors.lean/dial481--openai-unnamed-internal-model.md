---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the two successor checks of a RAM processor

One uniform finite stack program examines the site address, reads the outgoing
eight words and then the incoming eight words, and checks both fields. The
first site installs the public initial state. The terminal site emits a false
outgoing-presence flag. The unconsumed incident bits are the sorting fields.


### `Side`

 Outgoing and incoming sides of a site's successor check. 

### `Port`

 Shared address, incident, width, cap, and scratch registers together with side-specific
words, flags, and records. 

### `edgePorts`

 Connect a single-edge reader to the shared incident stacks and the selected side's word,
flag, and record registers. 

### `initialPorts`

 Connect initial-state normalization to the public initial word, received state word,
received running bit, and scratch stacks. 

### `normalizeIfFirst`

 Install the public initial state at a site with no incoming edge and immediately return at
an interior receive site. 

### `body`

 Check outgoing and incoming fields in stream order, normalize the first site's state, and
emit the outgoing-presence bit. 

### `read`

 This table is independent of the word length, site count and site identifier. 

### `afterEdge`

 Register bank after one side's field check, with the unconsumed incident tail and that
side's updated words, record, and flags. 

### `afterNormalize`

 Install the public initial word and a true running bit in the incoming registers when the
site has no incoming edge. 

### `normalizeCost`

 Step count of first-site normalization, including the single return step when an incoming
edge is present. 

### `finish`

 Final register bank after both edge checks, first-site normalization, and emission of the
outgoing-presence bit. 

### `steps`

 Step count for the site-address scan, both eight-word successor checks, first-site
normalization, and outgoing flag emission. 

### `read_runs`

 Both outgoing and incoming words are preserved for the call loop. The two
record payloads are independently available to the sorted predecessor check.
The result includes a canonicality flag for each raw field, even if malformed. 

### `read_incident_runs`

 The incident vector in the precise layout of (10.1) supplies both fields
without a bit lookup oracle. 
