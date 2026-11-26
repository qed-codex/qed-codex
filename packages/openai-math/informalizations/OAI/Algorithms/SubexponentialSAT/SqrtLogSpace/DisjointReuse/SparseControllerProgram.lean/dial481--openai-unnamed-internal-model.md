---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseControllerProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseControllerProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseControllerProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete control composition for fixed finite bit commands. 

### `while_execution`

 A real finite while command composes actual local body executions. The
premises must be supplied by the concrete search, child, and leaf routines. 

### `while_execution_space`

 A fixed while table retains one uniform all-prefix stack bound across
every visit. Each premise is a measured execution of the concrete body. 

### `firstHit`

 The list is part of finite control, chosen with `k`, not an input table. 

### `Visits`

 Only actually executed phases occur as `next` constructors. A `stop`
retains the unvisited command suffix and performs no callback invocation. 

### `FailedStages`

 If the final flag is false, each phase was actually run, and each phase
output was false. This exposes all unsuccessful searches to completeness proofs. 

### `firstHit_execution`

 Fixed-code phases compose with their measured local budgets. This is an
intermediate theorem: the actual phase programs must discharge `hphase`. 

### `Visits.first_success`

 A successful search exposes its first successful concrete phase, all actual
failed earlier phases, and the untouched command suffix. 
