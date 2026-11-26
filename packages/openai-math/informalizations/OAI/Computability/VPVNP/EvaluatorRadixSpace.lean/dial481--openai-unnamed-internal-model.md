---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRadixSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRadixSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRadixSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Peak storage of the radix conversion

The exponent, divisor and requested number of rounds are all encoded on
stacks. Every instruction uses at most one additional bit. The exact
polynomial clock therefore gives a polynomial storage bound at every
intermediate point, including storage of the compact output digits.


### `radixRoutine_space`

 The bound holds for every intermediate configuration reached by the
routine. It depends on the divisor only through the length of its input
encoding. There are ten physical bit stacks. 
