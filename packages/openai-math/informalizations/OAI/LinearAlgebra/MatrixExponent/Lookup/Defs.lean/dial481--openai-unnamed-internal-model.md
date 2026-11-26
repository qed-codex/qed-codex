---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Lookup/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Defs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sorting dictionary and query records

A dictionary row has its marker set and carries a count as payload. A query
row has zero padding. At a given key, all its queries precede the unique
dictionary row. The sorting hypothesis below concerns only inputs of this
form and requires the complete ordered output.


### `Sorting`

 The ordinary-width sorting bound restricted to dictionary and query rows.
The keys enumerate all addresses once in key order. The second sort key is
the dictionary marker. Identical query rows require no tie breaking. 
