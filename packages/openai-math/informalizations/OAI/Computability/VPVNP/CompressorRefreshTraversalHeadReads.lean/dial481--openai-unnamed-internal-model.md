---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshTraversalHeadReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshTraversalHeadReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshTraversalHeadReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Header and singleton-row reads of the refresh role

The expressions that compute incidence and scratch heads read the published old and
new level headers. The child-node pointer uses exactly two cells of the preimage row.
All subsequent offset arithmetic on the level-plan operands introduces no probes.


### `InputReads`

 The child and parent argument addresses are readable, and the lane count, segment heads and
demand and term bases read only below the stated memory limit. 
