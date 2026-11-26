---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkMapCompiledSource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapCompiledSource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapCompiledSource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The actual compiled shrinking map source at a selected vertex

The compiled payload records the native term run of its producing occurrence
and retains the grid ordinal of each of its selected motifs. The resident map
and term heads in that same payload are the words read by the shrinking map
segment. The final vertex frame preserves these operands at every ordinal.


### `mapRowSource_compiled`

 Extract the map arrays, term records and descriptor from one compiled
shrinking payload. The certificate for the term words is the actual run stored
by the producer, with its original input memory and chronological reports. 

### `mapRowSource_vertex`

 Read the actual row certificate at an arbitrary later final-site call of
the packed terminal program, identifying the producing pass by its selected
occurrence in the executed history. 
