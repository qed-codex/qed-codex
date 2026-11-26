---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationBetaProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationBetaProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationBetaProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native beta evaluation.  The caller supplies actual coefficient arrays,
not evaluated row values.  Masters205..212 are preserved;220 is the result.
Work230/231/232 holds the framed row scan, choice scan and reverse buffer. 

### `readRow`

 Consume the outer list tag and physically decode one coefficient array. 

### `lowFrame`

 All changed ports are above the persistent native arithmetic region. 

### `selected`

 Evaluate the current actual row, then add it to the existing beta. 
