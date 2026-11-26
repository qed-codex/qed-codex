---
{
  "module": "OAI/Computability/VPVNP/RAMLocalRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLocalRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLocalRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary paths of the private call interpreter

A site processor in Lemma 10.1 follows the program's binary branches and reads
exactly one word of guesses at a permitted external read. A write has no guessed
value. The processor checks its instruction clock before dispatch, and checks
its remaining probe budget before consuming read bits or recording a write.
A successful call returns its unused bit suffix for the next call.


### `guessBits`

 Bits used by the site validator, including the guesses made at reads. 

### `Event.probeCharge`

 Charge one probe for each external read or write and zero for a private tick or branch. 

### `Event.guessWidth`

 Number of guess bits reserved by the site validator for this event. A branch uses one bit
and a read uses one full word. 

### `LocalCallRun`

 Metered execution on a binary stream. `guessWork` counts reserved bit slots,
including the requested slots when the stream ends during a guess. 

### `LocalCallRun.output`

 The successful call report and unused guess suffix, or `none` when the local execution
  fails. 

### `LocalCallRun.instructions`

 Number of instructions charged by the local interpreter, including the terminating
  instruction when one executes. 

### `LocalCallRun.probes`

 Number of probe slots charged, including an allowed read that fails for lack of enough
  guess bits. 

### `LocalCallRun.guessWork`

 Number of guess-bit slots requested by branches and reads, including requests whose input
  stream is too short. 

### `LocalCallRun.stop`

 One terminating instruction. 

### `LocalCallRun.prepend`

 One executed instruction followed by the remainder of this call. 

### `runLocalCall`

 Interpret a call privately. The caller supplies the remaining allowance for
probes after charging the unit for starting the call. 

### `runLocalCall_iff`

 A successful report determines the consumed binary string exactly. This
also distinguishes branches with the same continuation or result. 

### `existsUnique_callBits`

 With exact use of the bits, every permitted trace has one accepting
binary path through the local call simulator. 

### `runChargedCall`

 The three remaining allowances count the startup charge as well as the
probes. A zero allowance rejects before the program sees its first instruction. 
