---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BlockRecursion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BlockRecursion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BlockRecursion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recursion on blocks and zero padding

A recursive call may have inputs that are already computed values. Work over
an arbitrary algebra `K` with only the constants of `F` supplied for free,
then instantiate `K` with the polynomial ring of the padded problem.


### `multiplies_step`

 First form two families of linear combinations, then compute and
recombine the `r` smaller matrix products. 

### `integral_power_cost`

 A rank witness gives a cost recurrence valid up to each power of the
block dimensions. The overhead grows with the largest of the three areas. 
