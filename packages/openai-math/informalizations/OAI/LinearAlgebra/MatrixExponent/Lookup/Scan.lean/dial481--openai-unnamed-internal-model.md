---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Lookup/Scan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Scan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Scan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Grouping the queries gives a sorted permutation of the input rows 


# Scanning dictionary rows

Two adjacent blocks share only a counter and a validity bit. Joining their
networks along those wires avoids copying either block of rows.



# Ordering the dictionary and query rows

Read a key's wire positions in a fixed order. After the key comes the
dictionary marker, then the count payload. The marker places every query
before the dictionary row for that same key.



# From tagged permutations to sorting dictionary and query rows

At height `w=t+1` the payload has exactly `2w` bits. A sort on whole
rows suffices since the query payloads are all zero and the dictionary
has only one row for each address.

