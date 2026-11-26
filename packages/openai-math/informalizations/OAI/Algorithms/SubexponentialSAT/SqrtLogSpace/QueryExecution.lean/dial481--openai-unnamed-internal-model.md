---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Composition of the concrete streamed query. The traversal resource lemma
keeps the per-head execution time separate from its prefix storage bound;
neither the number of assignments nor their running time is used as space. 

### `PrefixBound`

 A source-prefix assertion for the actual compiled command table. 

### `PrefixBound.monoSteps`

 Restrict a prefix certificate to a shorter execution prefix. 

### `PrefixBound.withHalt`

 Extend a command-prefix certificate through the compiled halt transition. 

### `body_prefix`

 The actual frame parser and cleanup are composed with the measured work
trace. The possibly exponential work time does not enter the storage bound. 

### `headLoop_resources`

 The list is a proof index for the already-emitted frame stack, not an
operational enumeration. This lemma composes actual callback traces and
preserves one fixed endpoint envelope throughout both representative passes. 

### `replay`

 Re-read the existing representative stack for either of the two passes.
Both destination words are replaced by paid commands, including on the
second pass after the first has decremented its address to the node offset. 

### `replay_nil`

 Zero heads execute the real copy/test/halt path and invoke no head work.
In particular the repeated-pair base address649 is retained on this edge case. 

### `cleanup`

 Return all borrowed current-head words before the attained-signature DFS
resumes. Ancestor frames and the emitted representatives are retained. 

### `result_high_frame`

 This includes the persistent tuple ports836/837/842/845, node850,
correction masks857/858, accumulated jets863, and the full baseline869. 

### `run_space`

 The same measured tail consumes the completed product and restores all
borrowed tuple words. Its local time is polynomial and does not depend on the
number of previously emitted signatures. 

### `command`

 A new finite-difference pair begins with the actual zero dictionary and
the current reversed free-coordinate masks are expanded to ambient masks.
Neither a support family nor a tuple family is stored by this command. 

### `support_command_run`

 This instance starts from the exact masks emitted by the ternary pair
DFS. Its outputs are the transported supports used by the actual native
factor correction and head predicate; no high coordinate enters either set. 
