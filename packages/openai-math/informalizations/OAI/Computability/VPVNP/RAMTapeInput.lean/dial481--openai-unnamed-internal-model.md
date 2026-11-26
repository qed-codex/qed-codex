---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform finite-stack parsing of the physical site tape

After the public field lengths are available as unary scratch counters, the
control copies the self-delimiting prefix, the site address, its four header
bits and the whole incident vector, then consumes the zero padding. The control
and its register set are fixed across all lengths.


### `parse`

 Sequential reader. The address and incident lengths are popped from their
own counters and the fixed four header marks are written by the control. 

### `result`

 Bank after parsing, with the prefix, address, header, and incident bits on separate stacks
and the measured size preserved. 

### `parse_runs`

 Correct on all data-field values and all lengths of zero padding. Unused
scratch data are cleared, while the full literal prefix is saved in order. 

### `prepared`

 The local parser begins with its entire tape at the input head. The size
and field counts can have been produced by previous routines on these stacks. 

### `parse_processorTape`

 A linear stack-instruction bound for parsing the literal physical tape.
The successful run exposes the exact incident vector used by the word machine. 
