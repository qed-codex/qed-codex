---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramCountPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramCountPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramCountPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual reclamation of node-work scratch before Hermite reconstruction.
The static port set includes both the native CRT work ports and the scalar/
polynomial arithmetic readiness ports, together with the reader temporaries. Runtime data are cleared by real
stack loops; persistent node and jet inputs remain outside this set. 

### `ports_gap`

 Ports between the native CRT bank and the explicit reader bank are not
cleared by count preparation. 

### `output_parked`

 The parked source/layout masters, including 730 through 743, survive. 

### `protectedInputs`

 In particular the actual ring metadata and the newly produced node/jet
streams survive the cleanup that establishes the CRT scratch condition. 
