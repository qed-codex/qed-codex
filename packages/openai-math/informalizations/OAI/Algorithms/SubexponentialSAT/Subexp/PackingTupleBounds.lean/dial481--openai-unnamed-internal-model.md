---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingTupleBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingTupleBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingTupleBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds for the actual tuple tables used by packing

These estimates use the concrete framed record encoding and the executable
Cartesian-power recurrence.  The cost bound includes an empty alphabet.


### `generated_powerCost_le`

 The generated-table bound is valid also when no alphabet record exists.
In that case the first expansion empties the table, and subsequent iterations
have the exact linear cost shown above. 
