---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word code for the greedy descriptor choices

A vertex's record contains a fixed number of forbidden expressions. Each
expression is the xor of the words named by its row of pointers. A color
test uses one pointer to the neighbor's current assignment. The tag tests
in Appendix C use the arc displacement, up to two increments, and the
neighbor's current offset. Zero terms can be supplied by a shared zero cell.
The instruction table is fixed once the degree and row arity are fixed.

Starting from candidate zero, each pass increments the candidate exactly
when it occurs among the forbidden expressions. The length of that list
bounds the number of passes needed, including when entries are repeated.


### `readExpression`

 Pointer row traversal, with ordinary word-address arithmetic. 

### `readRows`

 Values of all forbidden expressions, in descriptor order. 

### `compareWord`

 The unsigned quotient of a word by itself tests whether it is nonzero.
The product in register 6 stays one precisely while every comparison differs. 

### `choose`

 Register 0 holds the first descriptor address. The other input registers
may contain arbitrary values. Register 2 returns the least missing index. 

### `climb`

 Successive candidates produced by the fixed number of complete row passes. 

### `choose_trace`

 The block reads from the descriptor address in register zero. The stated
event counts include all row dereferences, even for a repeated forbidden word. 

### `chooseFromState`

 Starting a fresh burst call uses the persistent input as the row address. 

### `choose_native`

 Native execution from freshly reset private memory and registers. The candidate
returned in the persistent state is the least omitted nonnegative index. 

### `visitHead`

 A visitor's header contains the label destination and the next vertex's
header address. The forbidden operand rows immediately follow that header. 

### `visitCode`

 Instructions for one greedy vertex visit, loading its record, choosing a label that passes
the forbidden-expression tests, and advancing the cursor. 

### `visitMachine`

 Instantiate the greedy visit at the specified word width with register four as its return
register and no public operands. 

### `Visit`

 Observable execution of one complete vertex visit. The output label is
stored externally and the persistent return word is the next record address. 
