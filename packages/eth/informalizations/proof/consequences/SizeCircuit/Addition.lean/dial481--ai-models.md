---
{
  "module": "proof/consequences/SizeCircuit/Addition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Addition.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Addition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the circuit counts the ones

Facts on `addStep` and `added` of proof/consequences/SizeCircuit/CircuitDefs.lean, for «a circuit
with O(n) gates of two inputs tests whether |S| = s» (proof of Corollary 7).

* `AddGood n st`: all wires named in the state exist, the gates read earlier wires only, and wires
  of the next weight wait only while wires of the present weight do. A step keeps this
  (`addGood_addStep`).
* While a wire waits, a step lowers the number of waiting wires by exactly one; it writes at most 5
  gates and finds at most one digit (`counts_addStep`). So after n steps no wire waits
  (`added_spec`).
* `addValue v st`: under the values v of the wires, the number written by the digits found so far
  plus the waiting wires that are 1, each with its weight. A step keeps it if v obeys the gates
  (`addValue_addStep`). So at the end the digits write the number of inputs that are 1
  (`addValue_added`). 

 ### A step when wires of the present weight wait 

### `addStep_three`

 The step if at least three wires of the present weight wait: a full adder. 

### `addStep_two`

 The step if exactly two wires of the present weight wait: a half adder, and its sum is the next
digit. 

### `addStep_one`

 The step if exactly one wire of the present weight waits: it is the next digit. 

 ### The two adders 

### `fullAdder_spec`

 The sum and twice the carry of a full adder make the number of ones among its three inputs. 

### `halfAdder_spec`

 The sum and twice the carry of a half adder make the number of ones among its two inputs. 

### `wfa_fullAdder`

 The gates of a full adder read earlier wires only. 

### `wfa_halfAdder`

 The gates of a half adder read earlier wires only. 

### `length_fullAdder`

 A full adder has 5 gates. 

### `length_halfAdder`

 A half adder has 2 gates. 

 ### What a step keeps 

### `AddGood`

 All wires named in the state exist, the gates read earlier wires only, and wires of the next
weight wait only while wires of the present weight do. 

### `addGood_addStart`

 The start is good. 

### `addGood_addStep`

 A step keeps a good state good. 

### `counts_addStep`

 While a wire waits, a step lowers the number of waiting wires by exactly one; it writes at most
5 gates and finds at most one digit. 

### `iterate_spec`

 After k ≤ n steps: the state is good, n − k wires wait, at most 5k gates are written and at most
k digits found. 

### `added_spec`

 **After the n steps**: no wire waits; all digit wires exist; the gates read earlier wires only;
there are at most 5n gates and at most n digits. 

 ### The number that is kept 

### `onesAmong`

 The number of wires of the list that are 1 under v. 

### `onesAmong_nil`

 No wire, no one. 

### `onesAmong_cons`

 The number of ones of a list of wires: the first wire and the rest. 

### `addValue`

 The number written by the digits found so far, plus 2^j for each waiting wire of the present
weight 2^j that is 1, plus 2^{j+1} for each waiting wire of the next weight that is 1. 

### `addValue_mk`

 The value of a state given by its four parts. 

### `addValue_push`

 The value after a new digit d has been found and the next weight has become the present one. 

### `addValue_addStep`

 If v obeys the gates after a step, it obeys the gates before it, and the step has kept the
value. 

### `addValue_iterate`

 If v obeys the gates after k steps, the value is still the number of inputs that are 1. 

### `addValue_added`

 **At the end the digits write the number of inputs that are 1**, under all values v of the wires
that obey the gates of the addition. 
