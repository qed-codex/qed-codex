---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionResult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionResult.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionResult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical input assembler for the two primed groups

The fixed opcode table, started in the prescribed header memory, has one
accepting native path per internal bit assignment. Every parser leaf receives
the corresponding tape bit. Three cut-length reads on each of the two visits
to a rectangular position increase the total cost by exactly six per position.


### `native_cost_bound`

 The exact cost is the scheduled cost plus three length reads at each data
call. The same uniform upper bound applies to every assignment and memory. 

### `nativePathEquiv`

 Histories of the actual fixed opcode machine enumerate the shared internal
bits in the two primed groups. The auxiliary RAM's caps include its header reads. 

### `nativeRun_matches`

 The opcode report list and the semantic input-pass reports carry the same
memory updates and cursor returns, with three additional probes per data call. 

### `nativeRun_preserves_header`

 Every address below the scratch rectangle is preserved, including histogram
entries reserved there and all three cut-length words. 

### `nativeRun_input`

 Every actual opcode run writes the selected internal assignment's exact
primed input bit at each physical site and tape offset. 

### `nativeRun_cost`

 Exact and uniform bounds for the native reports of any accepting opcode
history, without first imposing a cost cap on that history. 
