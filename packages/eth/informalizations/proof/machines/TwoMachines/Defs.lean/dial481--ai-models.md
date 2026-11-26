---
{
  "module": "proof/machines/TwoMachines/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/TwoMachines/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/TwoMachines/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two machines in alternation, and a choice between two machines: definitions and statements

**The sentences answered.** Proof of Corollary 11: «Run the algorithm of Theorem A (c), with the
pieces of Appendix B, and the algorithm of Theorem D (b) in alternation, one operation of each at a
time, and output the result of the one that stops first.
Both compute the same number. This multiplies the number of operations of the faster one by a
constant». Step 6 of Appendix D: «In the other cases, that is, if n < K₀^17 or this k exceeds (log
n)^(1/4), the algorithm tries all assignments».

**What is used.** proof/machines/Wrap puts a polynomial-time front end and last step around ONE
machine that is only known to exist (`Wrap.EveryMachineCanBeWrapped`); here two such machines are
combined.

**What is stated here.** All machines are Mathlib's (`Turing.TM2ComputableAux Bool Bool`);
`Wrap.Outputs M x y t` says that M, started on the bit string x, halts within t steps with output y.
* `alt K₁ K₂ pre₁ pre₂ post₁ post₂`: the alternation as a computation cut into steps. Its state is a
  pair: a value that stands for a configuration of M₁ and one that stands for a configuration of M₂.
  One step advances BOTH by one step of their machines. It has a result as soon as one of the two
  has halted.
* `Hosts X N q`: the machine N carries out the computation X cut into steps, with a polynomial
  overhead.
* `Alternates M₁ M₂ pre₁ pre₂ post₁ post₂ N q`: whenever M₁ puts out y₁ on `pre₁ x` within t₁ steps,
  M₂ puts out y₂ on `pre₂ x` within t₂ steps, and the two results agree (`post₁ y₁ = post₂ y₂`), N
  puts out that result on x within q·(min(t₁, t₂) + |x| + 1)^q steps.
* `EveryTwoMachinesCanBeAlternated`: for ALL machines M₁, M₂ with finite alphabets and all
  polynomial-time `pre₁`, `pre₂`, `post₁`, `post₂` there are codings K₁, K₂ of their configurations,
  a machine N with finite alphabets and numbers q₀, q such that N carries out `alt K₁ K₂ …` and
  alternates M₁ and M₂.
* `choose K₁ K₂ test …`, `Chooses M₁ M₂ test … N q`, `EveryTwoMachinesCanBeChosenBetween`: the same
  for “M₁ if the test on the input says so, else M₂”.

**What it does not say.** The overhead is a power q, which may depend on the two machines and the
four functions, where the paper has a constant factor. `Alternates` and `Chooses` fix what N puts
out and a bound on its steps, not
the steps themselves; that N carries out the named computation is said by `Hosts`. If the two
results differ, or one of the machines does not halt in the sense of `Wrap.Outputs`, `Alternates`
asks nothing. 

 ### The two computations cut into steps 

### `alt`

 M₁ on `pre₁ x` and M₂ on `pre₂ x` in alternation. A state is a pair of values, the first for a
configuration of M₁, the second for one of M₂. One step applies the coded step of M₁ to the first
and the coded step of M₂ to the second. There is a result once one of the two stands for a halted
configuration: `post₁` of the output of M₁ if M₁ has halted, else `post₂` of the output of M₂. 

### `choose`

 M₁ on `pre₁ x` if `test x` is true, else M₂ on `pre₂ x`: `Stepped.ite` of the two simulations
`Wrap.sim`. 

### `start`

 The start configuration of M on the bit string x. 

### `Hosts`

 The machine N carries out the computation X: whenever X ends on x with the result w within T
steps and with all states of size at most S, N puts out w on x within q·(T + 1)·(|x| + S + 1)^q
steps. 

 ### What the machine around the two machines does 

### `Alternates`

 For all bit strings x, y₁, y₂ and all t₁, t₂: if M₁ puts out y₁ on `pre₁ x` within t₁ steps, M₂
puts out y₂ on `pre₂ x` within t₂ steps, and `post₁ y₁ = post₂ y₂`, then N puts out this bit string
on x within q·(min(t₁, t₂) + |x| + 1)^q steps. 

### `Chooses`

 For all bit strings x, y and all t: if `test x` is true and M₁ puts out y on `pre₁ x` within t
steps, then N puts out `post₁ y` on x within q·(t + |x| + 1)^q steps; if `test x` is false and M₂
puts out y on `pre₂ x` within t steps, then N puts out `post₂ y` on x within q·(t + |x| + 1)^q
steps. 

### `EveryTwoMachinesCanBeAlternated`

 Any two machines with finite alphabets can be run in alternation: for all such M₁, M₂ and all
polynomial-time `pre₁`, `pre₂`, `post₁`, `post₂` there are codings K₁, K₂ of their configurations, a
machine N with finite alphabets and numbers q₀, q such that N carries out the computation
`alt K₁ K₂ pre₁ pre₂ post₁ post₂` and `Alternates M₁ M₂ pre₁ pre₂ post₁ post₂ N q` holds. 

### `EveryTwoMachinesCanBeChosenBetween`

 A polynomial-time test on the input can choose between any two machines with finite alphabets:
for all such M₁, M₂, every polynomial-time `test` and all polynomial-time `pre₁`, `pre₂`, `post₁`,
`post₂` there are codings K₁, K₂, a machine N with finite alphabets and numbers q₀, q such that N
carries out the computation `choose K₁ K₂ test pre₁ pre₂ post₁ post₂` and
`Chooses M₁ M₂ test pre₁ pre₂ post₁ post₂ N q` holds. 
