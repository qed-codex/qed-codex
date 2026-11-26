---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackNativeCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackNativeCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackNativeCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running a virtual stack call inside the native pair simulation

The private RAM rows consume exactly the source branch prefix, ending with
the same stack bank. The caller may use every bit left over. Closing the call
with an accepting continuation recovers exactly the bounded stack path count,
including coincident successors of a choice.


### `NativeCall`

 The exact native prefix of an accepted call and the interpreter's
behavior on every other stream. Each continuing stack row costs four
native instructions and a true halt costs one. Thus three instructions
from the final row are available to its continuation. 

### `reachable_capacity`

 A bounded source run needs at most one additional cell per source
instruction on each stack. This gives an interval size when a separate
space estimate is unavailable. 

### `parse_native`

 Every branch of the private RAM stack fragment agrees with the source
interpreter. At the exact native cutoff no source termination premise is
needed. A source stopping bound also permits arbitrary extra native fuel. 

### `execute_continuation`

 For a true source halt, the caller resumes from the actual native
configuration, with arbitrary continuation fuel and the entire unused suffix. 

### `execute_accept_iff`

 Closing with the native accept instruction consumes exactly one of
the complete successful source words. This holds even with coincident
choice successors and early halts. 

### `nativeStreams_card`

 The native private RAM call has the same multiplicity as the capped
stack machine. All initial banks obeying the representation and every
external memory give the same equality. 
