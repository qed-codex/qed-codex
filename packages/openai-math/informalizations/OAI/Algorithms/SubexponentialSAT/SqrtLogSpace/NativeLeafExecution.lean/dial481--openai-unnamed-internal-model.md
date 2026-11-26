---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete shared-ABI loading, local execution and whole-count export for a
DFS leaf. The local command remains explicit; its actual execution proof is
supplied by the streamed leaf construction. No new machine service is defined. 

### `call_export_execution`

 The local compiled halt is paid before the full count word is copied out;
the leaf bank is then physically cleared, with every prefix bounded by B. 

### `command_execution`

 Concrete input words, empty worker ports and reset registers are produced
by the loader. The local bound depends on those input sizes independently of
the suspended DFS frame. The caller supplies a proof of the explicit local
command, rather than an abstract evaluator or layout service. 
