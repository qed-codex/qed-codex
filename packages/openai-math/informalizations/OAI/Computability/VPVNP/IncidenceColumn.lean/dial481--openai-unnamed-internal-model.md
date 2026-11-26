---
{
  "module": "OAI/Computability/VPVNP/IncidenceColumn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceColumn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceColumn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a column of the exact-one incidence matrix

On a pass for row `r`, the column parser increases its capped tally precisely when
the column is selected and its incidence bit for row `r` is set. The scan consumes
one tick per encoded bit and leaves the head at the following tag.


### `partialCount`

 The count after reading the first `j` row bits of one column. 

### `scanColumnBits`

 Starting at row bit `j`, read the rest of the column and return to the tag state. 

### `runColumn`

 Reading a column adds its selected incidence bit to the capped row count. 
