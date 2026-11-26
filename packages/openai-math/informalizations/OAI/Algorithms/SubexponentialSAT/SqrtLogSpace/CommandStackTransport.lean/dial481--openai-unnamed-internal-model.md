---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandStackTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandStackTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CommandStackTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 All-prefix resource transport for the existing exact-time tape replay.
The imported avoidance certificate excludes reads as well as writes, including
`peek`. Erasing hidden caller data is a proof construction only: the actual
instruction table and its measured number of steps remain unchanged. 

### `projectState_rebase`

 A concrete parameter bank disjoint from hidden storage is unchanged by
the proof-only shadow projection. Registers are always retained. 

### `shadow_stack_bound`

 The shadow state retains only visible inputs. Its storage bound does not
contain the size of the hidden collector or incumbent. 

### `trace_prefix_rebase`

 An arbitrary prefix of the rebased execution is the rebase of the exact
same-length prefix of the original execution. 

### `trace_stack_bound`

 Only hidden caller stacks contribute the frame bound. Every visible stack
is controlled by the actual local trace, with no multiplicative recurrence. 

### `eval_shadow`

 A local execution on the empty hidden shadow yields an execution of the
same fixed command on the actual caller, at exactly the same step count. 

### `eval_shadow_prefix_bound`

 The local all-prefix bound is transported through the compiled command,
including its final halt. Hidden external words are restored unchanged. 

### `eval_shadow_prefix_frame`

 Hidden caller words are preserved at every prefix of this same replayed
execution, including prefixes within called finite instruction tables. 
