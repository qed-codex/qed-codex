---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecWorklistProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecWorklistProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecWorklistProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local encoded worklist updates by a fixed Boolean-stack program

The branch decision and child records are supplied as data. No formula search
or splitting callback is an instruction. Pending work, accumulated leaves, and
both child sources may have arbitrary suffixes; only the current records are
read. The five stack ports are pending, leaves, child A, child B, and scratch.


### `record`

 One tagged, escaped list record. The payload may encode a whole CNF. 

### `copyAt`

 The three copy ports are fixed when this finite program is constructed. 

### `copyAt_eval`

 A framed copy reads one record only, including when the source contains
more records. The exact trace is inherited from the actual fixed copy program. 

### `data`

 Register 2 is the supplied terminal decision; register 3 is the skip flag.
Every stack may contain an arbitrary suffix except for the empty local scratch. 

### `branchCommand`

 Push B before A, putting A at the top of the depth-first pending stack. 

### `command`

 Both branches consist exclusively of calls to fixed finite bit programs. 

### `program`

 Four Boolean registers, five Boolean stacks, and 61 fixed control labels.
These counts do not depend on payloads, formula width, or the number of leaves. 

### `terminal_trace`

 Actual finite-program trace: emit the current record and preserve all suffixes. 

### `branch_trace`

 Actual finite-program trace: discard current, then push supplied B and A.
No read or copy of the accumulated pending or output suffix occurs. 

### `terminal_cost_le`

 The bound depends only on the emitted record, never on old output length. 

### `branch_cost_le`

 Only the discarded record and the two child records enter the time bound. 

### `terminal_primitive`

 The finite bit program has an actual primitive-machine execution with a
fixed linear factor. The old pending and leaf lengths are absent from the bound. 

### `terminal_list_trace`

 Instantiating a payload encoder connects the bit trace to a list worklist. 
