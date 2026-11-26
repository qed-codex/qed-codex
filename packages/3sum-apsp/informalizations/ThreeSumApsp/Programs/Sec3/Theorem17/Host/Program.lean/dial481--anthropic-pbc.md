---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Program.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Program.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Program.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the program, assembled

The procedures of the host are appended to a program `P₀` that already holds a solver of
Lop-AE-SparseTri and the two procedures that compute the parameters `D` and `g`.  This file has the
list of the procedures (`et17Procs`), their numbers (`et17NumsAt`), the proof that the program so
obtained is the context that the top procedure assumes (`et17Ctx_assembled`), and the
result: the host solves Exact Triangle (`et17_solves`).


### `strNumsAt`

 The numbers of the procedures of Strassen's algorithm, if the list of the procedures of the host
starts at the number `o`. 

### `cpNumsAt`

 The numbers of the procedures that countPrime calls. 

### `chNumsAt`

 The numbers of the procedures that choosePrime calls. 

### `et17NumsAt`

 The numbers of the procedures that the top procedure calls: `pS` is the solver, `pD` and `pG`
compute the parameters. 

### `et17Procs`

 The procedures of the host: procedure number `i` of this list gets the number `o + i`.  The top
procedure has the number `o + 27`; behind it stands the sieve of Eratosthenes, which `primes`
calls. 

### `et17Ctx_assembled`

 **The context of the top procedure**, in the assembled program with anything appended to
it. 

### `et17_solves`

 **The host of Theorem 17 as a solver of Exact Triangle**: from a solver of Lop-AE-SparseTri and
two procedures that compute the parameters, in one program `P₀`, the appended procedures make a
solver of Exact Triangle with the time `hostTime` and the need `hostNeed`. 
