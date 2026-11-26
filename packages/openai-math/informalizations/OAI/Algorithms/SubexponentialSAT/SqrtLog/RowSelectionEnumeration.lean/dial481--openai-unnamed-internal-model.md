---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RowSelectionEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit mixed-radix enumeration and deterministic maximal-minor scan.
The enumeration includes repeated indices; their zero determinants are harmless.
Its cost is counted separately from primitive-machine implementation. 

### `candidateAt`

 Explicit tuple indexing, with no noncomputable finite enumeration. 

### `candidates`

 Every size through K is examined, in increasing mixed-radix order. 

### `choose`

 Preserve the earlier candidate on ties. 

### `select`

 Actual deterministic selection, depending only on the matrix and rank cap. 
