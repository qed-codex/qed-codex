---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Border/Surplus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Border/Surplus.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Border/Surplus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Geometric border rank

Take Zariski closure in the space of all three-tensor coefficients over
the algebraic closure, including the coefficients outside the multiplication
support. The Veronese span bound gives an exact decomposition of every
power at polynomial overhead. This overhead disappears in the limit.


### `BorderRankLE.asymptotic`

 In geometric border rank the decompositions can use the algebraic
closure. Specialization and field descent remove that scalar extension. 

### `ZClosure.cells`

 The product on any set of whole output cells pays at least for the
most nearly square rectangle of the same area. 


# Geometric border rank at the harmonic threshold

Choose the retained area as a product of rounded side lengths.
Trimming the longer side, or both sides equally at a square, makes
these the most nearly square lengths that fit at that area.


### `border_surplus`

 The border-rank half of the harmonic threshold corollary. 
