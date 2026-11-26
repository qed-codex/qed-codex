---
{
  "module": "proof/rates/CountedRecursion/EndPlugged.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndPlugged.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndPlugged.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (b) with the pieces computed by their algorithm

`recursionPluggedFrom : RecursionPluggedFrom`. The run of `RecursionCountedUpTo` has the price 1 for
a query to the tables. Raise it to 3 = 1 + 2 (`PricesScale`: no price grows more than three times,
so the cost is at most three times as large); then the queries to the pieces are answered by running
the algorithm and a query to the tables is passed on (`PiecesCounted.OracleFromAlgorithm`). The
states grow by the room of the algorithm at Λ and by the size of a query to the tables with its
answer, which is within the bound on the sizes (`tableQuery_le`); hence the constant C₀ + 1. 

### `recursionPluggedFrom`

 **Theorem A (b) with the pieces computed by their algorithm**, from the form with the priced
oracle. 
