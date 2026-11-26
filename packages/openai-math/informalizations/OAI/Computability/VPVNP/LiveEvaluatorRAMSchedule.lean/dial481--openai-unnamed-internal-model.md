---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scheduled burst calls for one live evaluator transition

Cursor zero selects the transition and saves its five fields in external
scratch. The following calls check one cell of the first tape and then one
cell of the second tape. All four public words are lengths or addresses.
The instruction table is independent of the radius, word width and addresses.


### `Block`

 A native block for the scheduled transition checker with four public operands. 

### `Pub`

 The operand indices for window radius, old configuration, proposed configuration, and
instruction scratch. 

### `Op`

 A single scheduled transition-checker operation over its 32 registers and four public
operands. 

### `ops`

 Sequence of one or more elementary opcodes in their indicated order. 

### `load`

 Public words are radius, old configuration base, new configuration base,
and the base of five scratch words. The old state is read once per call. 

### `first`

 Select the first tape and its first write/move pair in scratch. 

### `second`

 Select the second tape, subtract the first tape length from the old cell
index, and select its second write/move pair in scratch. 

### `locate`

 Read the target state and the write/move pair of the scheduled tape. 

### `finish`

 Compute the next cursor and total number of calls afresh after checking
the cell. This also works after the first call's transition dispatch. 

### `body`

 At cursor zero prepare a transition, otherwise locate and check the indexed tape cell, then
compute the return cursor. 

### `table`

 The burst-call template for the transition schedule with its supplied
instruction-preparation block. 

### `calls`

 One dispatch, followed by a visit to every cell in each tape window. 

### `isFirst`

 Whether a cell-check ordinal belongs to the first tape's window. 

### `visit`

 The scheduled visits form a bijection between the two tape fields and
the noninitial calls, in tape order and increasing cell order. 

### `install`

 Apply an ordered list of word assignments to the evaluator register bank. 

### `loaded`

 The register bank after loading the radius, configuration and scratch addresses, persistent
cursor, and old control word. 

### `load_exec`

 A complete register-bank witness and event trace for the common prefix. 

### `located`

 Selected tape index, bases, target, write symbol and move after three
reads from the five words saved by the preparation call. 

### `locateEvents`

 The read of the selected target and the reads of the write symbol and motion for the tape
chosen by the cursor. 

### `finished`

 Closing register bank has successor cursor and total call count. 

### `program`

 Actual word program for every scheduled call of a fixed evaluator. 

### `body_exits`

 At cursor zero the body executes preparation. At all other cursors it
checks exactly the addressed cell. Both phases compute the successor cursor
in the same final fragment. This equivalence holds on arbitrary memory. 

### `body_cursor`

 Every normal exit publishes the successor and the total, including a
branch of the preparation call that changes external scratch memory. 

### `execute_call`

 Exact native report, with surplus choice bits rejected at the common
exit. Only the final cell accepts instead of returning another cursor. 

### `cell_call_cost`

 Noninitial calls read the old state, three scratch words, one input
cell and one output cell. They never write or consume a choice. 

### `initial_choices_iff`

 The initial call has exactly the preparation fragment's branch choices
and final scratch memory. Loading the public geometry and closing the
cursor are deterministic, including on an initially accepting evaluator. 

### `noninitial_choices_iff`

 The only choice list of a successful cell call is empty, its memory is
unchanged, and its local success predicate is exactly the cell comparison. 
