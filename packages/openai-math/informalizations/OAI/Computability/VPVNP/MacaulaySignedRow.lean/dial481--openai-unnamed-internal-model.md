---
{
  "module": "OAI/Computability/VPVNP/MacaulaySignedRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySignedRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySignedRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native read of a shifted integer equation in the Macaulay matrix

The reader decodes both monomials, checks divisibility, and, on its true
branch, counts the signed coefficient at their coordinatewise difference.
The reader restores its flag and residual buffer after returning the scalar.


### `signed_row`

 The complete guarded original-row phase on the ordinary reader advice. 

### `signed_row_plan`

 A single reader plan supplies the scan, temporary-buffer and counted
coefficient budgets before the matrix entry is selected. 
