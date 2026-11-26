---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MinimumProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MinimumProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MinimumProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed program selecting the first minimum unary score

The input is a framed list of prepared unary scores. Scores are represented
by list lengths. The program returns the selected zero-based index in unary.
All control, registers, and stack ports are fixed independently of the input.


### `compare_eval`

 A genuine call to the destructive comparator, including all required
framing and bounds on the two residual scratch stacks. 

### `Invariant`

 Invariants at record boundaries. The score bound is independent of how
many records remain, because the stored best score only decreases. 

### `scanBudget`

 A sum of actual per-record bounds, with the unary index increasing. 

### `loop_eval`

 The fixed parser/callback loop visits every record in order. 

### `command`

 The program is one fixed finite instruction table for every nonempty list. 

### `firstMinimum`

 The score/index pair selected by the first-minimum rule. 

### `program_runsIn`

 An actual halting trace, with polynomial cost in the prepared records. 

### `indexChoice`

 An indexed specification of the same earliest-minimum rule. 

### `program_candidates`

 The unary program's output indexes the original candidate chosen by the
natural-number conditional-expectation algorithm. 
