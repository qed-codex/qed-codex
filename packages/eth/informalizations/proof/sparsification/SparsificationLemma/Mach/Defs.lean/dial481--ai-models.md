---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A machine that prints the outputs of the sparsification: definitions and statements

`SparsABCD` below states sparsification with parts (a) to (d), a form that the paper does not state;
its part (d) is the running time, and `Prints` is that part in the parameters of the machine. Lemma
4 says «one can compute, in time 2^(εn) times a polynomial in n, …».
It is ONE machine for all widths k and all precisions.
On the side of the input, «k-CNF» is `SatK.IsKCNF` (at most k literals in every clause, no clause
written twice) without an empty clause; on the side of the output it is `SparsificationLemma.IsKCNF`
together with `List.Nodup`.
**The input** is 1^s 0 1^k 0 followed by the code of the formula (`encIn`): the precision s and the
width k in unary. The machine runs the sparsification procedure of Appendix C (Calabro's algorithm
as changed there), with the thresholds `thetaU τ` for τ = 2^(4s+17), so 2^(−s) has the role of ε.
**The output** is the list of the formulas, written by the code `code`.
**The time** is at most C·(length of the input + 2^k)^C·2^(C·⌊n/2^s⌋) for one constant C (`Prints`).
In the machine built here, with the tools of this development, every round of the walk through the
tree rewrites the whole state, which holds the formulas found so far. So the
exponent of 2^(n/2^s) is C and not 1. To get time 2^(εn) one gives the machine a precision s with C
≤ ε·2^s. The theorems of this development that turn a function into a machine give C only after the
machine is fixed, and only as «there is a C»; so we do not build a machine that computes such an s
from ε, and the input has s and not ε. This is a limit of the tools used here, not of the
mathematics.
`SparsABCD` is the form with parts (a) to (d), with s = `precE C k ε`; the price is an absolute
constant in part (c): at most (Ck/ε)^(16k) occurrences of a variable.
`LemSparsification` is the case k = 3 in the words of the paper.
This file has definitions only. The statements are propositions; they are proved in other files. 

 ### Input and output as words 

### `encIn`

 The input word: 1^s 0, then 1^k 0 and the code of φ as in `SatM.enc`. 

### `codeNat`

 A number in unary: 1^v 0. 

### `codeLit`

 A literal: one bit, true for xᵢ and false for ¬xᵢ, then i in unary. 

### `codeCl`

 A clause: 1 before every literal, 0 at the end. 

### `codeFml`

 A formula: 1 before every clause, 0 at the end. 

### `code`

 A list of formulas: 1 before every formula, 0 at the end. 

 ### The machine 

### `Prints`

 **Part (d), in the parameters of the machine.** One machine and one constant C: for all k ≥ 1,
all s ≥ `s0U k`, all n and every k-CNF φ on n variables without an empty clause, the machine,
started on 1^s 0 1^k 0 code(φ), halts with
the code of the list of outputs for τ = 2^(4s+17) within C·(length of the input +
2^k)^C·2^(C·⌊n/2^s⌋) steps. 

### `precE`

 The precision for width k and ε, given the constant C of the machine: the least s ≥ `s0U k` with
C/ε ≤ 2^s. 

### `SparsABCD`

 **Sparsification, parts (a) to (d), on a Turing machine.** One machine and one constant C: for
all k ≥ 1, n, rational ε ∈ (0,1] and k-CNF φ on n variables with no empty clause, let s =
`precE C k ε`.
The machine, started on 1^s 0 1^k 0 code(φ), halts with the code of a list Φ of k-CNFs on the same
variables, none with a clause written twice, such that (a) Φ has at most 2^(εn) members; (b) every
assignment that satisfies φ satisfies
exactly one of them, and every other assignment none; (c) in each of them every variable occurs in
at most (Ck/ε)^(16k) clauses; (d) the number of steps is at most C·(length of the input +
2^k)^C·2^(εn).
This form is not in the paper. The machine gets not ε but the precision s, which depends on C; as
only «a C exists» is stated, it does not say how to run it for a given ε (`Prints` is the form with
s
as a free input). In (c) the bound is (Ck/ε)^(16k), where Step 5 of Appendix D has 2·(8k/ε)^(3k) +
2; in (d) it is the product above, where Step 5 has time 2^(εn)·n^(O(k)). 

### `LemSparsification`

 **Lemma 4 (Sparsification Lemma, for clauses of at most 3 literals).** For every ε > 0 there is
a constant M(ε) ≥ 1 such that for every 3-CNF φ on n variables one can compute, in time 2^(εn) times
a polynomial in n, at most 2^(εn) 3-CNFs
on the same variables, each with at most M(ε)·n clauses, such that φ is satisfiable if and only if
at least one of them is.
«One can compute»: there is one machine for all ε; for a given ε it is started on the constant word
1^s 0 1^3 0, s = s(ε), followed by the code of φ. A 3-CNF has nonempty clauses of at most 3
literals, and no clause is written twice (in an output, a clause may list a literal twice, and two
clauses may list the same literals in different orders; neither makes the statement weaker). The
polynomial c·(n+1)^c may depend on ε. 
