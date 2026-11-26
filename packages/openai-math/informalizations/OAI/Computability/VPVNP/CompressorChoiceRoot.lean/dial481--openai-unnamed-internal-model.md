---
{
  "module": "OAI/Computability/VPVNP/CompressorChoiceRoot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceRoot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceRoot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native computation of the number of motif copies

Binary search on the integer interval from zero to the demand energy computes
the least integer whose square, multiplied by the fixed denominator, reaches
that energy. The search runs the same native instruction table for all inputs.


### `body`

 Registers 0 and 1 contain the numerator and denominator. Registers 2 and
3 hold the inclusive search interval, 4 and 5 hold one and two, and 6 and 7
hold the midpoint and its test score. 

### `root`

 Bisection includes the zero-energy case, for which the loop has no iterations. 

### `root_exec`

 Complete computation of the integral ceiling test with at most seven
instructions per binary digit of the numerator, including all loop tests.
Every recorded event is a private deterministic tick. 
