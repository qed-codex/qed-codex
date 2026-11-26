---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderBounded.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBounded.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBounded.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A public cursor bound for a native stage

Three local instructions compare the persistent cursor with a public capacity.
Below that capacity the original table runs. At or above it the stage accepts,
so the enclosing stage linker can hand control to the next table.


### `shift`

 Shift only the jump destinations of a native instruction. 

### `bounded`

 Wrap a worker in a public cursor-bound check that accepts when its capacity is reached. 

### `publicData`

 Append the stage's capacity word to the worker's original public operand bank. 

### `machine`

 Instantiate the cursor-bounded worker on its original operands and supplied capacity. 

### `execute_active`

 The only overhead on an active call is three ticks. The original choices,
probes, result, and remaining fuel have their exact native semantics. 

### `execute_closed`

 At the capacity the unique successful input is the empty choice string. 
