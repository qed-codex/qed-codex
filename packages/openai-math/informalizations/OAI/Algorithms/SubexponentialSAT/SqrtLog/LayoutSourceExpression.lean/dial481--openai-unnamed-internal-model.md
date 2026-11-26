---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourceExpression.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourceExpression.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourceExpression.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Degree certificates for the actual typed literal and interpolation-row
sources. These remove the full-polynomial cutoff premise at R+1. 

### `literal_code`

 A native scalar literal is exactly one typed coefficient cell. 

### `literal_evaluate_full`

 The full cutoff is discharged even for the actual zero and one literals. 

### `source_row_degree`

 Any exact source-row witness inherits the audited full source degree. 

### `source_row_evaluate_full`

 No separate degree assumption remains at the source's R+1 cutoff. 

### `typed_row_contract`

 Concrete native table values give a typed expression of degree at most R,
and evaluation at R+1 recovers the complete source polynomial. The degree
conclusion is derived here, not supplied by the caller. 
