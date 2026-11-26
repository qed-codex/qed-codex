---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCoreChildProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCoreChildProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCoreChildProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual encoded construction of the core child

The caller supplies a forward encoded core clause on stack 9, an encoded
selected family on stack 12, and the parent formula on stack 13. All other
stacks are empty. The program builds the core record, removes every clause
equivalent to a selected clause, restores record order, and calls the concrete
absorber. The result is on stack 13; every other stack is empty.

The finite program does not depend on any of its three input values. The
equivalence tests, framing, reversal, and absorption are actual bit programs.


### `seedCore_eval`

 Construct a singleton encoded list by moving and escaping the actual
core payload. Neither the payload nor its length appears in finite control. 

### `eraseWithAccumulator`

 Finish an actual filter pass with an already encoded output accumulator.
The caller can put reversed petal records in the accumulator as well as the
singleton core used below. 

### `eraseWithAccumulator_eval`

 This shared erasure block accepts any genuine encoded record accumulator.
Its bound counts the accumulator bits, even if none of the parent clauses is
retained. Every payload, including an empty payload, is copied by real loops. 

### `prepare`

 Prepare the unabsorbed core child. The singleton core accumulator is
reversed together with the kept records, placing the core first. 

### `result_length_le`

 The returned child adds at most the serialized core record to the parent
length. This is independent of list order and duplicate literal encodings. 

### `command_eval`

 The complete source execution has no assumed semantic callback. It
consumes the core and selected family, returning the exact absorbed child. 

### `program_runsIn`

 Fixed finite code, with its final halt charged to the same quadratic
bound in the lengths of the three actual encoded inputs. 

### `result_set`

 Set semantics of the exact list output, valid even with reordered or
repeated literals and repeated clauses in any of the supplied lists. 

### `result_childA_set_of_selected`

 A selected family need only have the right clause sets. Literal order in
the gathered clauses need not match the core-then-petal concatenation order. 
