---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The triangular convolution controller charges actual fixed-width reads,
copies, and cell writes. The local pair contract is a contract for a fixed
finite command and is instantiated by the concrete quartic/jet service. 

### `PairSpec`

 An actual pair-command contract. Only one local multiply-and-accumulate
operation is assumed here, at an in-bounds output cell, with explicit cost. 

### `innerStep_run`

 One iteration of the actual inner command, including every data movement
and the physical increment of the output index. 

### `innerLoop_run`

 The complete inner loop executes exactly the triangular row, with all
field data, scratch use, and per-pair work accounted for by actual commands. 
