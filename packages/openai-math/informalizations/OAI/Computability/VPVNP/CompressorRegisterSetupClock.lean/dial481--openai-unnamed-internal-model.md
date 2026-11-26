---
{
  "module": "OAI/Computability/VPVNP/CompressorRegisterSetupClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRegisterSetupClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRegisterSetupClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The event log of register setup

Every external address used by the expression compiler is computed from
the public operands, the state word and the current memory. The scratch
registers can therefore start with arbitrary words. Even nested loads and
repeated loads of the same address have the same complete event log.


### `events_eq`

 Evaluating all setup lines produces the same events as a zeroed
compiler bank, including the address and return value of every read. 
