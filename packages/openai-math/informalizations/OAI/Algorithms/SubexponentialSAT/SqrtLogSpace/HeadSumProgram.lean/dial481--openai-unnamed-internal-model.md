---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The head rescan retains one raw Boolean assignment and a binary countdown.
The full-key/correction gate is executed for every candidate. Accepted values
are accumulated before the cursor advances, including the empty-head case. 

### `Cursor`

 The terminal cursor may have one overflow bit; it is never queried. 

### `seed`

 The existing head preparation stores its actual zero word on651. Two
copies initialize cursor and binary-fuel construction; the head sum is reset. 

### `additionRegisters`

 Addition consumes the assignment product directly at854. The two
coefficient scratch ports avoid the retained product zero/table caches. 

### `addition_project`

 The local projection uses the actual product idle layout left by the
factor interpreter; no array is copied and no layout service is assumed. 

### `add_eval`

 One concrete dense addition preserves every caller stack except the two
named arrays. Its local temporary growth is polynomial in their bounded size. 

### `accumulate`

 Accepted factors are added and their reusable arithmetic workspace is
reclaimed before the controller increments its candidate word. 

### `gateValue`

 The tested value uses every integer-signature component and local correction bit. 

### `body_eval`

 Compose the real gate, the selected branch, and the real ripple increment.
The branch contract is an internal composition rule; the final scan instantiates
it with the named assignment-factor and dense-add commands. 

### `body_cursor_next`

 The counter interface sees the exact next index even after the last word
has overflowed; the overflow word is excluded from further callbacks. 

### `fold`

 The mathematical output recurrence keeps only the current accumulator.
It specifies the native counted scan, and is not an executable assignment list. 

### `command_fold`

 Output correctness for the actual indexed head loop. The step premise is
instantiated by body_eval and the concrete accepted-factor composition. 

### `fold_decode_sum`

 A valid additive accumulator decodes to the exact sum of all visited
contributions, with no retained family of previous states. 

### `range_sum_eq_assignments`

 Numeric bit-counter order covers every head assignment exactly once. 

### `add_prefix`

 Dense addition's local working set is independent of the retained caller
frame. The physical input cap P is supplied by the bounded arrays and caches. 

### `Cursor.assignment_word`

 The actual numeric cursor denotes the assignment used by the full-key gate. 

### `cursor_gate_iff`

 With the staged local E mask and all-one local head mask, the actual gate
is exactly the full integer-signature fiber restriction. 

### `addition_input_length_le`

 The local addition cap follows from the physical caches and the proved
polynomial encoded-array bound, independently of the caller's frame bound. 

### `reset_prefix`

 The paid arithmetic reset only clears cells; it preserves the same
per-stack envelope throughout its actual lifted execution. 

### `accumulate_prefix`

 Array addition followed by reclamation preserves one caller envelope.
Only the independent physical cap of the28 arithmetic ports enters the budget. 

### `finalize`

 Both binary controller words are physically reclaimed after the exhausted
loop, including the possible terminal overflow bit of the assignment cursor. 

### `scan`

 The complete head-rescan control, including paid initialization and cleanup. 
