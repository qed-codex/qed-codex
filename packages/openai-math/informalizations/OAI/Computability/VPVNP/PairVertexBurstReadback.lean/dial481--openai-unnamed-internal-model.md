---
{
  "module": "OAI/Computability/VPVNP/PairVertexBurstReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexBurstReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexBurstReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning one terminal vertex at the burst cutoff

The prefix enters the DFS after preparing the actual root argument. The
native occurrence supplies the choice events and the histogram update.
Conversely, every returning input must pass the same deterministic prefix.


### `prefix_occurrences`

 Pull a complete accepting word back through the native bootstrap,
geometry and gather prefixes. Empty words are allowed. 

### `emit_at_cutoff`

 When the actual report fits the public clock, the reported output
includes exactly the prefix events and preserves the semantic update of the
DFS and flush. The clock may have arbitrary spare instructions. 

### `observed_at_cutoff`

 Uniqueness and external readback also hold for an arbitrary observed
return, including a report first supplied by the burst interpreter. 
