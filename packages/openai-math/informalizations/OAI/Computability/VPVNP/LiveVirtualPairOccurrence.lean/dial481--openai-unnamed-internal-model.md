---
{
  "module": "OAI/Computability/VPVNP/LiveVirtualPairOccurrence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairOccurrence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairOccurrence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # From source tapes and histogram visits to the fixed program's compressed call

A native schedule emits concrete per-call tapes from its selector, arc and final-site
phases. The accepting-tape equivalence below uses the identity on those tapes.
The only counter condition on the simulator concerns its actual writes. Their
mathematical values follow from readback of the canonical virtual occurrence.


### `SourceRuns`

 Source-level obligations for one schedule on the actual prepared memory.
The returned reports are the unrelocated reports of the pair instruction table. 

### `SourceRuns.encoding`

 Trace encoding that identifies the source schedule's semantic occurrences with their
  selector, arc and vertex phases. 

### `SourceRuns.emission`

 Injective translation from those encoded phases to native motif-ordinal term bursts and
  the corresponding arc and vertex bursts. 

### `SourceRuns.tapes`

 Per-call private tapes for each emitted ordinal phase list. Their range is exactly the
  tapes on which the native pair program runs from the prepared memory to a halt. 

### `SourceRuns.paths`

 The equivalence to raw accepted paths preserves the actual list of tapes. 

### `SourceRuns.execution`

 Assemble the relocation contract using only the source classification, its
execution facts, and counter readback of the selected mathematical occurrence. 

### `CompressedInput`

 The physical inputs at one nominated first-half group. 

### `CompressedInput.cuts`

 Assignment of all physical cuts for the chain containing the selected first-half pair
  group. 

### `CompressedInput.i`

 Zero-based index of the nominated pair group within the first half of the physical chain. 

### `CompressedInput.trace`

 Prepared header-stage execution for this first-half group on its actual cuts and advice,
  furnishing the memory from which nominations are read. 

### `CompressedInput.μ`

 Production-count nomination selected for this pair by the physical nomination stage. 

### `CompressedInput.branch`

 Initialization and sparse-copy runs for the selected nomination, preparing the auxiliary
  pair memory with the header from the actual exterior cuts. 

### `CompressedInput.exterior`

 Recover the primed exterior cut strings from the outgoing exterior fields of the first-half
physical cuts, starting with the width-zero initial cut. 

### `CompressedInput.nominationFits`

 Certify the nomination stage's address, word-width and clock requirements for the selected
group using the pair-stage conditions at its index. 

### `modelExterior`

 Transport a physical exterior cut assignment to the model using the equalities of chain
heights and cut widths. 

### `compressedObligation_of_inputExecution`

 Transport all model dimensions simultaneously, preserving the native index,
input memory and selected physical nomination. 

### `VirtualPairs.PhysicalInput`

 One checked physical branch for the fixed program's model. 

### `VirtualPairs.modelIndex`

 Express the selected physical first-half index in the fixed model's index type using the
equality of chain heights. 

### `VirtualPairs.exterior`

 First-half exterior cut data of the selected physical input, transported to the fixed
program's model dimensions. 

### `VirtualPairs.input_shadow`

 The compressed call reads the canonical virtual pair's own reset memory at
each address in this actual physical input's shadow. 

### `VirtualPairs.nativeRuns`

 Native schedule facts on this particular canonical monomial witness.
The expected motif flushes start with the actual memory of the copy stage. 

### `VirtualPairs.nativeExecution`

 Actual source tapes, their costs and their histogram writes give the canonical
occurrences and increments expected by the compressed stage's linker. 

### `VirtualPairs.compressedCalls_of_nativeRuns`

 Source executions at all valid prepared groups supply the complete first-half
compressed-call obligation, with the model's exact occurrence type and field exponents. 
