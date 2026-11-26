---
{
  "module": "OAI/Computability/VPVNP/RankQueryTimeBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryTimeBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryTimeBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A uniform singly exponential clock for the physical rank scan

The bidegree rectangle has at most six times the cube of the common input
bound. Within each cell the logarithmic Schur recursion gives a singly
exponential number of steps. Loading the root, checking the resulting scalar,
and moving the cursor add polynomial overhead in the word widths.


### `rankTime_le_exp`

 One bound on the six physical size parameters suffices for the complete
rank query over a rectangular matrix, including every index update. 
