---
{
  "module": "OAI/Computability/VPVNP/PairSimulationAssemblyBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAssemblyBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAssemblyBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Per-vertex bit bounds on the actual repeated compressor

The field records of Theorem 7.1 cover each choice read below a selected
vertex. Joining two procedures and repeating a block preserve this
coverage at every selected term. This bounds the private binary string
at each final site, including independent old half-arc guesses.


### `PassReaders.termParsers`

 Use the same order, arc payloads and kernel choices as the complete
history reader. 

### `ExecutionCovered`

 Every term of every reachable pass has enough recorded field width at each output site to
cover the bits for its children's old halves and its local kernel choice. 

### `branchParsers`

 Follow the actual term choices into the local subtree parsers of this
branch of the existing compression history. 

### `ProcedureCovered`

 Coverage of a procedure on every legal input state and lane count. Each branch of the
resulting execution is checked against the records supplied by the procedure's record
bounds. 

### `selectedParsers`

 On a complete choice of terms, use the concrete readers and records
of the compressor to expand one final vertex. 

### `selectedSite_length_le`

 The per-site private string uses at most the per-block growth factor
times the larger of the leaf-string bound and the intermediate field bound. 

### `cursorSite_length_le`

 The bound on private bits at every final vertex, specialized to the
original capped machine's validating leaf bursts. 
