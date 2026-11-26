---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTraceJobs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTraceJobs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTraceJobs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering the selected vertex jobs from an emitted trace

The selector words, the native shared-arc call list, and all vertex strings
in a complete trace come from one branch and one edge assignment. Each
vertex string therefore has the preorder job decomposition for that same
branch, and their exponent increments add to the decoded monomial.


### `TerminalData`

 The native shared scan supplies the incident values of every vertex
before the independent site witnesses are chosen. 

### `TerminalData.arcs`

 Path of the shared-arc scan that fixes the wire payload incident at every terminal site. 

### `TerminalData.choices`

 For each terminal site, a local monomial witness choice evaluated on the half-wire
  assignment from the shared-arc path. 

### `TerminalData.phases`

 Build the three choice-stream lists from the supplied selector tapes, the shared-arc path's
calls, and each terminal site's encoded witness in site order. 

### `TerminalData.exponents`

 Total exponent of a parameter label in the terminal monomial, obtained by summing its local
witness exponent over all sites of the shared arc assignment. 

### `terminalSites`

 Site parsers on the final network of the selected execution branch, formed by pushing the
initial parsers through the chosen terms in order. 

### `executionTrace_jobs`

 A single branch, one native shared scan, and actual terminal witnesses
recover all three observable phases and every parameter exponent at once. 

### `TerminalData.jobs`

 The individual preorder jobs belonging to the witness at one of the
terminal sites, with both incident halves drawn from the same native scan. 

### `compressedTrace_jobs`

 Every phase triple in the counted RAM family has one selected branch
and shared native arc path whose concrete site jobs produce its vertex
bit strings and whose local increments produce its decoded exponents. 
