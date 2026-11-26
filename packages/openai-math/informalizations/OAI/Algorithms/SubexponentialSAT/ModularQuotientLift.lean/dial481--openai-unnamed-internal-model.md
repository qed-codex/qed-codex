---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ModularQuotientLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularQuotientLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularQuotientLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary quotient and remainder on caller-selected stack ports

The fixed quotient program is relocated to eight distinct caller ports.  Its
existing instruction-trace bound is retained exactly.  Endpoints are explicit
updates of the caller's own stack store, so every unassigned stack is framed.


### `quotientStacksAt`

 Only the remainder, consumed input, and quotient ports change. 

### `programAt`

 Relocation changes only the fixed port names, not the instruction table size. 

### `programAt_runsIn`

 The actual quotient routine runs within its proved bound on arbitrary
caller storage.  Ports `1` through `4` are initially empty work stacks. 

### `programAt_eval`

 A direct structured-call interface, retaining the genuine trace length
rather than padding it to the upper bound. 

### `programAt_primitive`

 The verified binary-machine compiler preserves this arbitrary-frame run. 
