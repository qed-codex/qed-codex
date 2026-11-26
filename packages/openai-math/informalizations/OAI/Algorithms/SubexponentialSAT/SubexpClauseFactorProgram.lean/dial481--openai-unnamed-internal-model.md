---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpClauseFactorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpClauseFactorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpClauseFactorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical construction of one clause factor

The preserved input ports contain the field modulus, declared-variable shape,
padded-array shape, chunk width in unary and binary, encoded clause, and field
word width. The produced scope uses stable last-occurrence order; the table
contains Boolean values in descending local scalar-rank order.


### `scopeOf`

 This view retains the exact scope order emitted by the physical producer. 

### `makeTable_eval`

 The lifted local table program still preserves the binary chunk width and
all higher caller registers. The final zero-valued fuel word is returned so
the caller can physically clear its full remaining width. 

### `cleanup_eval`

 Zero-valued padded counters are really consumed. Their full word widths
are charged in this cleanup, including the remaining fuel word. 

### `makeCount_eval`

 The actual encoded scope determines the unary arity and binary p^arity
fuel. Only their representations, not their numeric values, are existential. 

### `command_eval`

 Complete physical construction from one canonical clause and preserved
parameter words. The scope and enumeration fuel are both produced by the
program. The only remaining hypotheses describe its input representation. 

### `program_runsIn_raw`

 The raw scope bytes are independent of the finite-index bound proof. 
