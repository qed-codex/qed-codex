---
{
  "module": "OAI/Computability/VPVNP/RegisterTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegisterTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegisterTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed register instruction tables on binary stacks

A deterministic register program for a coordinate query can run for
exponentially many instructions. Its program counter is finite control.
Ordinary instruction callbacks resume directly at the next program counter,
so the machine needs no stack of fuel credits. Each instruction restores a
bank of width-bounded registers before the next instruction starts.


### `step`

 The next program counter and register contents for a register-only opcode. 

### `Runs`

 Runs between instruction-entry boundaries, including the boundary at which a caller takes over. 

### `code`

 Fixed physical binary control. Nonlocal callbacks are exit labels for callers. 

### `bank`

 Initial bit stacks for the register table, encoding the public words, persistent word, and
registers with an empty address log. 

### `one_run`

 One register instruction is simulated by the physical machine within a
quadratic word-length bound. 

### `run`

 End-to-end simulation between arbitrary instruction-entry labels. Each
stack has polynomial height independently of the number of loop iterations. 
