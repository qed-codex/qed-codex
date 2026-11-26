---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Routing/Control/Keys.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Control/Keys.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Routing/Control/Keys.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ordering disjoint blocks by local keys

Only the keys of nonempty blocks need to be distinct. In particular
unused centers do not need to be globally ordered.



# Addressing overlapping action balls

Two centers are neighbors precisely when they differ by a product
of two radius words, one inverted. A fixed list enumerates these
products, and its first occurrence of each label is used.



# The control metadata uses only a bounded orbit diagram

In particular, comparing two request tuples does not require forming
an array indexed by every possible tuple of global labels.



# A bounded local transcript of a whole schedule

A transcript records the initial stocks, the successive decisions
and the stocks after each round. The initial state and the local
update tests characterize the image of the branch encoding.



# Local allocation of copies

A request is held at the same home by all its users. Their common
ordering is given by the list of neighbors at that home.



# Designating one supplier per request

Use the first center in the common order at the request's home.
After this choice the route itself is fixed by the local shape.



# Computing allocation keys from local orbit observations

