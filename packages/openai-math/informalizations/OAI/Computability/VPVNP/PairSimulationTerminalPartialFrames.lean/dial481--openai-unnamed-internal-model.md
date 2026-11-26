---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalPartialFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalPartialFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalPartialFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical terminal frames on partial nondeterministic paths

A successful shared-bit call can return to its worker or finish that phase.
At a finishing call, the already traversed prefix and the last report form a
completed fourth block. Its actual final memory initializes the vertex phase.
A later rejecting vertex has no effect on this classification of the prefix.


### `BitPrefix`

 Every completion from the current fourth-stage state can be prepended
by the actual successful earlier calls of this same stage. 

### `shared_vertices_safe`

 Every successful report, including the terminal accepting exit, on
every reached physical prefix from the shared-bit entry preserves the word.
The statement places no requirement on whether a later burst will accept. 
