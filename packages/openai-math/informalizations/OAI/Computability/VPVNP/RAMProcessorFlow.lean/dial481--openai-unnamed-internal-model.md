---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorFlow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorFlow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorFlow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linking burst-processor stages with named exits

The call interpreter must return to one of several program counters, request
an external read or write, or finish its call. A fragment's local rows can
name both local continuations and arbitrary exits. Linking selects the entry
of the destination immediately, with no added step on these transfers.


### `Fragment`

 A finite stack-code block whose instructions can continue at a local state or transfer to a
named exit. 

### `Fragment.State`

 Finite set of instruction states internal to this fragment. 

### `Fragment.entry`

 Initial local instruction state on entry to the fragment. 

### `Fragment.code`

 Instruction at each local state, with successors selected from local states and named
  exits. 

### `isolated`

 Standalone fragment table that executes the local code and treats every named exit as an
accepting halt. 

### `Runs`

 An execution from fragment entry to the specified named exit in exactly the stated number
of steps and with the stated final stacks. 

### `direct`

 Form a one-instruction fragment whose continuations are all named exits. 

### `returning`

 Turn a finite routine into a fragment that transfers a normal return to the specified exit
label. 

### `returning_runs`

 The continuation after an ordinary subroutine can be any flow label. 

### `fromCode`

 Install a multi-exit program. A designated boundary row is intercepted
on entry, allowing the caller to decide what follows each returned action. 

### `onPorts`

 Place a fragment's ports inside a larger bank, leaving the remaining
stacks available to the caller. 

### `State`

 Instruction address in the linked processor, pairing a block label with a local state of
that block. 

### `enter`

 Select a named block and its entry state as the linked instruction address. 

### `next`

 Resolve a successor by continuing inside the current block or entering the destination
named by an exit. 

### `program`

 Link the fragment tables into one stack program by resolving each local successor and each
named transfer. 

### `run`

 A whole deterministic path in a fragment runs unchanged in the linked
program, arriving directly at the entry of its exit label. 
