---
{
  "module": "OAI/Computability/VPVNP/RankCursorLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The physical descending scan for the rank query

A successful coefficient query and cursor update leave one continuation bit.
The loop requests the next pair when this bit is true and returns the rank
already stored by the update when it is false. No loop bound or matrix
dimension is part of the finite control.


### `State.continues`

 The initial and continuing states of the rank scan carry a true flag. 

### `scan`

 Invoke the coefficient-and-update routine at each true mark. Its normal
return supplies the flag read by the next iteration. 

### `scan_runs`

 A physical step preserves the encoded cursor and advances it according
to the coefficient zero test. This yields a complete finite run, with a
bound uniform over every rectangular coefficient query. 

### `matrix_scan_runs`

 With the Schur coefficients this control returns the ordinary rank over
any field, including characteristic two. 
