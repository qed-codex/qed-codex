---
{
  "module": "OAI/Computability/VPVNP/RAMTapeCharges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCharges.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCharges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Precharging startup, probes and instruction dispatch

The local verifier pays for a dispatch before reading a program row, and
pays for each call startup or probe before using any read guesses or writing
a probe record. Failed checks enter the rejecting halt. The normal charge
decrements both unary allowances and the binary global allowance and
increments the binary cumulative cost.


### `bank`

 The instruction, call and site caps have one mark per remaining unit.
The global allowance and cumulative cost each occupy exactly one word. 

### `chargeRun`

 The successful path takes exactly two unary pops and two linear binary
updates. Startup and probes have the same one-unit effect on these caps. 

### `failureTicks`

 The first failed allowance determines where execution stops. A final
overflow after both unary pops and the global decrement takes the full cost. 

### `chargeReject`

 Every exhausted budget and every cost overflow reaches the actual
rejecting row, with the exact stopping cost of the precharge. 

### `routine`

 Redirect the successful halt to a normal return while keeping the
rejecting halt and all stack updates on the named ports. 

### `liftRun`

 Lifting also covers an execution ending at the rejecting control state.
Every port outside the image of `ports` keeps its initial stack. 
