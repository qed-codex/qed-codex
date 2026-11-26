---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ScheduleProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ScheduleProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ScheduleProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual binary construction of the disjoint-sparsification parameter.
All arithmetic uses fixed finite programs; the input numeral is runtime stack data. 

### `clogAt_eval`

 The two work stacks are restored, and all other caller stacks are framed. 

### `command`

 Ports0..5 retain n, lambda, nu, nu squared, sqrt lambda, and s.
Scratch6..18 is reused and restored by each actual subroutine. 

### `slots`

 Six persistent local words; every local work stack is empty at boundaries. 

### `command_eval`

 Exact parameter construction. The returned words are physically retained on
ports1..5; all local scratch stacks are empty, and the original binary n survives. 

### `program_trace`

 The compiled local schedule has one actual trace and a uniform all-port,
every-prefix bound. The polynomial depends on n and the retained binary width. 

### `sharedStacks`

 Fixed pre-DFS bank: input n267, retained schedule s266; remaining local ports
use their unchanged low indices. All off-bank caller data are framed. 

### `sharedProgram_trace`

 Every retained caller stack contributes to the shared native schedule's
prefix bound; the bound is on the actual lifted trace. 

### `resetShared`

 Eight fixed register writes discharge the concrete native caller's
arbitrary register contents before entering the schedule subroutine. 
