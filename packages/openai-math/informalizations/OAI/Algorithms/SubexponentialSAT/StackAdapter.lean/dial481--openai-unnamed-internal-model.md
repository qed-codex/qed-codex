---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StackAdapter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackAdapter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackAdapter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adapting the verified TM2 microstep expansion to finite stack programs

This layer handles finite source control, stack-index reindexing, raw input,
and the one-bit output convention. It supplies actual transition equations.


### `sourceTransition`

 Finite dispatch for one source micro-instruction. 

### `compiledMachine`

 The fully specified primitive-bit compilation of the fixed source machine. 

### `overhead`

 Fixed source-block size times fixed alphabet/block-code simulation cost. 

### `compiled_execution`

 Actual source traces become actual primitive traces at fixed multiplicative cost. 

### `simulation`

 A proved concrete compiler certificate, with every decoder and trace obligation discharged. 

### `macrostep_to_primitive`

 A fixed-alphabet TM2 bound is sufficient: this theorem supplies the actual
constant-overhead primitive compiler rather than assuming one exists. 
