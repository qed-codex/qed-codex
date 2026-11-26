---
{
  "module": "OAI/Computability/VPVNP/PairTerminalGatherNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalGatherNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalGatherNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native terminal gathers in the selected wire geometry

Each vertex reads the final shared bits into its actual root argument before
DFS. The same bit is read at both endpoints. The directory lookups add five
probes per outgoing slot when summed over the whole graph.


### `argumentSize`

 Number of bits in a final site's argument packet, summed over all outgoing and incoming
slots. 

### `run`

 The actual linked table fills the root store and passes control and the
unconsumed branch stream to its continuation. 

### `run_after_reports`

 Run the gather in the memory actually written by the shared bit scan. 

### `probes_total`

 Exact external traffic of all the actual gather prefixes, including
both occurrences of a loop and each of the five directory probes per arc. 
