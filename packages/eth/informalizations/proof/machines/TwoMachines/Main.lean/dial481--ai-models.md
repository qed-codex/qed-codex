---
{
  "module": "proof/machines/TwoMachines/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/TwoMachines/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/TwoMachines/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two machines in alternation, and a choice between two machines: the proofs

`alt_runs`: let h be the first time at which one of the two machines has halted; up to h the
alternation advances both, at h it has a result, and h is at most the smaller of the two numbers of
steps.
`alt_isPolyT`: its three parts are polynomial-time. `CountKSat.exists_tmW` carries the computation
out; `exists_bound₂` does the arithmetic. The choice is `Stepped.ite` of two simulations `Wrap.sim`;
its runs come from `Stepped.branch_runs_inl` and `Stepped.branch_runs_inr`, its polynomial time from
`IsPolyT.ite`. 

 ### The alternation 

### `alt_out_running`

 As long as neither machine has halted the alternation has no result. 

### `alt_step_rep`

 One step of the alternation advances both configurations. 

### `alt_init`

 The alternation starts with the pair of the start configurations. 

### `exists_halt`

 A run of M on x with output y within t steps: after some n ≤ t steps of the step that stays, M
is in the halted configuration with y on its output stack. 

### `eq_of_halted`

 If M is halted after i steps and reaches the halted configuration c after n steps, it is in c
after i steps already. 

### `out_haltList`

 What a coding reads from the halted configuration with y on the output stack. 

### `size_rep_le`

 The size of the value for the configuration after i steps. 

### `alt_runs`

 If M₁ puts out y₁ on `pre₁ x` within t₁ steps, M₂ puts out y₂ on `pre₂ x` within t₂ steps and
the two results agree, the alternation ends on x with that result within min(t₁, t₂) steps, on
states of size linear in |pre₁ x| + |pre₂ x| + min(t₁, t₂). 

### `alt_isPolyT`

 The three parts of the alternation are polynomial-time if the four functions are. 

### `exists_bound₂`

 The numbers: for all q₀, a₁, a₂, c₁, c₂ there is a q such that q₀·(t + 1)·(n + ((a₁·(p₁ + 1) +
a₁·t) + (a₂·(p₂ + 1) + a₂·t)) + 1)^q₀ ≤ q·(t + n + 1)^q whenever p₁ ≤ c₁·(3n + 3)^c₁ and p₂ ≤ c₂·(3n + 3)^c₂. 

### `exists_length_le`

 The length of the value of a polynomial-time function on bit strings. 

### `everyTwoMachinesCanBeAlternated`

 Any two machines with finite alphabets can be run in alternation. 

 ### The choice 

### `everyTwoMachinesCanBeChosenBetween`

 A polynomial-time test on the input can choose between any two machines with finite alphabets. 
