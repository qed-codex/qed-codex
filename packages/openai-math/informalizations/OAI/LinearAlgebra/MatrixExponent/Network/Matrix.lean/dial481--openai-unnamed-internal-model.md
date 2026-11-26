---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Network/Matrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Network/Matrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Network/Matrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `Representation`

 A matrix encoding on binary indices. Padding by zeros preserves products
but need not preserve the identity matrix on unused indices. 

### `exists_representation`

 Use the regular representation and pad the complementary block with zeros.
Any active diagonal index recovers base-field elements. 


# Returning a trivalent network to its ground field

A matrix index passes through the original vertices in sequence. Parallel
composition concatenates two chains, and trace sums the original wires. A
single additional table selects the distinguished index at both ends.


### `Chain`

 The first branch handles empty networks without allocating an index.
Every nonempty chain reserves enough vertices to pin its ends once. 

### `Net.descend`

 A trivalent network of ground-field values descends without changing any
exterior positions. The bound counts vertices and also holds when both sides
count the common exterior arity. 
