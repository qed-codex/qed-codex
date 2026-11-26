---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Weighted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Weighted.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Weighted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Discrete weighted growth of three polynomial prices

Move the three widths from `n(A,B,C)` to `(n+1)(A,B,C)`. For each
pair of widths use both orders of the two increments. Their sum
allows the paired row estimates to be applied at each unchanged
width, both before and after the change. The harmonic lower bound
on the increments telescopes against a difference of logarithms.


### `Increments`

 Paired growth for the logs of two prices with the same first input. 

### `growth`

 If a potential grows by at least `v/(n+3)` at every step and is
at most `w log(n+3)+C`, then `v ≤ w`. 
