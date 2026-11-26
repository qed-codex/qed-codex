---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapCallExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact successful clock of an initialized and inlined motif map

The register recipes and the pointer directory add a fixed prefix to the successful
map evaluation. Inlining the public constants then multiplies the length of this
entire prefix by the block length. The host reaches its successful continuation with
the same private memory as the source computation.


### `entryTicks`

 Source tick count at the given selector sequence, including both initializer phases. 

### `source_run_success_exact`

 The fixed natural public bank runs the initialized map for exactly its successful
tick count. The memory equality includes the directory written by initialization. 

### `run_entryInput_success_exact`

 Transport the exact successful source path and its canonical private memory to
the host. The caller's registers, exterior memory and histogram are framed on that path. 
