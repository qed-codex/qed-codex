---
{
  "module": "src/Lib/ClassField/HeckeCharacter/SplittingCharacters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/SplittingCharacters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/SplittingCharacters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splitting characters

Here a pair of spaces is indexed by two characters `ν_S`, `ν_T` of `[U(1)]`; one can also use
splitting characters `χ_S`, `χ_T`. The two descriptions agree: `ν ↦ ν.spaceChar k`, the Hecke
character `y ↦ ν(y / ȳ) υ(y)⁻ᵏ` (with `υ` the splitting character from `WeilData`), is a bijection
onto the splitting characters of rank `k` (`HeckeChar.isSplitting_iff`). Here `divStar` is the map
`y ↦ y / ȳ` from the ideles onto the norm-one ideles `unitary (𝔸 E)`. The file also gives the rules
for products, inverses and hyperbolic planes, the character of `[U(1)]` that gives the power of `υ`
by minus the signature of a space, and the splitting characters of a pair with one character.

## Relation to the literature

Known result: splitting characters of a CM extension, described through Hilbert's Theorem 90.
Source: Harris–Kudla–Sweet (1996), §1.


### `HeckeChar.exists_baseChange_eq`

 A Hecke character `ξ` that is trivial on the ideles of the totally real subfield, that is, on
the ideles fixed by conjugation, is a base change from `[U(1)]`: `ξ(y) = ν(y / ȳ)` for a character
`ν` of `[U(1)]`. 

### `HeckeChar.exists_baseChange_iff`

 A Hecke character is a base change from `[U(1)]` if and only if it is trivial on the ideles
fixed by conjugation. 

### `HeckeChar.IsSplitting`

 A splitting character for a space of rank `k`: a Hecke character whose restriction to the ideles
of the totally real subfield (the ideles fixed by conjugation) is that of `υ ^ k`. Classically this
restriction is `η ^ k`, with `η` the quadratic character of the CM extension; here we use only that
the restriction of `υ` has order at most two. 

### `_root_.New.HeckeChar.isSplitting_iff`

 A Hecke character `χ` is a splitting character for rank `k` if and only if
`ν(y / ȳ) = χ(y) υ(y) ^ k` for exactly one character `ν` of `[U(1)]`. 

### `_root_.New.HeckeChar.IsSplitting.autChar`

 The character `ν` of `[U(1)]` with `ν(y / ȳ) = χ(y) υ(y) ^ k`, for a splitting character `χ` of
rank `k`. The Weil representation `ω_{χ_S, χ_T}` is `pairWeil` at these characters for `χ_S` and
`χ_T`. 

### `spaceChar_mul`

 The splitting character of `ν * ν'` at rank `k + l` is the product of those of `ν` at rank `k`
and of `ν'` at rank `l`, as for an orthogonal sum of spaces. 

### `spaceChar_inv_mul_upsilonU1_pow`

 For a character `ν` of `[U(1)]` and `k : ℕ`, `ν.spaceChar k` is the Hecke character
x ↦ `ν (x / x̄) * υ x ^ (-k)` of `E`, where `υ` is the splitting character from `WeilData`.
Replacing `ν` by `ν⁻¹ * upsilonU1 ^ k`, where `upsilonU1` is the restriction of `υ` to the norm-one
ideles, inverts this rank-`k` Hecke character. 

### `spaceChar_add_two_mul`

 Adding `l` hyperbolic planes, that is, raising the rank by `2 * l`, keeps the splitting
character if `ν` is multiplied by `upsilonU1 ^ l`. Here `ν.spaceChar k` is the Hecke character
`x ↦ ν (x / x̄) * υ x ^ (-k)` of `E`, where `υ` is the splitting character of the Weil data.
`upsilonU1` is the restriction of `υ` to the norm-one ideles. 

### `spaceChar_stdChar`

 For signs `s : n → ℤˣ` of a space of rank `card n`, with `n₊ = negCount (-s)` signs `1` and
`n₋ = negCount s` signs `-1`, consider the standard character `stdChar s = upsilonU1 ^ n₋`, where
`upsilonU1` is the restriction to `U(1)` of the splitting character `υ` from `WeilData`. Its
rank-`card n` Hecke character `spaceChar` (x ↦ `stdChar s (x / x̄) * υ x ^ (-card n)`) is
`υ ^ (-(n₊ - n₋))`, the power of `υ` by minus the signature. 

### `spaceChar_rankTwist_eq_ite`

 Let `E` be a CM field with Weil data, whose splitting character is `υ`. For a character `ν` of
`[U(1)]` and a finite type `n`, let `rankTwist ν n = ν · υ^⌊card n / 2⌋` (with `υ` restricted to
norm-one ideles). Its space character at rank `card n`, the Hecke character
`x ↦ (rankTwist ν n)(x / x̄) · υ(x)^(-card n)`, equals `ν.baseChange` if `card n` is even and
`ν.baseChange * υ⁻¹` if `card n` is odd. 

### `inv_spaceChar_rankTwist_inv`

 Let `E` be a CM field with Weil data, whose splitting character is `υ`. For a character `ν` of
`[U(1)]` and a finite type `n`, let `rankTwist ν⁻¹ n = ν⁻¹ · υ^⌊card n / 2⌋` (with `υ` restricted to
norm-one ideles). Its space character at rank `card n` is the Hecke character
`x ↦ (rankTwist ν⁻¹ n)(x / x̄) · υ(x)^(-card n)`. The inverse of that character equals
`ν.baseChange` if `card n` is even and `ν.baseChange * υ` if `card n` is odd. 
