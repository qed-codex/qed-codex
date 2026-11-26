---
{
  "module": "OAI/Computability/VPVNP/StructuredStacks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStacks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStacks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Structured finite-control programs for bit stacks

The local validator in §10 performs nested scans, branches and calls. Each routine
has one normal return and may also halt with acceptance or rejection. Linking a
return to the next instruction introduces no extra machine step. All constructions
on finite controls use only finite sums and individual new labels.

The continuation semantics counts accepting paths with a fixed remaining step budget.
It permits exact accounting through a call even when the callee makes binary choices.


### `Routine`

 A control label is local to this routine. `none` in an instruction's continuation
returns to the caller, while a halt ends the entire execution. 

### `Routine.entry`

 The local control label at which an invocation of the routine begins. 

### `Routine.code`

 The stack instruction at each local control label, using an absent successor to return to
  the caller. 

### `close`

 Closed executable with an arbitrary halt outcome at the normal-return boundary. 

### `standalone`

 Closes a routine as a stack program by installing a rejecting halt at its normal-return
boundary. 

### `Runs`

 A deterministic execution from the routine entry to normal return in exactly the indicated
number of instructions, with the specified initial and final stack banks. 

### `install`

 Install a routine's control into its caller, redirecting normal returns. 

### `ret`

 Returns normally in one instruction, preserving the stack bank. 

### `push`

 Pushes one bit onto the specified stack and returns normally. 

### `halt`

 Halts the whole execution with the specified acceptance bit. 

### `followedBy`

 Run both routines, returning normally only when the second does. 

### `choose`

 Two branch slots count separately, even for routines with identical effects. 

### `popCase`

 Pop one bit, dispatching separately on an empty stack, zero, and one. 

### `popLoop`

 An empty stack ends the loop. On a present bit, first run the selected body.
When it returns, `repeatOn` decides whether to continue or to finish the scan. 

### `countFrom`

 At a normal return the continuation receives the exact remaining fuel and stacks. 

### `count`

 Counts accepting branches from the routine entry within the fuel budget, using the
continuation’s count at each normal return. 

### `stackPaths_close`

 A fixed closed machine realizes the continuation semantics for either return outcome. 

### `countFrom_install`

 An installed control counts precisely the same paths as its original routine,
then resumes with the residual budget. 

### `count_followedBy`

 Sequencing spends no instruction on transferring control from one routine to the next. 

### `count_choose`

 A binary nondeterministic instruction contributes both of its branch counts. 

### `count_popCase`

 A case instruction consumes exactly one machine step and removes the head when present. 

### `count_popLoop`

 One test of the loop selects the body and links its normal return either to the next test
or to the caller. The body may make any number of binary choices before returning. 
