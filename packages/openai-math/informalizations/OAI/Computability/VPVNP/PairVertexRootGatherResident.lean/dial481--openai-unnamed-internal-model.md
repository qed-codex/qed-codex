---
{
  "module": "OAI/Computability/VPVNP/PairVertexRootGatherResident.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootGatherResident.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootGatherResident.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private vertex state preserved by the terminal root gather

The DFS stack and its geometry pointer are below the root packet. The
histogram, the twelve-word frame and the scalar cache lie beyond the packet.


### `Resident`

 The private data needed to enter DFS after the root argument has been filled. 

### `after_gather`

 Replacing the root packet preserves the DFS stack and every vertex-wide
private field, including every initially zero histogram component. 

### `residentGeometry`

 The dispatcher and flush can read their two fields through DFS scratch. 

### `cacheScratch`

 The leaf verifier sees all 38 unchanged scalar operands in its scratch. 

### `zeroHistogram`

 Every labeled counter seen by the site report starts at zero. 

### `of_ready`

 A geometry run supplies the resident state from a booted stack and an
initially zero histogram. Its private stores are outside the histogram. 
