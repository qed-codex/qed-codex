---
{
  "module": "OAI/Computability/VPVNP/PairSimulationWorkerPhaseEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationWorkerPhaseEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationWorkerPhaseEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relocating all accepted source worker paths to their terminal phase

The source executes on memory agreeing with the physical bank away from the
two terminal controller cells. Known paths replay forward after the clock is
reduced by the dispatch allowance. Conversely every completed physical block
can be recovered at the full source clock. The chosen memory readback agrees
at every worker address, including the dense histogram.


### `WorkerFrame`

 Obligations for the actual worker reports under the terminal controller. 

### `block`

 Transport a completed source-worker path to a physical terminal phase, adding the
controller reports and computing the resulting physical memory from their events. 

### `sourceBlockEquiv`

 All actual physical completions, including arbitrary incoming tape
lengths, are obtained from the original worker at the selected memory. 
