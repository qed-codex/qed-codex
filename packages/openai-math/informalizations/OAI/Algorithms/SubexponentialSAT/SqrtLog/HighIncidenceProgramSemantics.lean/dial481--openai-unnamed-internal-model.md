---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The physical mask is exactly the finite incidence cutoff on original
variables. The theorem counts zero-degree variables in the ambient dimension. 

### `empty_scopes_mask`

 Empty scope families and unused variables produce low bits, not omitted
coordinates. In particular the physical output length remains n. 

### `suppliedScope_card_le`

 Even nonnormalized supplied records overcount rather than undercount mass.
This suffices for the high-dimension bound with the physically counted S. 

### `computed_high_dimension_rawMass`

 The threshold may be computed from raw entry counts. Duplicates or
out-of-range supplied IDs cannot invalidate the dimension estimate. 
