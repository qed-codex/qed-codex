---
{
  "module": "OAI/Computability/VPVNP/UniversalCountAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The circuit advice for the integer coefficient of the paired family

The same advice program verifies every input and candidate path of a given
length. It simulates the decoded machine on the full input, including its own
prefix, using the canonical zero-padded choices. The deterministic enumeration
thus computes the integer coefficient before reduction into any field.


### `verifierProgram`

 The gate instructions for checking a canonical path of the universal machine on an input of
length n, shared by every input and candidate path of that length. 

### `acceptingCount_le`

 The raw integer count fits even when every path branches and accepts. 

### `count_digits_value`

 Reading the final stack as a natural number retains the entire path count. 
