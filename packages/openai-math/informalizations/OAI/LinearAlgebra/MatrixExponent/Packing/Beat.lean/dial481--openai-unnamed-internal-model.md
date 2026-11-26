---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/Beat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Beat.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Beat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Quantitative reduction bounds for one subround and one reset 

### `mass_step`

 Each elementary step adds exactly the old bit incidences. 


# Choosing the number of subrounds and the rotor

Choose a sufficiently small tagged-permutation exponent, then let the
number of subrounds grow in fixed strides. The address length grows
exponentially in the number of strides. Its small power grows as
`2 ^ i`, which the contraction absorbs geometrically.


### `frequent_tag`

 Either source of inexpensive rotors supplies arbitrarily large
address lengths with a polynomially bounded payload. 

### `choose_rotor`

 Choose the contraction count from the available address length.
Even an arbitrarily sparse sequence of good lengths suffices. 


# Reduction of core width

Use a fixed number of contracting subrounds followed by a degree
reset. Choose the rotor large enough for the degree at the last
subround and cheap enough for the contraction to absorb its cost.


### `beat`

 Core width is halved up to the frozen charge and slack. The overheads
are uniform across field extensions and depend only on the incoming
core degree and the ground field. 

### `Reduction.iterate`

 Repeat a fixed beat while keeping both rates and the subdivision explicit. 

### `beats`

 Iterate with a bounded additive loss and only exponential growth
of the subdivision, load and full-degree exponent. 
