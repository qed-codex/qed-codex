---
{
  "module": "OAI/Computability/VPVNP/RAMWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word work of the finite instruction interpreter

The instruction charges follow the actual local run, including a failed call.
The bound is uniform in the incoming persistent state, probe allowances, and
bits. All arithmetic in the private machine is on words and all operands have
constant arity.


### `continueCall`

 Which invocation follows the current dispatch. A rejected probe, a short
choice stream, or a terminating instruction has no successor invocation. 

### `Instr.logCharge`

 A private load scans at most the number of write-log slots reserved
for this call. A store prepends its address and value. 

### `Machine.dispatchWork`

 Sum the elementary opcode charges actually incurred by the local call.
The final dispatched instruction counts even when it causes rejection. 

### `Machine.loggedDispatchWork`

 Opcode work in the implementation with a concrete write log. 

### `Machine.loggedDispatchWork_le`

 The reserved linear scans bound the actual linear scans on *every* choice
stream. The invariant pays for at most one new private write per dispatch. 

### `Machine.loggedDispatchWork_start`

 Each call starts with an empty log; its instruction fuel is enough log
capacity even on rejecting paths. 

### `Machine.callWordWork`

 Besides opcode work, reserve eight control operations per dispatch,
five word stores per occupied probe record, and four operations per bit
guessed, fetched and packed into a word. 

### `Machine.meteredLoggedCall_work_le`

 On a fresh call the actual one-pass work is bounded by the reserved
work, including truncated streams and attempted over-cap probes. 

### `Machine.siteWordWork`

 Count the elementary work of the same invocation that returns the site's
reports and unused bits. 

### `Machine.privateSite`

 The metered result of the concrete word interpreter and its private
memory log. The successful reports and unused bits are the ordinary site's
output, including on malformed incoming data. 

### `Machine.privateSite_work_le`

 The site portion of the paper's clock bound when the bucket size is at
most twice the instruction fuel. For fuel `n^u`, `u ≥ 1`, this follows from
`H ≤ 2n`. The constant leaves room for the remaining validation checks. 
