---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Parameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Parameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Parameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The parameters of Theorems 17 and 19 in integer arithmetic

The proof of Theorem 19 chooses `D` and `g` as rounded real powers of `n`: "Let D be the largest
power of four with D ≤ n^{1/18}, […] and let g := ⌈D^{1/36}⌉" on the route through Theorem 5, and
"Let D := ⌊n^{1/18}⌋ and g := ⌈D^{0.0315}⌉" on the route through Corollary 26.  The reduction of
Theorem 17 cuts each residue class into chunks of at most `n²/√D` query pairs and splits `C` into
pieces of at most `⌈s/g⌉` vertices, where `s = ⌊√D⌋`.  A program finds all these numbers by
operations on natural numbers.

* `rootFloor e t` is `⌊t^{1/e}⌋` and `rootCeil e t` is `⌈t^{1/e}⌉` (`floor_rpow_inv`,
  `ceil_rpow_inv`); they are characterised by `x ≤ rootFloor e t ↔ x^e ≤ t` (`le_rootFloor_iff`) and
  `rootCeil e t ≤ g ↔ t ≤ g^e` (`rootCeil_le_iff`).
* The four functions `paramD₅Nat`, `paramG₅Nat`, `paramD₂₆Nat`, `paramG₂₆Nat` are the parameters
  of the proof of Theorem 19 (`paramD₅Nat_eq`, `paramG₅Nat_eq`, `paramD₂₆Nat_eq`, `paramG₂₆Nat_eq`);
  they are at least 1 and at most `n` or `D` (`paramD₂₆Nat_le`, `paramG₅Nat_le`, `paramG₂₆Nat_le`).
* The sizes of the proof of Theorem 17: `⌊n²/√D⌋ = ⌊√(n⁴/D)⌋` (`queryCapNat_eq`), `s` is the integer
  square root (`sOf_eq_sqrt`), and the rounded quotients are `a ⌈/⌉ b` (`pieceSizeNat_eq`,
  `numPiecesNat_eq`, `numChunks_eq`).  The middle part `C_k × ℤ_p` of an instance has at most `D`
  vertices (`pieceSize_mul_le`).


 ## Roots, rounded down and up 

### `rootFloor`

 The greatest `x ≤ t` with `x^e ≤ t`: `⌊t^{1/e}⌋` for `e ≥ 1`. 

### `rootCeil`

 The least `g` with `g^e ≥ t`, for `t ≥ 1` and `e ≥ 1`: `⌈t^{1/e}⌉`. 

### `rootFloor_pow_le`

 The power of `rootFloor e t` does not exceed `t`. 

### `le_rootFloor`

 `rootFloor e t` is the greatest `x` with `x^e ≤ t`. 

### `le_rootFloor_iff`

 The characterisation of `rootFloor` by which a program finds it. 

### `floor_rpow_inv`

 `rootFloor e t` is `⌊t^{1/e}⌋`. 

### `le_rootCeil_pow`

 The power of `rootCeil e t` reaches `t`. 

### `rootCeil_le`

 `rootCeil e t` is the least `g` with `t ≤ g^e`, for `t ≥ 1`. 

### `rootCeil_le_iff`

 The characterisation of `rootCeil` by which a program finds it. 

### `ceil_rpow_inv`

 `rootCeil e t` is `⌈t^{1/e}⌉`, for `t ≥ 1`. 

 ## The parameters of the proof of Theorem 19 

### `paramD₅Nat`

 "Let D be the largest power of four with D ≤ n^{1/18}". 

### `paramG₅Nat`

 "and let g := ⌈D^{1/36}⌉". 

### `paramD₂₆Nat`

 "Let D := ⌊n^{1/18}⌋". 

### `paramG₂₆Nat`

 "and g := ⌈D^{0.0315}⌉": the least `g` with `g^2000 ≥ D^63`. 

### `floor_rpow_one_div`

 `⌊n^{1/18}⌋`, with the exponent as the paper writes it. 

### `paramD₂₆Nat_eq`

 "Let D := ⌊n^{1/18}⌋". 

### `paramD₂₆Nat_le`

 `⌊n^{1/18}⌋ ≤ n`. 

### `one_le_paramD₂₆Nat`

 `⌊n^{1/18}⌋ ≥ 1` for `n ≥ 1`. 

### `findGreatest_four_pow`

 The greatest `k` with `(4^k)^18 ≤ n` is `⌊log₄ ⌊n^{1/18}⌋⌋`. 

### `paramD₅Nat_eq`

 "Let D be the largest power of four with D ≤ n^{1/18}". 

### `one_le_paramD₅Nat`

 A power of four is at least 1. 

### `paramD₅Nat_le_paramD₂₆Nat`

 The largest power of four below `n^{1/18}` is at most `⌊n^{1/18}⌋`. 

### `paramG₅Nat_eq`

 "and let g := ⌈D^{1/36}⌉". 

### `paramG₂₆Nat_eq`

 "and g := ⌈D^{0.0315}⌉". 

### `paramG₅Nat_le`

 `⌈D^{1/36}⌉ ≤ D`. 

### `paramG₂₆Nat_le`

 `⌈D^{0.0315}⌉ ≤ D`. 

 ## The sizes of the instances of the proof of Theorem 17 

### `queryCapNat`

 `⌊n²/√D⌋`, the largest number of query pairs of an instance. 

### `pieceSizeNat`

 The number of vertices `⌈s/g⌉` of a piece of `C`, with `s = ⌊√D⌋`. 

### `numPiecesNat`

 The number of pieces. 

### `queryCapNat_eq`

 `queryCapNat n D` is `⌊n²/√D⌋`: both are the greatest `c` with `c² D ≤ n⁴`. 

### `queryCapNat_succ_le_iff`

 The test by which a program finds `queryCapNat n D`: `c + 1 ≤ ⌊n²/√D⌋` if and only if
`(c + 1)² D ≤ n⁴`. 

### `queryCapNat_succ_sq_mul_le`

 The largest number that this test forms. 

### `sOf_eq_sqrt`

 `s = ⌊√D⌋` is the integer square root. 

### `pieceSizeNat_eq`

 `pieceSizeNat D g` is the number `⌈s/g⌉` of vertices of a piece, where `s = ⌊√D⌋`. 

### `numPiecesNat_eq`

 `numPiecesNat n D g` is the number of pieces. 

### `numChunks_eq`

 The number of chunks of a set of pairs in integer arithmetic. 

### `pieceSize_mul_le`

 A piece has at least one vertex, and the middle part `C_k × ℤ_p` of an instance has at most `D`
vertices. 
