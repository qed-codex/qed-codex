---
{
  "module": "OAI/Computability/VPVNP/RAMTapeChargesControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeChargesControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeChargesControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite control for metering RAM calls and probes

One dispatch removes one unary fuel mark. Starting a call and taking a probe
use the same charge entry: remove a call mark and a site mark, subtract one
from the binary global allowance, and increment the binary cumulative cost.
No branch of the control iterates to the numerical value of a binary word.


### `Port`

 Stack labels for dispatch fuel, call and site credits, binary global and cumulative
counters, and arithmetic scratch. 

### `State`

 Metering control for dispatch, unary credit removal, binary carry or borrow, and counter
restoration. 

### `resume`

 Reject overflow after restoration, finish after incrementing cost, or begin incrementing
cost after decrementing the global budget. 

### `code`

 Meter a dispatch by one fuel mark, or charge a call or probe against the call, site,
global, and cumulative counters. 

### `Data`

 Contents of the unary allowances, binary charge counters, and scratch stack used by the
metering control. 

### `Data.fuel`

 Unary instruction fuel, with one mark removed for each dispatch. 

### `Data.call`

 Remaining unary charge marks for the current call. 

### `Data.site`

 Remaining unary charge marks for the site. 

### `Data.globalLeft`

 Binary global allowance decremented by one per charge. 

### `Data.cost`

 Binary cumulative cost incremented by one per charge. 

### `Data.tmp`

 Reversed output bits saved while updating a binary counter. 

### `Data.stacks`

 Read a metering stack from its named counter or scratch field. 

### `Data.set`

 Update a single metering stack in the charge bank. 

### `tick`

 A continuing deterministic transition. Halting states have no successor. 

### `Run`

 An execution of the charge controller between two states and banks in exactly the given
number of stack steps. 

### `scanData`

 Choose the active binary counter without disturbing the other counter. 

### `adjustRun`

 Exact runtime of the binary update, with overflow and underflow flags
preserved all the way to the terminating control decision. 
