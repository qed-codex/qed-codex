---
{
  "module": "proof/variables/VariableBound/Count/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Count/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Count/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One sparse formula counted as in Steps 1 to 4 of Appendix D: the certificate

Proves `VariableBound.StCertCountD`: the program `countD` is polynomial-time (`PolyT`) in the pad,
jointly in the width k, the index of the clique solver, n and Δ (k, n, Δ in unary) and the formula,
for a polynomial-time clique solver (`S.Poly`), given the certificates of
its parts: one evaluation by networks (`Net.StCertEvD`), the search (`StCertSearchD`), the listed
family of Lemma 13 (`Fld.StCertFamD`) and the parameters (`StCertParam`). The proof is a
composition. Two
closure lemmas come first: the remainder of an integer modulo a power of two, and the logarithm of a
number given in unary; they are copies of lemmas of
proof/rates/ClauseBound/ParityChecks/CertLib.lean. 

 ### Two closure lemmas 

### `emod_natCast`

 The remainder of an integer modulo a natural number, by cases on the sign. 

### `modZ_polyT`

 The remainder of an integer modulo a natural number is polynomial-time. 

### `mod_two_pow_polyT`

 The remainder of an integer modulo a power of 2 is polynomial-time, for the exponent in unary. 

### `log_unary`

 ⌊log₂ n⌋ is given in unary if n is. 

 ### The program 

### `evX_polyT`

 The program for X(𝓛) is polynomial-time, given the certificate of one evaluation and a
polynomial-time solver; k, n, Δ, β in unary. 

### `evF_polyT`

 The program for F(𝓛) is polynomial-time, given the certificate of one evaluation and a
polynomial-time solver; k, n, Δ in unary. 

### `countD_polyT`

 The count is polynomial-time, given the four certificates and a polynomial-time solver; k, n, Δ
in unary. 

### `stCertCountD`

 Steps 1 to 4 of Appendix D: for every polynomial-time clique solver, the count of one sparse
formula is polynomial-time, jointly in its input, given the certificates of one evaluation by
networks (`Net.StCertEvD`), of the search
(`StCertSearchD`), of the listed family of Lemma 13 (`Fld.StCertFamD`) and of the parameters
(`StCertParam`). 
