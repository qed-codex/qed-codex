---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual fixed binary comparison/update used by the streaming selector.
Its queue port is a bounded iterator frame, not a list of candidate records. 

### `updateProgram`

 The original numerical comparator and strict update, with a concrete halt. 

### `update_trace_space`

 A single local update has polynomial space at every instruction prefix.
The bound includes the untouched iterator/caller frame on port 8. 

### `installProgram`

 Bootstrap from the separately paid first score. 

### `install_trace_space`

 The first incumbent is installed by finite copying instructions. 

### `update_numeric`

 The finite bit routine uses the same strict comparison as the cached
semantic update, retaining the incumbent on an equal score. 

### `appendPorts`

 Serialization uses the existing measured bit escaping routine. 

### `append_eval`

 Exact measured appending, with no retained candidate family. 

### `appended_history_length`

 Exact retained history growth: one selected payload and its framing bits.
No trial payload or losing score is retained in the history stack. 

### `encodedHistory`

 Only selected rows occur in this proof-level serialization. 

### `readEntry`

 Read the actual retained candidate and its full binary score. 

### `visits_best`

 Refinement of a genuine iterator trace to the cached strict argmin.
`ranks` is proof evidence of visits, never a machine stack or runtime list.
The body premise concerns its actual measured execution and must be discharged
by candidate loading, normalization, exact scoring, and `updateProgram`. 

### `visits_minimum`

 Every losing callback contributes a comparison constraint on the actual
returned binary score, not only on a semantic annotation. 

### `enumerate_minimum`

 Complete coverage and measured time of the actual overflow-controlled
scan. The single seeded incumbent is paid separately by `install_trace_space`.
Callback correctness is an intermediate implementation contract. 

### `command`

 The fixed-width shape is copied before padding, and survives every score.
Only the actual canonical mass word is padded; the final exact count has its
own canonical output path. 

### `leafRegisters`

 The query owns the low scratch bank; the retained selector score and
fixed unary shape are outside it. All other selector stacks are framed. 

### `command`

 Three measured parameter copies, positive modulus normalization, and the
actual conversion from binary round count to the unary loop controller. 

### `normalize_eval`

 A native positive normalizer changes only the modulus word. 

### `unary_eval`

 The round counter is converted physically; its value, rather than its
binary word length, becomes the number of future rounds. 

### `command_eval`

 Actual initializer, including every copy, arithmetic microstep, unary
output bit, and return. The enclosing measured preparer supplies the initial
scratch invariant when this local routine is integrated. 

### `result_modulus`

 Saved modulus has the exact canonical width used in the fixed-square
candidate-count estimate, even if the arithmetic preparer emitted padding. 

### `trace_space`

 The initializer is polynomial work, so its complete local trace bounds
all stack prefixes, including its persistent saved parameters. 

### `corePorts`

 Only the fixed nine-port argmin core is reset after its three prepared
parameters have been saved. History, formula, and count output are framed. 

### `saveShape`

 Preserve the initial unary round count as a fixed score width before the
round controller starts consuming its own copy. This is separate from numeric
preparation because initial deterministic rows must be serialized at the same
canonical width before the argmin core is cleared. 

### `finishSetup`

 Invoke only after the initial deterministic history is constructed using
the canonical width. This stage never repeats numerical preparation. 

### `zeroStacks`

 Physical construction of the one retained zero candidate. The depth
counter is copied from817; the canonical modulus780 determines chunk width. 

### `zero_eval`

 No width product is materialized in binary or used as a host-language
loop: the finite constructor scans the modulus once for each binary depth
counter iteration, and charges every copied and emitted bit. 

### `registers`

 These are the fixed leaf ports, not an input-dependent bank allocation. 

### `CoreClean`

 The four arithmetic scratch words and exhausted parser queue are empty at
candidate boundaries; retained best words are not part of this condition. 

### `update_eval`

 Actual score comparison, with an exact whole-bank frame statement. 

### `install_eval`

 Bootstrap pays the first full score and stores it by actual copying. 

### `attempt`

 Every attempted candidate, including every loser, performs preparation,
exact mass evaluation, and physical fixed-width score padding. `mass` is fixed
finite syntax; its implementation proof remains an integration obligation. 

### `attempt_eval_of_query`

 Physical padding connects an actual complete query trace to the selector
score ABI. This lemma assumes executions, never an unimplemented query oracle. 

### `body_eval_of_attempt`

 Once the actual preparation/query/padding trace is supplied, the cached
minimum step follows with every other stack preserved. 

### `append_eval`

 Serialize precisely one attained winner and clear its cached score. 

### `resetGuard`

 The outer unary controller reads a preserved counter stack. Resetting its
flag after the inner scan is an actual charged instruction. 

### `round`

 One seed evaluation is paid before the full overflow-controlled scan.
The scan also visits zero; strict comparison makes the repeated seed harmless.
No exponential candidate list is present in the instruction sequence. 

### `round_eval_of_stages`

 Measured composition uses the actual execution of each fixed stage.
This is deliberately an intermediate trace lemma, not a closed query service. 

### `StageSpace`

 Every primitive source-table prefix of a stage, including every stack.
The bound is uniform across calls; it contains no completed-visit counter. 

### `round_space_of_stages`

 Stage bounds combine by their common maximum. In particular the number
of streamed candidates never multiplies the retained-space bound. 

### `round_halt_space_of_stages`

 The actual final halt also obeys the same uniform source-prefix bound. 

### `rounds_space`

 The outer unary loop also uses a uniform space invariant. Its round count
changes the time bound, never the maximum retained space. 

### `roundBudget`

 A fixed explicit budget pays the seed, every visit and advance, the
retained winner append, and the outer flag reset. 
