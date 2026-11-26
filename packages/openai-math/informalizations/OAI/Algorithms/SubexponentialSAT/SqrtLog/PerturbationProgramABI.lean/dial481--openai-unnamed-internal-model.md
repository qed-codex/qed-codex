---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramABI.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramABI.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgramABI.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical interchange format for prepared incidence rows. Coefficients are
fixed-width extension-ring words; keys contain unary exponents and n support
bits. The outer variable key is Encoding.encodeNat v, matching the hash lookup.
This file also discharges primitive emission of each output record. 

### `dictionaryBits`

 No outer list markers: one framed key and one framed coefficient per item. 

### `incidenceRecordBits`

 Each hash selects its own incidence slice; only v appears in this key. 

### `emitRecord_trace`

 Concrete primitive bit execution: the fixed program is independent of n,
d, B, J and all coefficient values. Input words are reversed as required by
streaming prepend; their preparation is a separate paid stage. 

### `emitRecord_budget`

 A kept output atom costs polynomially many primitive transitions to emit. 
