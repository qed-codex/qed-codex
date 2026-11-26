---
{
  "module": "OAI/Computability/VPVNP/CompressorTransferredStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTransferredStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTransferredStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All eight startup reports of the compressed pair

Every report uses the memory left by the previous report and its linker tag
write. The state passed to the online stage carries its controller bank, the
persistent cursor operands and the natural history-arena bounds.


### `Trace`

 The two successive groups of startup reports that prepare the cursor frame and initialize
the calendar. 

### `Trace.frame`

 First four reports, which prepare and copy the cursor operands into the active frame. 

### `Trace.calendar`

 Last four reports, which compute the stride, install the arena and bank, and arm the
  calendar. 

### `Trace.source`

 All eight native startup reports indexed in execution order. 

### `Trace.entry`

 The nine boundary memories before, between, and after the eight startup calls, including
linker tag writes. 

### `trace`

 Construct the startup reports, beginning the calendar initialization in the memory produced
by the frame transfers. 

### `Runs`

 Both groups of native startup calls run, with calendar initialization using the
post-transfer cursor memory. 

### `run`

 The pair performs the eight source calls with the actual intervening
transfer writes. A lower tag address and a fitting descriptor allocation
suffice independently of the contents of the incoming memory. 

### `Runs.output`

 The exact native post-memory, including the tag transfer to stage eight.
The first header retains the natural arena base, level count and input length. 

### `eventually_run`

 One length threshold covers the complete physical startup, for every
incoming memory and every linker tag preceding the polynomially bounded
workspace. Only the eight compiler constants and the live dimensions enter
the source instruction tables. 
