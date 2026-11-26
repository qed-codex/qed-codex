---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorEnds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorEnds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorEnds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Detecting the two ends of the site chain

A site has an outgoing edge when a bit in its address is zero. It has an
incoming edge when a bit is one. The scan saves and restores the address and
returns both edge-presence flags in finite control.


### `State`

 States for scanning and restoring the site address while recording whether outgoing and
incoming edges exist. 

### `code`

 The control scans a site address once, then transfers its bits back. 

### `run`

 The entire bank is restored, including the address. The empty address
returns two false flags, as required for the single-site chain. 
