---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dynamic-degree coefficient arithmetic

These executable callbacks operate on a runtime-sized coefficient vector.
Their counters include all scalar callbacks and one event per vector/list
entry. A separate flat-stack refinement must account for scanning serialized
vectors; callback event counts alone are not claimed to be primitive time.


### `sumRun`

 Evaluate and sum a list of measured scalar computations. 

### `tabulateRun`

 Tabulation explicitly charges one event per output coefficient. 

### `tripleRun`

 Two scalar multiplications, with both measured costs retained. 
