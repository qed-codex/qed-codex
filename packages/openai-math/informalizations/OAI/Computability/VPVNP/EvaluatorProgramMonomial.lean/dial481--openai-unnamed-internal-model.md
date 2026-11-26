---
{
  "module": "OAI/Computability/VPVNP/EvaluatorProgramMonomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramMonomial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramMonomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The monomial scheduler on binary advice and exponents

Loading the self-delimiting fields, converting the native binary exponents
to radix digits, and traversing those digits are fixed controls. This links
their semantics to the chronological matrix-choice effect on the input
exponents. The callback specifications concern the two matrix steps.


### `nativeMachine`

 The radix converter followed by the monomial scheduler with the supplied Frobenius and
label-multiplication callbacks. 

### `rawMachine`

 The complete monomial routine that loads the tagged raw input before executing the
converter and the two scheduled callbacks. 

### `native_realizes`

 The native little-endian exponent array reaches the chronological
Frobenius and label action sum. Its exact conversion time precedes the
scheduler's per-path budget. 

### `raw_realizes`

 The whole parser, radix converter, and scheduler start with just the
single advice-and-exponent stream on the input stack. 
