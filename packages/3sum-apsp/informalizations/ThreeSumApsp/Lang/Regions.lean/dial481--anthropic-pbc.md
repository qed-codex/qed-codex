---
{
  "module": "ThreeSumApsp/Lang/Regions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Regions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Regions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Regions of the memory, and the cells that a step leaves alone

A region is given by its first address `a` and its number `n` of cells.  `Inside a n b` says that
the cell `b` lies in it, `Outside a n b` that it does not, and `Apart a n a' n'` that two regions do
not meet.  `InOrder top [(a, n), (a', n'), …]` says that the listed regions lie one behind the other
and end at or below `top`.  All of these abbreviate linear inequalities.

`SameOn K μ μ'` says that the memory `μ'` agrees with `μ` on every cell that satisfies `K`.  It is
the one notion of "these cells are unchanged": a routine promises `SameOn K μ μ'` for the cells
`K` that it leaves alone.  (It is `Set.EqOn μ' μ {b | K b}`, stated with a predicate: the conditions
`K b` that occur are linear inequalities between addresses and are used as such.)  The usual choices
of `K` have names.

* `SameOutside μ μ' a n`: all cells outside one region; `SameOutside2` and `SameOutside3`: all cells
  outside two or three regions.
* `Kept μ μ' fr`: all cells below the free pointer `fr`.
* `KeptBut μ μ' fr out len`: all cells below `fr` outside the region of an output.

## How a fact is carried from one memory to a later one

A predicate `X` about a memory has one lemma of the name `X.keep` and of the form

  `theorem X.keep (h : X μ …) (hs : SameOn K μ μ' := by light_keep) : X μ' …`

where `K` describes the cells that `X` reads; `Seg.keep` is the model.  The argument `hs` has a
default proof.  So `h.keep`, with no argument, stands for "`h` still holds in the memory that is
asked for here".  The default proof `light_keep` uses every hypothesis of the form `SameOn _ ν ν'`
in the context, that is, the promises of the steps that were taken since `h` was obtained, and the
inequalities in the context that say where the regions lie.  In the proofs a promise is named when
the step is taken, as `same₂` in `rintro _ μ₂ ⟨sY, same₂⟩`.

`wrote μ dst f j` is the memory `μ` after a loop has written `f 0`, …, `f (j - 1)` to the cells from
`dst`.


 ## Regions 

### `Inside`

 The cell `b` is among the `n` cells from address `a`. 

### `Outside`

 The cell `b` is not among the `n` cells from address `a`. 

### `Apart`

 Two regions of the memory, of `n` cells from `a` and of `n'` cells from `a'`, do not meet. 

### `InOrder`

 A map of a part of the memory: the regions of the list lie one behind the other, in the order of
the list, and the last one ends at or below `top`.  A region of the list is the pair of its first
address and its number of cells. 

 ## Memories that agree on some cells 

### `SameOn`

 The memory `μ'` agrees with `μ` on every cell that satisfies `K`. 

### `SameOutside`

 The memory `μ'` agrees with `μ` outside the `n` cells from address `a`. 

### `SameOutside2`

 The memory `μ'` agrees with `μ` outside the `n` cells from `a` and the `m` cells from `b`. 

### `SameOutside3`

 The memory `μ'` agrees with `μ` outside three regions: `n` cells from `a`, `m` cells from `b`,
and `k` cells from `c`. 

### `Kept`

 No cell below the free pointer has changed. 

### `KeptBut`

 No cell below the free pointer has changed, except the `len` cells from `out`. 

### `SameOn.cell`

 The case of a single cell. 

### `SameOn.mono`

 Fewer cells are kept. 

### `SameOn.then`

 Two steps that keep different cells. 

### `SameOn.write`

 Writing a cell that need not be kept. 

 ## Writing a region cell by cell 

### `wrote`

 The memory `μ` after `f 0`, …, `f (j - 1)` have been written to the cells from `dst`. 

### `wrote_zero`

 Nothing has been written yet. 

### `wrote_done`

 A cell that has been written. 

### `wrote_rest`

 A cell that has not been written (yet). 

### `wrote_succ`

 One more cell is written. 

### `update_wrote`

 A write outside the cells that have been written can be done first. 

### `sameOutside_wrote`

 Writing `j ≤ n` cells from `dst` changes no cell outside the `n` cells from `dst`. 

 ## The tactics 

### `light_keep_steps`

 A part of `light_keep`.  For each hypothesis `SameOn K' ν ν'` in the context whose condition
`K' x` follows by linear arithmetic, it adds the equation `ν' x = ν x`.  Then it replaces the writes
`Function.update ν b z` and `wrote ν dst f j` by their definitions. 

### `light_keep_core`

 The work of `light_keep`; the lemmas in brackets are used when `K x` is simplified. 

### `light_keep`

 `light_keep` proves `SameOn K μ μ'` (also written `SameOutside`, `Kept`, …) or `μ' b = μ b`.

It takes a cell `x` with `K x`.  Each hypothesis `SameOn K' ν ν'` in the context whose condition
`K' x` follows by linear arithmetic from the hypotheses yields the equation `ν' x = ν x`; the writes
`Function.update ν b z` and `wrote ν dst f j` are replaced by their definitions.  Then `μ' x = μ x`
has to follow from these equations.  If it does not, the tactic tries once more after simplifying
`K x`, which computes the lengths of lists.  The order of the hypotheses plays no role, and further
hypotheses do no harm. 

### `light_keep`

 `light_keep [h₁, h₂, …]` is `light_keep` with the terms `h₁`, `h₂`, … added to the context; the
simplification of `K x` may rewrite with them as well.  So they can be promises, inequalities, or
lemmas on the length of a list. 

### `light_order`

 `light_order` proves `InOrder top [(a, n), …]` by linear arithmetic from the hypotheses in the
context, which may be of this form themselves. 
