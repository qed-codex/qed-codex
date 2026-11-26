---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSelectorRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Inverting the term selector of a valid physical online row

Each successful burst advances the term worker by one ordinal, including
bursts recovered from an arbitrary accepting path. The directory guard
therefore forces the exact motif count. The admitted term and its entire
list of burst choices are then recovered from the actual source execution.


### `ProgramTable`

 Bundle the control type with its physical machine table, so equality
of installed tables can be used even when the catalog indexes differ. 

### `WorkerInput.table`

 The term-worker program paired with its control type, instantiated from the pass grid, the
demand and supply orders, and the input's four address words. 

### `sourceTable`

 The program and control type installed for a directory row, obtained by instantiating its
catalog worker with the public words read from that row's input. 

### `WorkerInput.installed_of_words`

 Identify the installed source using just the selected catalog row
and its public operand words. 

### `WorkerInput.validRow_unique`

 An arbitrary valid selector row, with the term table installed on its
input addresses. The recipe's start, exclusive bound, and actual data
memory are the only inputs besides the machine and fuel identities. 

### `WorkerInput.validRow_fields`

 The accepted term also describes the data in the actual post-worker
memory. No new guess is made to choose the continuation state. 

### `WorkerInput.validStep_rowChoices`

 The three entering control calls and the closing call do not change
the multiplicity of the term selected by the recovered row. 

### `WorkerInput.decode_validStep`

 The reference input used by the semantic decoder can have its own
memory and private clock. For the recovered row, use the demand cells in
the actual post-launch RAM and the fuel installed by the calendar. The
canonical full-width tapes depend only on the pass and selected term. 
