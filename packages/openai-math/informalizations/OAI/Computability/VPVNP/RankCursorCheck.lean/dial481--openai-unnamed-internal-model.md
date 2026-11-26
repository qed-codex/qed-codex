---
{
  "module": "OAI/Computability/VPVNP/RankCursorCheck.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorCheck.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorCheck.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Checking one Schur coefficient and rolling the rank registers

After the root query returns, the zero test scans the field element in its
polynomial-basis representation. Its bit feeds the cursor update directly.
The check erases the coefficient and reuses the same registers on the next
root query.


### `check`

 Consume the scalar result, roll the two binary cursor words, and emit
the control bit for the next iteration. 

### `checkClock`

 Step bound for testing the packed Schur coefficient for zero, clearing the scalar, and
advancing the rank cursor registers. 

### `check_runs`

 The rank registers and the entire engine bank are reusable after the
scalar check, including the full polynomial-basis zero test in characteristic two. 
