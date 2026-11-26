---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterKernelExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterKernelExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterKernelExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Observing a bounded kernel through its compiled flow

The standalone accept continuation observes the event log and exact use of the choice tape.
Returning a designated register observes its final value. External memory is recovered by
replaying the same log, provided the kernel records its writes faithfully.


### `Replays`

 A kernel records the actual external-memory effect of each successful run. 

### `Refines.kernel_of_exec`

 On a finite derivation's exact tape, a bounded refining kernel succeeds and returns
the same events, registers and external memory. 

### `Refines.kernel_iff_exec`

 Exact-use characterization, including rejected tapes. 
