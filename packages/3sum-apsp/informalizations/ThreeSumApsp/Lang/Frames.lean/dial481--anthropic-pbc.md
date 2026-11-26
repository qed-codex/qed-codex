---
{
  "module": "ThreeSumApsp/Lang/Frames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Frames.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Frames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Local variables as a list

In the proof of a procedure body the state is written out as ⟨frame [a, b, …], μ⟩: the list
holds the local variables 0, 1, …, and all further ones are 0.  An assignment to local x replaces
entry x of the list (setLocal).  The rules of this file treat one statement each.  They are told the
value that is assigned or stored, and they ask for one fact about each expression: that its
evaluation stays within the limits and gives this value (Expr.Gives).  This fact and the comparison
of the costs are proved by default from the hypotheses in the context.  Ends.forFrame and
Ends.forShape are the rules for counting loops in this form.  In the names of the rules, To says
that the state is ⟨frame l, μ⟩.

Locals by name, and locals whose values do not matter:

* `setLocals l [(x, a), (y, b), …]` is the list `l` after the assignments `x := a`, `y := b`, ….
  With the names of the locals for `x`, `y`, … it describes the locals of a procedure by name:
  `setLocals [] [(Size, n), (Bound, U), …]`.
* `updateLocals loc [(x, a), (y, b), …]` is the same for locals that are not given as a list.  A
  lemma about a piece of text that several procedures share is stated for arbitrary locals `loc`.
* `refreshLocals l loc xs` is the list `l` with the entries `xs` read from `loc`.
* `LocalsBut xs l loc` says that `loc` agrees with `frame l` except perhaps at the locals `xs`.  In
  an invariant, `xs` are the scratch variables.  `Ends.asFrame` goes from such locals to a list, and
  `LocalsBut.of_eq` comes back.
* `Ends.pieceTo` and `Ends.pieceToThen` use a lemma about a piece of text that assigns only the
  locals `xs`: afterwards the locals are `refreshLocals l loc' xs`, where `loc'` are the locals of
  which the lemma speaks.  The lemma need not mention the locals that the piece does not assign.
* `Ends.forScratch` is the rule for a counting loop whose body may change the scratch variables
  `xs`: the round says nothing about the locals.


 ## The list of the locals 

### `setLocal`

 The list of the locals after an assignment of z to local x.  A list that is too short is filled
up with zeros. 

### `frame_setLocal`

 Reading a local after an assignment. 

### `update_frame_setLocal`

 An assignment to a local, in terms of the list. 

### `frame_append_zeros`

 Zeros at the end of the list do not matter. 

 ## The value of an expression 

### `Expr.Gives`

 The evaluation of e in σ stays within the limits and gives z. 

 ## One statement 

### `Ends.setVal`

 `x := e`, where e gives z, for locals that are not given as a list. 

### `Ends.setValThen`

 `x := e ; s`, where e gives z, for locals that are not given as a list. 

### `Ends.setTo`

 `x := e`, where e gives z. 

### `Ends.setToThen`

 `x := e ; s`, where e gives z.  The rest s of the text gets the steps that are left. 

### `Ends.storeTo`

 `mem[a] := e`, where a gives the address b, which lies in the memory, and e gives z. 

### `Ends.storeToThen`

 `mem[a] := e ; s`, where a gives the address b, which lies in the memory, and e gives z. 

### `Ends.forFrame`

 **Counting loops whose body is a block that changes no local variable**, with the locals as a
list.  Before round j the locals are the given ones with j in the counter, and I j holds of the
memory.  The bound hi gives n, and n fits in a word.  The round is a goal about the body, for the
rules of this file, and its time is body.blockCost, so that no number is typed.  A loop or a call
counts 0 steps in blockCost; for a body that contains one use Ends.forShape. 

### `Ends.forShape`

 **Counting loops whose body may change scratch variables.**  S j s μ' is the state before round
j, with the values s of the scratch variables and the memory μ'; I j holds of the memory.  The
counter of S j s μ' holds j, and S (j + 1) s μ' is S j s μ' with the counter increased; for a shape
fun j s μ' => ⟨frame [.., j, s], μ'⟩ both are proved by default.  The bound hi gives n, n fits in a
word, and the body keeps the shape and takes at most b steps. 

 ## Locals by name, and locals whose values do not matter 

### `setLocals`

 The list of the locals after several assignments, each given as a local and its value. 

### `updateLocals`

 The local variables after several assignments, each given as a local and its value. 

### `updateLocals_frame`

 Several assignments, in terms of the list. 

### `refreshLocals`

 The list `l` of the locals, with the entries `xs` read from `loc`. 

### `frame_refreshLocals`

 Reading a local of `refreshLocals l loc xs`. 

### `SameFrame`

 Two lists give the same local variables: they are equal up to zeros at the end. 

### `sameFrame_nil`

 The empty list gives the same locals as itself. 

### `sameFrame_cons_cons`

 Two lists give the same locals if their heads are equal and their tails give the same locals. 

### `sameFrame_cons_nil`

 A list gives the same locals as the empty list if all its entries are 0. 

### `sameFrame_nil_cons`

 The empty list gives the same locals as a list all of whose entries are 0. 

### `LocalsBut`

 The local variables `loc` are those of the list `l`, except perhaps the locals `xs`. 

### `LocalsBut.eq_frame`

 Locals that agree with a list except at `xs` are themselves given by a list. 

### `LocalsBut.update`

 An assignment, on both sides. 

### `LocalsBut.of_eq`

 Two lists agree except at `xs` if they give the same locals once these entries are copied.  For
two lists that are written out, the hypothesis amounts to the equations between their entries, where
an entry that is missing counts as 0. 

 ## A piece of program text with a lemma of its own 

### `Ends.asFrame`

 **From locals that are described by `LocalsBut` to a list.**  The entries `xs` of the list are
read from `loc`. 

### `Ends.pieceTo`

 **A piece of text that assigns only the locals `xs`**, at the end of the program.  `h` is the
lemma about the piece.  Afterwards the locals are the list `l` with the entries `xs` read from the
locals `loc'` of which the lemma speaks. 

### `Ends.pieceToThen`

 **A piece of text that assigns only the locals `xs`**, followed by the rest of the program,
which gets the steps that are left. 

 ## Counting loops with scratch variables 

### `Ends.forScratch`

 **Counting loops whose body may change the scratch variables `xs`.**  Before round j the locals
are the given ones with j in the counter and anything in the scratch variables, and I j holds of the
memory.  The round says nothing about the locals.  The counter is not among the scratch variables,
so the body does not assign it.  The bound hi gives n, n fits in a word, and the body takes at most
b steps. 
