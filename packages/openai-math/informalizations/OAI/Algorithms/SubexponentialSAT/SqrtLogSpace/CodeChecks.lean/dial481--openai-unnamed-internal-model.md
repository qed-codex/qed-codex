---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeChecks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeChecks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeChecks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Space of the concrete sparse-code predicates

The local-code and Walsh predicates are polynomial-time bit programs. These bounds apply
to every candidate, including losing candidates, and every stack in each actual source
prefix. They are intended as the body estimates of bounded-memory enumeration; the
materialized candidate-family programs are not used here.


### `ScanState`

 Both scans use fixed finite control and retain one encoded counter tuple. 

### `copy_convert_eval`

 Conversion is paid for afresh at every visit. The current counter remains
available, while the temporary input is consumed and all off-port stacks survive. 

### `invalid_conversion_eval`

 Invalid digits pay for copying, conversion, the branch, and full payload
cleanup. They do not change any retained stack or the rejection latch. 

### `latchReject`

 The result is a one-bit OR latch, not a retained list of check results. 

### `local_attempts_le_square`

 Invalid two-bit ternary digits cost at most a square of the old complete
matrix-and-word domain. This power is independent of the input. 

### `graph_attempts_eq_square`

 The graph's invalid high-bit words are also charged by a fixed square. 

### `visits_rejection_latch`

 A semantic visit log describes the actual latch updates. The log is proof
data only; the machine retains one Boolean and the current counter word. 

### `graph_stream_body_valid`

 A valid streamed character is checked by the original bit arithmetic. Only
the one-bit rejection latch changes; this includes every off-port caller stack. 

### `local_stream_body_valid`

 A valid streamed local-code word is checked by the original bit arithmetic. Only
the one-bit rejection latch changes; this includes every off-port caller stack. 

### `local_input_bound`

 This includes the caller's retained word on stack21; no stack is omitted. 

### `graph_input_bound`

 Walsh inputs include the full retained caller word on stack33. 

### `local_budget`

 The local predicate has a fixed polynomial budget, independently of acceptance. 

### `graph_budget`

 All scalar comparison and cleanup work is included in the Walsh predicate budget. 

### `local_check_runs_space`

 The actual complete local-word check has the same all-stack prefix estimate on both
accepting and rejecting words. The initial bound includes the suspended caller's stack21.
The final halt is included in both time and space. 

### `graph_check_runs_space`

 One actual Walsh-character check, with all persistent inputs, scratch, and the caller
frame on stack33 included at every source prefix. The retained matrix need not be good. 

### `pair_matrix_frames_eq`

 Matrix scalar order agrees with the original row-major matrix encoding.
The converter therefore stages one actual matrix without recoding a family. 

### `installMatrix`

 Staging a current matrix only clears the old matrix and reverses the
converted payload. No list of all test words is copied. 
