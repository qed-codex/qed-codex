---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Specialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Specialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Specialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Specializing a rank decomposition

A maximal ideal containing the kernel of polynomial evaluation at the
decomposition coefficients preserves all their equations. Over the integers
the residue field is finite. Over a base field it is a finite extension.


### `finite_field_of_finiteType`

 A field finitely generated as a ring is finite. 

### `finiteTypeWeighted`

 Rank witnesses over a field can be realized over a field of finite type
over any base ring mapping into the given field. 

### `specializeRank`

 Specialization preserves all three side lengths and the number of summands. 

### `finiteExtensionRank`

 A rank bound over an arbitrary extension holds over some finite extension. 
