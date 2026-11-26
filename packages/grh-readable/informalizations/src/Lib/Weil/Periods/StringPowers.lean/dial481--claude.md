---
{
  "module": "src/Lib/Weil/Periods/StringPowers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/StringPowers.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/StringPowers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The string of a graded space as the powers `𝔢 ^ i`

The orthogonal complement of `X` in a graded space with a string of `s` vectors behaves like
`E[𝔢] / (𝔢 ^ s)`: the vector called `𝔢 ^ i` is `New.Grading.stringPower`, a multiple of the string
vector with number `i`. That vector has grade `s - 1 - 2 * i`.

* `New.Grading.shift_mulVec_stringPower`: `New.Grading.shift` is the multiplication by `𝔢`.
* `New.Grading.form_stringPower`: `𝔢 ^ i` and `𝔢 ^ l` pair to `-N` if `i + l = s - 1`, else to `0`.
* `New.Grading.middlePower`, `New.Grading.form_middlePower`: for odd `s` the power of `𝔢` of
  grade `0` is the vector `z_N`, of norm `-N`.
* `New.Grading.stringMap_mulVec_stringPower`: the map `New.Grading.stringMap` between neighbouring
  spaces is the projection `E[𝔢] / (𝔢 ^ s) → E[𝔢] / (𝔢 ^ (s - 1))`.
* `New.Grading.exists_stringSum_eq`, `New.Grading.stringMapFin_stringSum`: over the finite adeles
  the `𝔢 ^ i` span the complement of `X` (the vectors fixed by the projection
  `New.Grading.stringProj` to the span of the string vectors), and `New.Grading.stringMapFin`
  keeps the coordinates in `𝔢 ^ i` for `i < s - 1`.

Notions from other files:
* `New.Space E ι ε`: a hermitian matrix `V.J` over `E`, indexed by `ι`, with an adelic point;
* `New.Grading V N X s`: an identification `X ⊕ Fin s ≃ ι` under which string vector `i` pairs only
  with string vector `s - 1 - i`, to `1` (to `-N` in the middle), a constant `c = star c ≠ 0`, and
  the fact `N = star N ≠ 0`;
* `New.Grading.shift`: the matrix, with entries in `E` seen as adeles by the diagonal embedding
  `toAdele`, that kills `X` and the last string vector and raises the number of any other string
  vector by one, up to a factor;
* `New.Grading.stringMap`, `New.Grading.stringMapFin`: the map that kills `X` and the string vector
  `s - 1` and keeps the number of any other string vector, up to a factor, and its part at the
  finite adeles;


### `powerCoeff`

 The coefficient of `𝔢 ^ i` at the string vector `i`: a power of the constant `c` of the grading,
times `-N` if that vector has negative grade, that is if `s ≤ 2 * i`. 

### `stringPower`

 The vector `𝔢 ^ i` of the complement `E[𝔢] / (𝔢 ^ s)` of `X`: the multiple `Y.powerCoeff i` of
the string vector `i`, and `0` for `s ≤ i`. 

### `powerCoeff_of_lt`

 For a grading `Y` whose string has length `s`, the vector `𝔢 ^ i` is `Y.powerCoeff i` times the
`i`-th string vector. If that vector has nonnegative grade `s − 1 − 2i` (`2 * i < s`), this
coefficient is `c ^ n` for `n = i - s / 2`, where `c` is the constant `Y.genericConst`. 

### `powerCoeff_of_le`

 In negative grade (`s ≤ 2 * i`) the coefficient of `𝔢 ^ i` is `-N * c ^ n` for
`n = i - (s - 1) / 2`. 

### `powerCoeff_ne_zero`

 The coefficient `Y.powerCoeff i` of `𝔢 ^ i` is nonzero, as `c` and `N` are. 

### `stringPower_eq_single`

 For `i < s` the vector `𝔢 ^ i` is supported at the string index `i`. 

### `shift_factor_mul_powerCoeff`

 The factor by which `Y.shift` takes the string vector `i` to the next one (the `if` below,
times `c`), times the coefficient `Y.powerCoeff i` of `𝔢 ^ i`, is the coefficient of
`𝔢 ^ (i + 1)`. 

### `shift_mulVec_stringPower`

 For a grading `Y` of `V` as `X` plus a string of length `s`, write `𝔢 ^ i` for
`Y.stringPower i`: the vector of the complement `E[𝔢] / (𝔢 ^ s)` of `X` that is a fixed multiple of
the `i`-th string vector, and `0` for `s ≤ i`. The matrix `Y.shift`, which kills `X` and acts on
this complement as multiplication by `𝔢`, sends `𝔢 ^ i` (seen over the adeles by the diagonal
embedding `toAdele`) to `𝔢 ^ (i + 1)`, for every `i < s`. For `i + 1 = s` the image is `0`. 

### `form_stringPower`

 The vectors `𝔢 ^ i` and `𝔢 ^ l`, that is `Y.stringPower i` and `Y.stringPower l`, pair under
the hermitian form `V.J` to `-N` if `i + l = s - 1`, and to `0` otherwise. 

### `middlePower`

 The vector `z_N`: for a string of odd length `s = 2 * n + 1` it is the power `𝔢 ^ n`, the one
of grade `0`. 

### `middlePower_eq_single`

 For a string of odd length `s = 2 * n + 1`, the vector `z_N` is the string vector with number
`n`. 

### `middlePower_apply_eq_zero`

 For a grading `Y` of `V` as `X ⊕ J_s` whose string has odd length `s = 2 * n + 1`, consider the
vector `z_N = 𝔢 ^ n` (`Y.middlePower`, a multiple of the middle string vector). It has grade `0`:
its entry vanishes at every basis index `k` of nonzero grade `Y.gradeOf k`. The grade is `0` on `X`
and `s − 1 − 2i` on the `i`-th string vector. 

### `form_middlePower`

 For a grading `Y` of `V` as `X ⊕ J_s` whose string has odd length `s = 2 * n + 1`, the vector
`z_N = 𝔢 ^ n` (`Y.middlePower`, the multiple of the middle string vector of grade `0`) has norm `-N`
under the hermitian form `V.J`. 

### `stringMap_factor_mul_powerCoeff`

 For gradings `Y` and `Y'` of string lengths `s` and `s - 1` with the same constant `c`, the
factor of `Y.stringMap Y'` at the string vector `i` (the two `if`s below) times the coefficient of
`𝔢 ^ i` in `Y` is its coefficient in `Y'`. 

### `stringMap_mulVec_stringPower`

 Let `Y'` be a grading of a second space `V'` with the same `N` and string length `s - 1`. Assume
`Y'` carries the same constant `c` as `Y`, where `c = c̄ ≠ 0` is the element of `E` that each
grading carries for the generic character. Then for `i < s` the matrix `Y.stringMap Y'` sends
`Y.stringPower i` (the vector `𝔢 ^ i` of `V`, seen over the adeles by the diagonal embedding
`toAdele`) to `Y'.stringPower i` (the vector `𝔢 ^ i` of `V'`), which is `0` for `i = s - 1`. 

### `stringSum`

 The vector `∑ i < s, t i • 𝔢 ^ i` over the finite adeles, with coefficients `t`. 

### `stringSum_apply_inr`

 At the string index `b` the sum `∑ t i • 𝔢 ^ i` has the entry `Y.powerCoeff b * t b`. 

### `exists_stringSum_eq`

 The vectors `𝔢 ^ i` span the complement of `X` over the finite adeles: a vector `y` fixed by
the projection `Y.stringProj` to the span of the string is a sum `∑ t i • 𝔢 ^ i`. 

### `stringMapFin_stringPower`

 For gradings with the same constant `c`, the map `Y.stringMapFin Y'`, the finite part of
`Y.stringMap Y'`, sends `𝔢 ^ i` to `𝔢 ^ i`. 

### `stringMapFin_stringSum`

 For gradings `Y` and `Y'` of string lengths `s` and `s - 1` with the same constant `c`, the map
`Y.stringMapFin Y'`, the finite part of `Y.stringMap Y'`, acts on the sums `∑ t i • 𝔢 ^ i` as the
projection `E[𝔢] / (𝔢 ^ s) → E[𝔢] / (𝔢 ^ (s - 1))`: it keeps `t i` for `i < s - 1`. 
