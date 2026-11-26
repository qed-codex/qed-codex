---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word-level correctness of the rectangular input dispatcher

The opcode table compares each flat position against the prefix, address,
header and incident-port boundaries. It returns a literal or a source address
together with the bit's first-pass owner flag. Only private register operations
are performed between the parameter loads and the final choice or copy.


### `DispatchInput`

 Values required at dispatch entry, including the packed literal prefix
and the arithmetic bounds for the exclusive ends of the input fields. 

### `DispatchOutput`

 Registers 26, 27 and 28 return the payload, fetch flag and owner.
All registers below 32 other than temporary offset 25 have their specified
field-result values, including the next cursor and write destination. 

### `dispatch_exec`

 The complete dispatcher computes the paper's scalar decision with
finite word instructions. Its trace has no external probes and uses only
private ticks, even at a missing port or on inconsistent message data. 
