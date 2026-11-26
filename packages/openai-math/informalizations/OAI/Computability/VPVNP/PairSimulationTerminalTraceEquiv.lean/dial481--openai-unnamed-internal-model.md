---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalTraceEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalTraceEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalTraceEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniqueness of the five terminal phases

The accepting exit of each worker uniquely determines its block of physical
calls. Concatenating the five blocks therefore gives a bijection with the
native accepted paths, for any predicate on the full sequence of reports.


### `Phase.unique_prefix`

 Two complete runs of the same worker on prefixes of a common call stream
consume the same prefix and leave the same reports, memory and suffix. 

### `Phase.block_eq_suffix`

 The terminal cut determines the full block and its remaining choice stream. 

### `FiveTrace.choices_injective`

 The entire five-phase trace, including the reports and each intermediate
memory, is uniquely determined by the sequence of native branch strings. 

### `fiveTraceEquiv`

 Concatenate the choices of the five admissible phases to obtain the
corresponding accepting path of the linked native program. 
