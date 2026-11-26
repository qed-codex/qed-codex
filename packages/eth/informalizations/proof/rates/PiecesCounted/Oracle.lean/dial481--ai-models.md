---
{
  "module": "proof/rates/PiecesCounted/Oracle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Oracle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/Oracle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the oracle to the algorithm

A machine that asks the pieces at the prices `price c` stays within its cost when each of these
queries is answered by running the algorithm of the last clause of Definition 7(c). This is the
substitution rule for query machines (`QueryMachines.stSubstWithin`) with the answering machine
`passOrRun Alg`:
a query of the first kind is asked again (no own step, cost w x); a query to the pieces is answered
by running Alg (at most 2^{cλ} own steps, no query). In both cases the substitution rule charges two
more, and these are in the prices of the hypothesis. 

### `passOrRun_pass`

 The answering machine on a query of the first kind: it asks the query again and hands the answer
back. 

### `passOrRun_run`

 The answering machine on a query to the pieces: it runs the algorithm. 

### `oracleFromAlgorithm`

 Proof of `OracleFromAlgorithm`: the substitution `stSubstWithin` puts the answering machine
`passOrRun Alg` in place of the oracle, and each answer stays within its price. 
