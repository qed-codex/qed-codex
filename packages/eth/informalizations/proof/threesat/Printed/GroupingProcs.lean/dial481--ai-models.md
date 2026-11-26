---
{
  "module": "proof/threesat/Printed/GroupingProcs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingProcs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingProcs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 for networks given by procedures

A machine for networks (`Printed.NetMachine`) asks the queries of Definition 2(iii) and is charged τ
operations for each. Here the queries are answered by the four procedures of `SecNetworks.Procs`,
step machines that take at most τ steps each (`SecNetworks.IsNetwork`).
* `map_range_eq_ofFn`, `inputOf_eq`: the input written down from the numbers that the procedures
  give is the input that belongs to the network;
* `answerOf_runs`: the four procedures as one machine answer every query that `netOracle` answers,
  within τ steps;
* `stOnProcedures`: so a machine that does what Lemma 1 says outputs the value within three times
  the bound of Lemma 1 (a query costs τ + 2 ≤ 3τ steps: `QueryMachines.stPlug`). 

### `map_range_eq_ofFn`

 A list written with `List.range` and the same list written with `List.ofFn`. 

### `inputOf_eq`

 The input written down from numbers that agree with those of the network N is the input that
belongs to N. 

### `answerOf_runs`

 The four procedures, as one machine, answer every query of Definition 2(iii) that `netOracle`
answers, within τ steps. 

### `stOnProcedures`

 **Lemma 1 for networks given by procedures.** 
