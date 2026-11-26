---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalDeterministic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalDeterministic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalDeterministic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering deterministic terminal stages on arbitrary accepting tapes

For a known ordinary worker segment with only empty choice strings, transport
its reads into the actual memory before comparing each physical call. This
proves the actual segment has the same report, choices and final worker memory
even when its caller supplies an arbitrary candidate tape.


### `Phase.force_empty`

 The witness needs a read bound only for the supplied deterministic
reference reports. The arbitrary candidate is taken directly from the
complete native path, with no hypothesis on its read addresses. 

### `Phase.force_quiet`

 Every completed phase from the same physical entry agrees with a
completed phase that consumed only empty choice strings. 
