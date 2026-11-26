---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighMarkedFrontend.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighMarkedFrontend.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighMarkedFrontend.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The original actual marked-scope/high-mask/parameter frontend is lifted
into the shared leaf ABI. Upper caller words and the marked mass collector
are retained; the lower workspace is reclaimed by an actual cleanup program. 

### `markedInput_bound`

 Reference staging preserves a physical input cap, apart from its one-bit
flag. This cap is independent of retained upper caller words. 

### `command_eval`

 Actual marked frontend execution and input-dependent time do not require
a bound on suspended collector or caller words. 

### `run`

 Full native frontend outputs, current marked scopes and high mask, and
all-prefix storage belong to the same actual lifted execution. The physical
local input cap is separate from retained upper caller stacks. 

### `accepted_command_eval`

 The unmarked native execution also has a source-dependent time bound
without restricting suspended collector words. 

### `accepted_run`

 The final unmarked count regenerates its own scopes and high set from the
current source rows, using the same actual frontend as each marked query. 

### `collector_frame`

 Physical protected collector words are not frontend outputs. 

### `result_kept_frame`

 The concrete return collector's retained words survive the actual
frontend result. This includes immutable sources and every caller bank. 

### `command_kept_frame`

 Exact kept-word frame for any actual marked frontend execution, obtained
from its concrete evaluated output by deterministic execution uniqueness. 

### `accepted_command_kept_frame`

 The accepted history-only frontend preserves the same concrete retained
words before its final count is installed on788. 
