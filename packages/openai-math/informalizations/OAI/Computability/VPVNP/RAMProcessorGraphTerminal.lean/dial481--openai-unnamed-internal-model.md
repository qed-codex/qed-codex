---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGraphTerminal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphTerminal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphTerminal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rejecting halts in the compiled site processor

A failed format, credit, or consistency check can halt inside an embedded routine.
Its literal rejecting row survives compilation of the graph and attachment of the
site prelude. Its path contributes zero and stops within one tick of reaching that row,
for every continuation of the enclosing program.


### `Routine.Rejects`

 A literal rejecting halt in the routine's own control space. The endpoint
has a named instruction so that it still halts when the routine is linked. 

### `Routine.Rejects.verdict`

 A deterministic path into a rejecting row stops, independently of every
normal-return continuation. 

### `Routine.Runs.then_reject`

 A normal first return enters a second routine's literal rejecting row. 

### `FiniteRoutine.reject_ofStackCode`

 The normal labels of the input code must be accepting halts. This makes
every literal rejecting row of the source an interior row of the compiled routine. 

### `graphRoutine_reject`

 The named rejected row of the complete burst graph is also a rejecting
row in the corresponding finite routine. 

### `callSite_reject`

 Include the boot steps that allocate and stage the physical record fields. 

### `callSite_reject_verdict`

 A failed call-site run has count zero under every continuation and a uniform
stopping bound, including the final instruction that observes the rejecting halt. 
