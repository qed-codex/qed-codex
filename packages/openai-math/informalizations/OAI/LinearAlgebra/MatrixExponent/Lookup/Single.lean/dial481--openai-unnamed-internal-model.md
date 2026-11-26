---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Lookup/Single.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Single.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Single.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Uniqueness of the guessed multiplicities and their product 


# Simultaneous evaluation at all query positions

One sorting call handles query rows and a fixed dictionary carrying
guessed counts. The trace contracts the count wires with binary weights.
Exactly one assignment passes the scan, including in positive characteristic.


### `lookup_net`

 The constant is uniform over extensions, table arities and entries. 
