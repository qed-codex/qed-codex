---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLocalCorrectionAlgebra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLocalCorrectionAlgebra.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLocalCorrectionAlgebra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Semantic invariants for the fixed-width local CRT preparation. Every
intermediate polynomial product may be truncated to D coefficients. The
constant coefficient is inverted once by the executable residue algorithm. 

### `repeatProduct`

 Tail-recursive repeated multiplication, with one cached accumulator. 

### `localProduct`

 Scan the supplied other nodes and multiply each local linear factor D
times. This is the value-level schedule of the physical node/power loops. 

### `correctionFromLoop`

 Finish the local inverse and multiply it by the supplied jet. 

### `computed_constantInverse`

 The computed inverse of the truncated local factor's constant term is
also the exact constant inverse required by the established CRT formula. 
