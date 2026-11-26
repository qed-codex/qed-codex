---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramReadout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramReadout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramReadout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `readoutWorkPorts`

 Readout work stays below the persistent source and arithmetic metadata. 

### `readoutPorts`

 Readout uses only its named arithmetic inputs and reserved work tapes. 

### `readout_eval`

 Relocate the actual native readout. It changes only output102 among
caller tapes, so node caches, jet-shape104, and the sparse answer166 survive. 

### `readout_machine_eval`

 Concrete assembly-to-dense-jet boundary on the final 40/768 workspace. 

### `denseProgram_run`

 Full moment assembly followed by physical dense Z-jet readout. All
remaining premises concern actual input encodings and the paid assignment
producer; no precomputed sums, products, or projected jets are accepted. 
