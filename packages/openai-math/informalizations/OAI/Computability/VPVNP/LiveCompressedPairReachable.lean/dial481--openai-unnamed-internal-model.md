---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairReachable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairReachable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairReachable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The reachable online and terminal phases of a compressed pair

When the online calendar returns, the next call stays in its source
invariant. When it accepts, the native transfer installs the terminal tag
in the actual memory belonging to a complete online path. Thus every
continuing call after the deterministic startup belongs to one of these
two source phases, including prefixes that may subsequently reject.


### `Protected.word`

 Source invariants need to protect an outer address only on calls
reachable within that phase. This includes the source accepting exit. 

### `Phase`

 The terminal invariant is indexed by the actual completed online path. 

### `Phase.step`

 One arbitrary continuing native call stays in its recorded phase or
enters the terminal phase with the right post-memory, and preserves the
chosen address. No accepting extension of this call is required. 
