---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeTerminal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeTerminal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeTerminal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual outer-CNF terminal handling. The ambient unary header is retained;
an empty formula emits its full count 2^n, and an empty clause emits zero. 

### `command`

 Nonterminal leaves pass through with both classifier flags available. 

### `result_count`

 The outer trivial cases produce the full ambient count, including n=0. 

### `program_trace`

 The all-prefix bound includes every persistent stack from the DFS frame. 

### `prepare`

 Dispatcher-local temporary cleanup is executed, not assumed at the DFS boundary. 

### `classifier_space`

 Only the classifier's local body word contributes to its temporary bound.
The retained DFS frame is bounded by the same unchanged `bound`. 

### `powerCall_space`

 The power producer's local footprint is independent of retained DFS words. 

### `power_bounded`

 Copy and power synthesis retain the caller's same per-stack envelope. 

### `prepare_bounded`

 Dispatcher scratch cleanup is non-growing, including arbitrary old words. 

### `command_bounded`

 Every terminal branch retains one fixed bound across arbitrary DFS frames. 

### `readyCommand_bounded`

 The complete ready terminal command preserves the same DFS stack bound.
The two local budgets depend only on the body and ambient dimension. 
