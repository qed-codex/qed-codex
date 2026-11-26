---
{
  "module": "OAI/Computability/VPVNP/RankQueryDescribeAdapter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryDescribeAdapter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryDescribeAdapter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Executable Schur description on a Macaulay relation matrix

The engine's describe action reads the current six-field query, evaluates its
fixed decision tree, selects an arm by the actual output tag, and returns
either a packed scalar or the loop counter and a fresh accumulator.


### `entryArm`

 Interpret a description tag by setting up a recursive sum, returning field zero or one, or
reading a Gram entry with the indicated sign. 

### `describeWith`

 Stage the current Schur query, run the description decision tree, and dispatch on its
three-bit tag using the supplied signed-entry routine. 

### `describe`

 Describe one Schur query using the physical Gram-entry routine backed by the Macaulay
matrix reader. 

### `timeWith`

 Step bound for one description dispatch when a signed Gram-entry call costs at most T
steps. 

### `clock`

 Step bound for the physical description dispatch when each underlying Macaulay entry read
costs at most B steps. 

### `describe_entries`

 Physical execution contract for the engine's describe action. Its only
matrix-dependent subprogram computes an individual Macaulay entry. 
