---
{
  "module": "OAI/Computability/VPVNP/UniversalCountStack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountStack.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountStack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic enumeration of fixed-length Boolean witnesses

Section 8.1 queries an integer coefficient by counting all canonical witnesses.
Two little-endian counters hold the current witness and the number accepted.
The control invokes a verifier, adds its one-bit result to the count, and
increments the witness. Overflow of the witness counter ends the enumeration,
including the case of a zero-bit witness.


### `Port`

 The witness and total counters, temporary digit stack, verifier result flag, and auxiliary
ports used by the witness enumerator. 

### `Register`

 Selects the binary counter holding the current witness or the number of witnesses accepted
so far. 

### `Register.port`

 The stack port storing the selected witness or total counter. 

### `Control`

 The local states for invoking the verifier, collecting its result, and propagating a carry
through either counter before restoring its digit order. 

### `enumerate`

 The finite control and ports are independent of the width of either counter. 

### `bank`

 Call boundary for the verifier. Its private work and its persistent input
are all located at `aux` ports. A normal return places one Boolean in `flag`. 

### `iteration_run`

 The next call starts with the incremented counters. On the last witness
the normal return has exactly the same layout, with the witness reset to zero. 
