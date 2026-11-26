---
{
  "module": "ThreeSumApsp/Lang/Calls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Calls.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Calls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Calls

Meets lim P p d vals μ T R is the specification of a procedure: procedure number p of the program P,
run at depth d on the arguments vals in the memory μ, ends within T steps with a result and a memory
that satisfy R. A routine is proved to meet such a specification (Meets.of_body), and a caller uses
the specification only, so that the proof of a caller does not depend on the body of a callee.

The specification of a routine x, as its callers assume it, has the form
`∀ (data) μ, hypotheses → ∀ d, d + k ≤ lim.depth → Meets lim P p d vals μ T R`.  Here k is the
number of levels of calls that x needs below itself, and d, the depth at which the body of x runs,
comes last.

There is one rule for calls, in four forms.  It is told the fact about the callee, from which it
reads the values of the arguments, the time and what holds afterwards, and it asks for what follows
the call.  Three side goals have default proofs: the arguments are safe and have these values, one
more level of calls is allowed, and the time suffices.  Ends.callTo and Ends.callToThen are the rule
for a state ⟨frame l, μ⟩; Ends.callLast and Ends.callThen are the same for local variables that are
not given as a list.


 ## Specifications of procedures 

### `Meets`

 Procedure number p of the program P, run at depth d on the arguments vals in the memory μ, ends
within T steps with a result r and a memory μ' that satisfy R r μ'. 

### `Meets.of_body`

 From a theorem about a body to the specification. 

### `Meets.mono`

 More time and a weaker conclusion. 

### `Meets.mono_time`

 A specification holds with every larger bound on the time. 

### `Meets.mono_const`

 A specification whose time is a constant times a shape holds for every larger constant. 

### `Meets.append`

 A specification holds for the program with more procedures appended. 

 ## The rule for calls 

### `Ends.callLast`

 `x := p(args)`, where the arguments give vals.  The procedure runs at depth d + 1. 

### `Ends.callThen`

 `x := p(args) ; s`.  The rest s of the text gets the steps that are left. 

### `Ends.callTo`

 `x := p(args)`, with the local variables as a list.  The procedure runs at depth d + 1. 

### `Ends.callToThen`

 `x := p(args) ; s`, with the local variables as a list.  The procedure runs at depth d + 1. 
