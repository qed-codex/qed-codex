---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Coloring/Run.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Run.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Run.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Comparing the sizes of two colour classes 


# Halving multiplicities with bounded counters

The counters never overflow. A unit is added only at an odd edge of
the chosen colour, after dividing the previous count by two.



# Computing a perfect matching

The degree and support are fixed. Append dummy edges, initialize bounded
counters, halve repeatedly, then retain real edges with final count one.



# Circuits for the full edge colouring

Both halves of a bisection occupy one array. The circuit carries
only the two decision bits per edge around the recursive call. Each
level adds one bounded polynomial overhead to the total cost.



# Cost of the three permutation controllers

Fixed chart tables are read in parallel. A colour determines an offset
in a fiber. Two permutation inversions and two more reads suffice to
construct all three factor lists.

