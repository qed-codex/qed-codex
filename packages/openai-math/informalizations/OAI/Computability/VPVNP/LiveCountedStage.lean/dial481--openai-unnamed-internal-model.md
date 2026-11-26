---
{
  "module": "OAI/Computability/VPVNP/LiveCountedStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCountedStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCountedStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A native counted stage with a public or memory-resident bound

The guard reads the last public word as either the capacity or its external address.
Below that capacity the original table runs. At or above it the stage accepts,
so the enclosing stage linker can hand control to the next table.


### `shift`

 Shift only the jump destinations of a native instruction. 

### `counted`

 Guard the original table using a direct word or an external memory cell. 

### `publicData`

 Append the stage's bound or bound address as the final public operand of its worker. 

### `machine`

 Instantiate the counted wrapper and underlying worker with their public operands and the
selected bound mode. 

### `limit`

 Effective stop cursor, as it is read at the start of the current call. 

### `guardEvents`

 The guard log records an actual external read precisely for an indirect limit. 

### `prefixReport`

 Prepend the direct or indirect bound check's events to a worker report while retaining its
return state. 

### `execute_active`

 Four guard instructions precede the original call, with exact remaining fuel,
branch stream, memory effects, and returned word. 

### `execute_closed`

 At and beyond the limit, including an initial limit of zero, the wrapper
accepts the empty choice stream and rejects every nonempty stream. 
