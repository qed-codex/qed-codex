---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed per-assignment factor evaluation. Factors are dispatched by runtime
ID; hash rows are expanded and tested by the computed idempotent, the marked
clause is multiplied directly, and added neutral factors contribute one.
Every operation below is an actual finite instruction table or native loop. 

### `indicatorStacks`

 The indicator's coefficient port78 is relocated; runtime theta78 stays
available to every subsequent source-row computation. 

### `choose`

 The role flag is tested before any arithmetic or source worker can reuse
its registers. The neutral case performs no source lookup. 

### `assignment`

 Complete assignment callback expected by the wide moment assembler. The
before/after helpers save the current head sums/products, form the actual
bucket/head choice, compute its Boolean weight, and restore the caller. 
