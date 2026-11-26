---
{
  "module": "OAI/Computability/VPVNP/QueryClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clock and length bounds for compiled payload queries

Each query can scan the full input and then move at most the length of the
payload to reach the addressed bit. The literal table contributes enough
prefix bits for a cubic bound on the total number of steps.


### `queryPrefix_lower`

 The unary state-count header alone has one bit for each running state. 

### `querySteps_le_clock`

 The fixed clock of §1.1 allows a full scan and a payload traversal for
each query, plus the halting instruction. 

### `queryInputLength_le`

 A quadratic table encoding preserves polynomial bounds on the number of
queries, the number of query-program states, and the payload length. 
