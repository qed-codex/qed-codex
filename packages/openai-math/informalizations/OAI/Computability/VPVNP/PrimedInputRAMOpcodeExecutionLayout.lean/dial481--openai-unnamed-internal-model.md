---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical primed input program refines the two-pass schedule

The single finite opcode table runs at the prescribed public parameters. Its data calls
add precisely three cut-length reads to the public item's probes. The four entry tests
and all dispatch arithmetic are private. The global correspondence uses only the invariant
on the three reserved length words, so it also applies to malformed primed message data.


### `nativeOps`

 The layout's sequence of first-pass bit choices and second-pass copies, using the native
encoding of a Boolean as a word. 

### `nativeMachine`

 Instantiate the fixed two-pass opcode table at the layout's word width and public parameter
words. 

### `nativeFuel`

 Per-call instruction allowance for the native input program, equal to `3*r + 165` for an
`r`-bit site index. 

### `native_body`

 Execute the input body from arbitrary private registers. This allows the combined
counter to enter it from its own phase dispatch without changing any public item. 

### `native_data`

 Each valid data call has its native event list, with one common private dispatch
cost for both possible values of the selected bit. 

### `physicalSchedule`

 Refinement by the fixed physical program of every scheduled owner and copy call. 
