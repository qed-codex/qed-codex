---
{
  "module": "OAI/Computability/VPVNP/EvaluatorProgramInputBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramInputBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorProgramInputBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Advice and clock bounds for the evaluator with its input parser

A fixed list of polynomial-length callback registers gives polynomial advice
for the whole program. The parser reads a runtime stream linear in the number
of exponent bits. Its cost fits the same exponential-in-length,
polynomial-in-exponent-width clock as conversion and traversal.


### `parser_budget_le_exp_poly`

 Add the parser clock to the full machine allowance. The exponent-array
width changes only the polynomial factor, and the bound is uniform over
binary inputs of that width and the index path. 

### `parser_schedule_le_exp_poly`

 The exact reader cost on a given input is bounded by the same clock. 
