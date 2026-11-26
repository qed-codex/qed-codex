---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CompileSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CompileSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CompileSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Transfer a genuine bound on every source stack configuration through the
guarded primitive compiler. The bound is independent of the number of source
instructions. Concrete counting programs must prove the source invariant. 

### `compile_word_space`

 Full output-word readback, time, and every-prefix visited space refer to
one and the same primitive execution. The actual source trace and source-stack
invariant must be provided by the concrete counting program. 

### `compile_word_answer_space`

 A full word on an arbitrary fixed tape and a separate Boolean halt are
preserved by the same execution used for both resource bounds. 
