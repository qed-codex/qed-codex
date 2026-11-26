---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composing the native stages of a shrinking vertex

The old-half-wire reader passes its exact stream suffix and private memory
to the hidden-field reader. The deterministic resident maps start with the
resulting private fields. The same entry scratch determines the path and
the entire returned scratch for every compatible native configuration.


### `Outcome`

 The data, native trace, and full scratch result of one local stage. 

### `Outcome.value`

 Typed value produced by this visit stage, such as its decoded child arguments or chosen
  hidden fields. 

### `Outcome.trace`

 Chronological native events emitted while producing the stage's value. 

### `Outcome.updated`

 Private scratch image retained by the next stage after this reader finishes. 

### `Reader`

 A partial visit-stage decoder for a node and scratch image. Success returns the typed
outcome and the unconsumed suffix of the choice tape. 

### `Frame`

 The four DFS registers and every private stack address protected across
the stage, together with its persistent word. 

### `Realizes`

 Each accepted result runs from every native input satisfying the entry
predicate, and a failed read precludes returning for every fuel. 

### `bind`

 Pass the first stage's parsed values, scratch, and suffix to the next. 

### `Splits`

 Successful parses split the supplied tape at the native choice events. 

### `Realizes.weakenPost`

 A later consumer may discard unused facts established at the exit. 

### `Realizes.bind`

 A rejection in a later stage follows back through the successful prefixes
of the earlier stages. This covers truncation within any consumed field. 

### `Setup`

 A deterministic register-setup stage described on the caller's scratch. 

### `Setup.trace`

 Events of the deterministic setup at the given popped node and incoming scratch image. 

### `Setup.updated`

 Scratch image left by the deterministic setup for the subsequent visit stage. 

### `Setup.reader`

 Expose deterministic setup as a unit-valued reader that emits its trace, updates scratch,
and retains the entire choice tape. 

### `Setup.ticks`

 A register-only setup has a fixed number of local ticks and keeps all scratch. 

### `Setup.seq`

 Consecutive setup fragments expose one trace and the last scratch update. 

### `Setup.realizes`

 A linked setup may read the real directory or write the private operands.
Its specified trace and writes must hold on every eligible input configuration. 

### `hook`

 Convert the composed local reader into one DFS visit with its full
scratch snapshot as the input condition. 

### `Entry`

 Native state at a DFS visit after the node was popped. 

### `Realizes.exactOn`

 Any compatible entry configuration produces the same parsed trace and
scratch result. The bit identity must also hold for a successful read whose
input scratch currently has no compatible DFS stack. 
