---
{
  "module": "OAI/Computability/VPVNP/StructuredStackLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact instruction costs of a structured stack loop

An empty pop returns immediately. A nonempty pop spends one instruction before
entering its body, whose normal return either finishes the loop or resumes at
the next pop. The bodies may use any of the stacks, including the stack scanned.


### `popLoop_empty`

 The terminating empty pop preserves the stacks. 

### `popLoop_continue`

 A continuing iteration costs one pop plus the body and the remaining loop. 

### `popLoop_stop`

 The final nonempty iteration costs one pop plus the body. 
