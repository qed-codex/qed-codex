---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One coefficient of a Horner round on bit stacks

The evaluator computes the shifted predecessor plus two scalar products.
It uses registers 0 through 5 for the modulus, predecessor, negated top
coefficient, modulus coefficient, Horner digit and multiplier coefficient,
respectively. Register 6 receives the result and register 7 holds the second
product. The same control works at every coefficient and every word width.


### `row`

 Execute the four modular operations for one Horner coefficient, leaving its result in
register six. 

### `rowRegisters`

 The two destination registers at the end of a row calculation. 
