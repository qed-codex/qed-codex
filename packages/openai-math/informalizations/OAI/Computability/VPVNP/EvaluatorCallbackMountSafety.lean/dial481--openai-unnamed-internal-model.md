---
{
  "module": "OAI/Computability/VPVNP/EvaluatorCallbackMountSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCallbackMountSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCallbackMountSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Mounting the streamed readers in the digit scheduler

Each scalar read operates on the unary label and the weighted payload. The
digit table, exponent counters and repeat stack retain their contents during
that read. Their lengths enter only the space bound for the enclosing machine.


### `workspace`

 Callback capacity available on all digit columns. 

### `frobenius_bounded`

 All paths of a Frobenius callback at a reachable column. 

### `label_bounded`

 All paths of a multiplication callback, including early rejection by the
basis-index chooser. The temporary digit holds exactly one field-cardinality
word when the repeated callback is entered. 
