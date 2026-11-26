---
{
  "module": "src/Lib/Analytic/PolyaVinogradov.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PolyaVinogradov.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PolyaVinogradov.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gauss sums of primitive characters and the Pólya–Vinogradov bound

The Gauss sum of a primitive Dirichlet character mod `q` has absolute value `√q`. For a
non-principal character mod `q`, every partial sum of its values is at most `2 √q (1 + log q)` in
absolute value.

* `New.norm_gaussSum_of_isPrimitive`: the modulus of the Gauss sum.
* `New.polya_vinogradov`: the Pólya–Vinogradov inequality.

## Relation to the literature

Known result: the Pólya–Vinogradov inequality for sums of a non-principal Dirichlet character. It is
proved here for initial intervals only, with the explicit bound `2 √q (1 + log q)`. The case of a
general character is reduced to the primitive character that induces it by a Möbius sieve. Source:
Pólya 1918, Vinogradov 1918; Davenport, Multiplicative Number Theory; Montgomery–Vaughan Thm 9.18.


### `norm_gaussSum_of_isPrimitive`

 The Gauss sum of a primitive Dirichlet character mod `q`, taken with the standard additive
character `x ↦ exp (2 π i x / q)` of `ZMod q`, has absolute value `√q`. 

### `four_mul_le_norm_stdAddChar_sub_one`

 The chord from `1` to the root of unity `stdAddChar k = exp (2 π i x)`, where `x = k / q` lies
in `[0, 1]`, has length at least `4 x (1 - x)`. 

### `norm_sum_stdAddChar_pow_le`

 For `k ≠ 0` in `ZMod q`, the sum of the powers `1, …, X` of the root of unity
`stdAddChar k = exp (2 π i k / q)` has absolute value at most `q / 2 · (1 / k + 1 / (q - k))`,
where `k` is read as its representative `k.val` in `[1, q - 1]`. 

### `norm_sum_le_of_isPrimitive`

 The Pólya–Vinogradov inequality for a primitive Dirichlet character `χ` of modulus `q ≠ 1`:
`|∑_{1 ≤ v ≤ X} χ v| ≤ √q (1 + log q)` for all `X`. 

### `card_divisors_le_two_mul_sqrt`

 A natural number `r` has at most `2 √r` divisors. 

### `apply_eq_sum_moebius_smul_of_changeLevel_eq`

 Möbius sieve: if `χ` mod `q = M * r` is induced by `ψ` mod `M`, then `χ v` is the sum of
`μ d • ψ v` over the common divisors `d` of `v` and `r`. 

### `filter_dvd_Ioc_eq_image_mul`

 The multiples of `d > 0` in `[1, X]` are the numbers `d * e` with `1 ≤ e ≤ X / d`. 

### `sum_eq_sum_divisors_of_changeLevel_eq`

 If `χ` mod `q = M * r` is induced by `ψ` mod `M`, then a partial sum of `χ` is a combination of
partial sums of `ψ`, indexed by the divisors `d` of `r`, with coefficients `μ d * ψ d`. 

### `polya_vinogradov`

 The **Pólya–Vinogradov inequality** for initial intervals: for a non-principal Dirichlet
character `χ` mod `q` one has `|∑_{1 ≤ v ≤ X} χ v| ≤ 2 √q (1 + log q)` for all `X`. 
