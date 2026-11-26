---
{
  "module": "OAI/Computability/VPVNP/RankCursorRegisters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorRegisters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorRegisters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A reusable physical cursor for the rank scan

A scalar coefficient supplies one zero-test bit. The cursor reads that bit,
computes its next two indices, copies them into its input registers, and
emits a new loop marker. A zero marker stops the enclosing loop with the
rank in input register one. A one marker calls the scalar query again using
the updated indices.


### `R`

 Number of cursor word registers, comprising eight inputs, six outputs, and the scratch
registers of the control program. 

### `arg`

 Address of one of the eight input words in the rank cursor’s physical register file. 

### `resultReg`

 Address of one of the six output words produced by the rank cursor control program. 

### `Port`

 The cursor’s word-machine ports together with the flag stack for the zero test and loop
decision. 

### `frame`

 Extend a word-machine stack bank with the supplied list of cursor flags. 

### `bank`

 Initial cursor stacks containing the persistent word, the specified register file, empty
machine scratch, and the supplied flag stack. 

### `continuing`

 The loop bit associated with a cursor state, true while coefficient queries continue and
false when the rank has been returned. 

### `Stores`

 Input register zero is overwritten by the next test. Register three
retains the fixed column bound, and registers four through seven stay zero. 

### `next`

 One fixed step, independent of register width, rank bounds, or the
coefficient oracle. The two indices are ready for the next iteration. 

### `clock`

 Step bound for one cursor update, including the zero-test input, control instructions,
index copies, and the next loop bit. 

### `next_runs`

 The next flag and register bank exactly implement the abstract transition.
In the halting case the first index is the answer and the second is zero. 

### `initial`

 Place a legal cursor in registers at the start of a scan. Only the two
indices and the column bound need nonzero words. 

### `next_space`

 Every intermediate physical stack respects the same quadratic working
space allowance, even when an arbitrary flag tail is carried through. 
