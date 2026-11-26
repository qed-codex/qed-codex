---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering the evaluator's functional from its advised polynomial

Choose the minimal polynomial of the same power-basis generator used by the
evaluator. The quotient isomorphism sends the formal root to this generator,
so reading the first coefficient of an encoded field element computes the
prime-field coordinate used by the branch counter.


### `primeCoordinate`

 The low limb is the output of the final prime-field coordinate query. 

### `exists_compatible_advice`

 Select one binary description and one field isomorphism that realize
the evaluator's specified coordinate on all coefficient vectors at once. 
