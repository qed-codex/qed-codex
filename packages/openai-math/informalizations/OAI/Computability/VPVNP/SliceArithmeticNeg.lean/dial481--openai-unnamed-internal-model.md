---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticNeg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticNeg.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticNeg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Destructive negation of a packed field scalar

The caller holds the input scalar in the accumulator and an empty query stack.
A copy of the scalar supplies the second input stream of the coefficientwise
scan. Each row computes the modular negation of the first input. The scan
consumes the copy and returns the negated scalar on the accumulator stack.


### `machine`

 Negate the packed accumulator coefficientwise using a private copy on the query port. 

### `value_neg`

 The destructive operation realizes the additive inverse in the quotient ring. 
