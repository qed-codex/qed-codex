---
{
  "module": "OAI/Computability/VPVNP/TensorRestrictionSemiring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorRestrictionSemiring.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorRestrictionSemiring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The restriction semiring on a finite party set

The direct sum and parallel tensor product of arrays make their mutual
restriction classes into a commutative semiring. The natural number `n`
is represented by the all-party diagonal with `n` entries. A nonzero array
restricts to the unit, and the product of its local dimensions gives a
natural number that restricts to the array. These are the order bounds
used in Appendix A.1 of *VP and VNP differ over every field*.


### `instance : NoZeroDivisors (RestrictionClass k J)`

 Nonzero coefficient witnesses in the two factors combine into one in their product. 

### `orderBounds`

 Rank bounds and monotonicity under independent restrictions supply all
the order hypotheses of strict spectral comparison. 
