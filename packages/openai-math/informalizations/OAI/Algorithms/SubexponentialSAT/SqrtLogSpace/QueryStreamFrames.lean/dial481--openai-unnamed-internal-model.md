---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryStreamFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryStreamFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryStreamFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Syntactic read and write exclusion for the actual streaming query.
The collector's remaining records and accumulated count stay opaque to the
conditioned query, so replay after changing those words uses the same steps. 

### `tuple_controller_avoids`

 This covers the actual fixed attained-signature DFS, including all
presence tests, cursor scans and frame manipulation. 

### `accepted_assignment_avoids`

 All accepted assignments use the actual fixed factor command; the
collector frame is excluded even from dispatcher and arithmetic reads. 

### `visitor_avoids_of_loader`

 The fixed visitor composes the actual two passes and all arithmetic
without any access to the suspended outer collector. 

### `visitor_avoids`

 The actual loader certificate closes the fixed visitor's only external
footprint obligation. 

### `command_avoids`

 Every instruction of the one fixed conditioned query excludes both
outer collector tapes, including all peeks and called instruction tables. 

### `shadow_eval`

 The shadow erases only proof-side caller data. The actual fixed query on
the original state executes exactly the same number of source steps. 

### `shadow_prefix_bound`

 Actual query prefixes retain the maximum of local storage and the opaque
collector frame, independently of the number of query or loop steps. 
