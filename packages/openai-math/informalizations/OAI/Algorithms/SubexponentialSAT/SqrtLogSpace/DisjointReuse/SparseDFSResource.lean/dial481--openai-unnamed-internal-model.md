---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSResource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSResource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseDFSResource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Resource bounds for the actual outer DFS commands.

Cleanup is structurally nonallocating. The bounds below concern the concrete
finite tables and every source prefix, before applying the guarded primitive
compiler. The selector and leaf contracts still require their own executions.


### `clearPorts_space`

 Sequential clearing keeps the same bound, including during every pop
and return jump. The finite list length never multiplies the space bound. 

### `finishVisit_execution_space`

 A complete visit cleanup clears the current formula and all 256 DFS
workspace stacks, preserves the other high words, and restores the loop flag
by reading the real frontier. Every intermediate stack remains bounded. 

### `branch_execution_space`

 The concrete disjoint splitter and child insertion share one uniform
bound. Both child records, the pending list and every caller stack are counted;
no number of previously visited branches occurs in this bound. 

### `startFrontier_execution_space`

 Frontier initialization moves the actual current formula into its escaped
record and retains the saved declared-variable word and every caller stack. 

### `popCurrent_execution_space`

 A real nonempty frontier pop decodes only its head record. All 1220 root
stacks are included, and no earlier traversal time appears in the bound. 

### `accumulate_execution_space`

 The root accumulator uses the same concrete addition/normalization trace.
The disjoint-mass premise bounds both canonical input words; the final count
is on physical port260 and both count scratch ports are empty. 

### `finishVisit_boundary_space`

 Cleanup restores the smaller loop-boundary bound even when the completed
callback used a larger transient workspace. Consequently that workspace bound
is not accumulated from one DFS visit to the next. 

### `selectCurrent_execution_space`

 The real selector runs in the frozen root bank. Its semantic hit/miss
results and all-prefix storage bound come from the same local execution;
the final return instruction is included before relocation into the root. 

### `branch_preserves_other_high`

 Every real branch execution preserves high words outside its fixed port
footprint. The header258 is handled separately by the splitter's exact header
readback; this structural rule covers raw input, leaf count, setup words and
all reserved high stacks for the very same branch witness. 
