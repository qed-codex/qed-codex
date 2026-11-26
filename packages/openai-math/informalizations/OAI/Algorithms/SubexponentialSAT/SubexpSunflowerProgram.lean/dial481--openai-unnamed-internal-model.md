---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSunflowerProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSunflowerProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSunflowerProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual finite programs used by sunflower candidate checking

Runtime clause counts and widths remain encoded stack data. The first
primitive counts framed records; it is an actual finite instruction table,
with a trace theorem, rather than a semantic list-length instruction.


### `program`

 Count records into a canonical unary field. Payload bits are skipped by
following their escape tags. The same thirteen labels handle every count. 

### `complete_trace`

 Canonical-input/canonical-output execution, with no residual work data. 

### `primitive_execution`

 The existing compiler transfers this actual finite program to primitive tape steps. 

### `probe`

 Membership with a preserved query and fully cleared work ports. 

### `probeProgram`

 A concrete fixed-table subroutine, ready to be relocated into a caller. 

### `probe_preserving`

 The probe changes no stack at all when called with clean workspace. 

### `Clean`

 Workspace is independent of the two preserved target clauses. 

### `probeCall_eval`

 The same fixed probe code is relocated to either target clause, with an
extra untouched register available for the first Boolean answer. 

### `callback`

 A real callback for the violation q∈D and q∉H. Both target encodings are
preserved; the reversed query payload is consumed after both probes finish. 

### `targets`

 The source iterator needs only these two persistent target encodings. 

### `ContainsIntersection`

 Semantic property checked by the concrete two-membership scan. 

### `command`

 Test `C ∩ D ⊆ H`. All three encoded clauses live on stacks, independent
of the fixed finite instruction table. C is consumed; D and H are preserved. 

### `program`

 Fixed syntax compiles to one finite machine, not a family indexed by the
number or size of the runtime clauses. 

### `rawInput`

 A fixed input schema for the relational checker: two framed target clauses,
then the source clause. All clause and literal counts remain runtime data. 
