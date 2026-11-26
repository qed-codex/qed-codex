---
{
  "module": "OAI/Computability/VPVNP/VerifierWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierWeight.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arithmetic formulas for a Boolean verifier's transcript

A reference reads either a Boolean constant, an input variable or a proposed gate
value. With all transcript values provided as variables, checking one AND or NOT
gate takes eight binary arithmetic operations and has syntactic degree at most
three. The final acceptance test multiplies this product by the output bit.


### `Program.checkFormula`

 Product of local consistency tests for the proposed gate values. 

### `Circuit.weightFormula`

 Formula for the product of all gate tests and the designated output. 
