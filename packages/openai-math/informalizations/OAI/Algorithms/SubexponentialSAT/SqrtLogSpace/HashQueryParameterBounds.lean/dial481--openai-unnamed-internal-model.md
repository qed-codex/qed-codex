---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryParameterBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryParameterBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryParameterBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual trial and accepted queries inherit the width-fixed scalar caps.
Every generic validity and raw-scope premise is discharged from the literal
formula, produced code rows, attained history and physical master words. 

### `trial_numeric_caps`

 Fixed-before-input scalar caps for the literal trial query. Numeric
values are bounded independently of arbitrary physical padding. 

### `accepted_numeric_caps`

 Fixed-before-input scalar caps for the literal accepted query. Numeric
values are bounded independently of arbitrary physical padding. 

### `trial_frontend_budget`

 The actual marked frontend reads only its six source words. The suspended
collector tail and accumulator remain unrestricted in this time bound. 

### `accepted_frontend_budget`

 The final unmarked frontend receives only the attained history. Its
capacity and running-time envelope use actual source bytes, never query time. 

### `trial_envelope`

 The same literal trial query and actual complete output alphabet
inherit the original resource envelope. All constants and the cutoff precede
the formula, attained history, candidate, mark and physical parameter words. 

### `accepted_envelope`

 The same literal accepted query and actual complete output alphabet
inherit the original resource envelope. All constants and the cutoff precede
the formula, attained history, candidate, mark and physical parameter words. 
