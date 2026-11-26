---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapNativeClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapNativeClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapNativeClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Instruction budgets for a complete fixed-template map call

The bounds include the port comparison, selector decoder, repeated label
lookups, the full-vector width comparison and the local histogram update.
The table constant is chosen before the dynamic widths and all input bits.


### `cap`

 The instruction bounds of the five linked phases at a selected grid row.
Two incident ports per supply edge suffice even when both ends are at this party. 

### `uniform`

 Fixing the tables gives a linear instruction cap, including the final
width comparisons on a descriptor whose totals differ. 

### `MapInvocation.nativeCap`

 The exact two motif tables of the selected compressor. Direct equality
checks emit no parameters and use their separate field comparison routines. 

### `mapInvocation_nativeCap`

 A single table constant covers both actual passes and all malformed bits. 
