---
{
  "module": "OAI/Computability/VPVNP/RAMExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounded executions of burst RAM calls

The genuine interpreter follows a supplied sequence of binary choices and
answers external reads from memory. A processor in Lemma 10.1 instead guesses
each answer. The two executions agree exactly when all reads in its local
transcript have their prescribed values. Binary choices are retained even when
their two continuations coincide.


### `Word`

 A width-`w` RAM word, represented by a natural number strictly below `2^w`. 

### `Memory`

 External RAM storing a width-`w` word at each natural-number address. 

### `CallAction`

 A small step in a call. `finish none` accepts and `finish (some s)`
returns the persistent state for the next call. 

### `Program`

 A burst-RAM call program with a private configuration type, an initializer from the
persistent word and a one-step instruction function. 

### `Program.start`

 Private state is recreated from the persistent word on every call. 

### `Program.step`

 Select the next call action from the current private configuration. 

### `Event`

 A recorded private tick, binary branch choice, external read or external write. Both kinds
of probe carry the address and word value. 

### `Report`

 A single call's ordered event trace and its optional persistent word for the next call. 

### `Report.events`

 Chronological sequence of private ticks, branch choices and external probes during the
  call. 

### `Report.result`

 Persistent word returned to start another call, or `none` when the machine accepts and
  stops. 

### `Report.prepend`

 Add an earlier event to the front of a call report. 

### `writeMemory`

 Set the addressed external word to the supplied value and preserve all other addresses. 

### `update`

 Apply one event to external memory, storing the supplied value on a write and preserving
memory for every other event. 

### `after`

 External memory after applying the writes in a chronological list of events. 

### `Correct`

 Every reported read equals the external word at its address after all preceding writes in
the trace. 

### `choiceBits`

 Extract the binary branch outcomes in order from a call's event trace. 

### `execute`

 Native execution. Unused choice bits, a rejecting halt, and exhausted
instruction fuel all reject. The exact-use convention gives a unique encoding
of each branch path. 

### `Guessed`

 Local call execution. Each external read guesses an arbitrary word. 

### `execute_iff`

 Correct read guesses leave one transcript per path of binary choices. 
