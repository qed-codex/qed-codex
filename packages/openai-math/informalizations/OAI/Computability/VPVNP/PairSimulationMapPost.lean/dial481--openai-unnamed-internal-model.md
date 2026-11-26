---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapPost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapPost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapPost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private memory after an inlined motif map call

Lowering the public constants changes the register allocation and instruction count.
The host uses the source call's private memory, so its output satisfies the same
canonical update of the directory, selector, label and histogram cells.


### `source_run_post`

 Installing the cast of the fixed natural constant bank preserves the
canonical private-memory update of the full descriptor-driven map. 

### `RunsPost`

 The call returns its exit, histogram, preserved caller state and private-memory
postcondition on a single host instruction path. 

### `lift_path_post`

 An individual source prefix of length `n` has exactly `factor L ord * n` host ticks.
Its private postcondition holds on the same host state as its register and histogram effects. 

### `lift_run_post`

 Lower the complete source call, retaining its postcondition and multiplying its
instruction bound by the fixed block length. 

### `run_entryInput_post`

 Run the inlined map from the caller's resident descriptor. The canonical memory
update uses the same initial host memory and the same exit as the histogram result. 
