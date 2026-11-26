---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorTableBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorTableBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorTableBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed polynomial bounds for the actual factor-table service. The scalar
allowance includes physical signed-word lengths; it never bounds the integer
value of an exponential modulus or numerator in unary. All ambient source
rows and every specialized incidence record are included. 

### `sourceEnvelope`

 State-independent allowance for every actual ambient source row. 

### `source_work_polynomial`

 Constants and degree precede every runtime source parameter and word. 

### `payloadEnvelope`

 Full normalized payload width, before inserting its framed table record. 

### `tableEnvelope`

 Includes the complete ambient loop, its growing table and export cleanup. 

### `serviceEnvelope`

 A local prefix allowance and compact retained table allowance together.
This is a fixed polynomial in scalar and physical-word caps, not total query time. 

### `table_service_polynomial`

 The same fixed coefficient and exponent bound the actual table call time,
its all-stack prefix allowance and the full compact table retained at return. 

### `payloadEnvelope_polynomial`

 Public fixed-polynomial certificates for composing physical caps. 
