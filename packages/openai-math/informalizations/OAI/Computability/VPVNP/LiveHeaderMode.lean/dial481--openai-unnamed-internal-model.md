---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderMode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderMode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderMode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native live-mode dispatch of Section 14.1

Processor zero supplies the mode at each nonempty incident cut in header
slots 2 and 3. A boundary group reads its one incident mode. An interior
group rejects unequal modes. The result tag selects the unit check, the
primed pair, or the evaluator tail.


### `Tag`

 The three live continuations selected by cut-mode agreement and group phase. 

### `Tag.code`

 Encode the unit, pair, and evaluator-tail continuations as machine tags zero, one, and two. 

### `selectTag`

 Choose unit mode for a cleared mode bit, otherwise select pair or evaluator tail according
to the group half. 

### `selected`

 Both-empty is outside the chain domain and is rejected. 

### `prepare`

 Public words 0 through 3 give the scratch addresses of the left and
right lengths, first-half flag and output tag. The packed site header is at
address zero. Registers 10 and 11 receive its two mode bits. 

### `chooseMode`

 Select a mode in register 12, checking nonemptiness and agreement. 

### `emitTag`

 The chosen tag goes into register 13 and the designated scratch word. 

### `program`

 The native routine that checks the applicable incident mode bits and publishes the
resulting continuation tag. 

### `program_length`

 The instruction list and register count are independent of the chain length. 

### `once_of_exec`

 A successful derivation of a deterministic acyclic block must be the
one computed by the straight-line interpreter. 

### `events`

 The trace has four reads, one tag write, and no nondeterministic choices.
Its length is at most 24, including both comparison tests at an interior cut. 

### `exec_selected`

 The executable mode block reads the packed word and dispatches to its
unique tag in at most 24 events and exactly five probes. 

### `native_selected`

 A correctly selected tag is written by the compiled standalone call.
The normal exit hands control to the next stage of a linked live program. 

### `native_rejected`

 Unequal modes on two nonempty cuts, or two absent cuts, reject at every
fuel bound and for every supplied list of choices. 
