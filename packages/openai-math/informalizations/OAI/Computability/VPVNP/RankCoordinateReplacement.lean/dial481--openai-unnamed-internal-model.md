---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateReplacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateReplacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateReplacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The numerator reader for a Cramer minor

The comparison aliases the caller's dense row address and reads the
replacement ordinal from a separate register. The selected scalar reader
therefore receives the usual two addresses. Its result is the target scalar
precisely on the replaced row. The ordinal and comparison workspace are
ready again at every return.


### `Work`

 Two comparison registers and the scalar-reader workspace used to recognize the replaced
row. 

### `Port`

 The public matrix-entry reader ports together with the row-replacement workspace. 

### `workBank`

 At entry, the row supplied by the caller is register zero. The second
comparison register holds the ordinal computed by the enclosing query. 

### `set_replacement`

 Installing a new ordinal into its designated stack preserves all other
workspace and advice. 

### `Ready`

 The scalar reader’s auxiliary bank is ready, register one holds the width-w replacement-row
ordinal, and the local register-zero stack is empty because comparison reads the caller’s
row port. 

### `numerator`

 The replacement ordinal is a runtime input to this fixed routine. 

### `correctSpace`

 Supply the target row as a scalar reader of the constant-row matrix.
Both arms may update the auxiliary state on return. Every address comparison
and each selected arm respect the stated cap, independent of their running time. 

### `submatrix_correctSpace`

 Assemble the Cramer numerator from the ordinal selectors and two raw
scalar reads. The target reader receives the selected original column on its
column port. Its row input is immaterial for the constant-row target matrix. 
