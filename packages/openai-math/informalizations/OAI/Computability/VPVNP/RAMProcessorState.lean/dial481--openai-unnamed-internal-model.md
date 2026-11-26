---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical bank at call-segment boundaries

This representation names every stack used by the opcode, credit, probe, test,
and record routines. Shared fields occupy a single stack. The same incoming
choices, cost, persistent word, and probe ordinal are therefore visible at each
stage without copying or consulting a global message assignment.


### `probePorts`

 Place each probe-stage port in the shared site-processor bank, reusing the ISA, choice,
record-field, and running-status stacks and assigning two scratch stacks for copies. 

### `Snapshot`

 The record buffer is already in reverse serialization order. Its
remaining stack contains one mark for each unoccupied slot. 

### `Snapshot.pub`

 Public operand words read by the instruction table during a call. 

### `Snapshot.cfg`

 Current program counter, persistent word, registers, and private-memory write log of the
  simulated RAM. 

### `Snapshot.publicH`

 Public call-cost allowance copied into the call counter when a fresh call begins. 

### `Snapshot.publicFuel`

 Public instruction allowance used to reset the fuel of each new call. 

### `Snapshot.fuel`

 Instructions still available to the currently simulated call. 

### `Snapshot.callLeft`

 Remaining units of call cost available under the current call’s allowance. 

### `Snapshot.siteLeft`

 Remaining call-cost units in this site’s budget for its local loop. 

### `Snapshot.cap`

 Word encoding the upper bound on cumulative call cost for the entire computation. 

### `Snapshot.globalLeft`

 Word holding the remaining global cost credit after charges already incurred. 

### `Snapshot.cost`

 Cumulative cost charged so far, counting one unit per call and one per external probe. 

### `Snapshot.savedStart`

 Bits of the start-cost field staged for the next record. For a probe this is the
  cumulative cost before its call. 

### `Snapshot.ordinal`

 Bits encoding the next probe’s zero-based ordinal within the current call. 

### `Snapshot.lower`

 Lower endpoint of the current site’s cost bucket, used to check the incoming running cut. 

### `Snapshot.boundary`

 Upper endpoint of the site’s cost bucket. A running computation continues here while its
  cost is below this word. 

### `Snapshot.targetCost`

 Cumulative cost advertised by the outgoing successor message for the end-of-site check. 

### `Snapshot.targetState`

 Persistent word advertised by the outgoing cut when the target is running. 

### `Snapshot.running`

 Whether the computation at the current cut has a running persistent state. 

### `Snapshot.hasTarget`

 Whether this site has an outgoing successor cut to check at its boundary. 

### `Snapshot.targetRunning`

 Running-status bit of the advertised outgoing cut. 

### `Snapshot.choices`

 Unconsumed private choice bits for RAM branches and guessed external-read answers. 

### `Snapshot.tag`

 Serialized kind word staged for the current initialization, read, or write record. 

### `Snapshot.address`

 Address bits staged for the record that the processor is about to emit. 

### `Snapshot.value`

 Value bits staged for the initialization, read, or write at the recorded address. 

### `Snapshot.remaining`

 One stack marker for each vacant slot in the site’s fixed-capacity record buffer. 

### `Snapshot.reverseBuffer`

 Accumulated serialized record bits in reverse order, ready to be reversed into the output
  block. 

### `Snapshot.output`

 Stack receiving the padded record block in forward serialization order. 

### `Snapshot.credit`

 Expose the public limits, remaining credits, cumulative cost, saved start cost, and probe
ordinal on the credit routine’s ports. 

### `Snapshot.tests`

 Project the bucket endpoints, current cut, outgoing target, status flags, and remaining
choices onto the site-test bank. 

### `Snapshot.probe`

 Assemble the ISA bank, choice bits, staged record fields, and running flag used by the
probe handlers. 

### `Snapshot.records`

 Arrange the five staged record fields, zero padding, vacant-slot markers, and serialization
buffers on the record routine’s ports. 

### `Snapshot.bank`

 Unused copies of aliased port labels stay blank. 

### `Snapshot.afterLocal`

 Install the configuration, remaining fuel, and unused choice bits yielded by a local
instruction segment. 

### `Snapshot.installLocal`

 A local segment changes only its ISA bank, remaining fuel, and choices. 
