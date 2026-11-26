---
{
  "module": "OAI/Computability/VPVNP/OracleBinaryTarget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OracleBinaryTarget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OracleBinaryTarget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparing a queried exponent against a count register

One static Boolean expression per possible count compares the query's binary
digits with the fixed count. Values exceeding the number of available flags
therefore produce a zero target row and are rejected by the row-count circuit.


### `expr`

 Boolean equality test between the wired binary word and the natural-number target,
returning false when the target exceeds the word's range. 
