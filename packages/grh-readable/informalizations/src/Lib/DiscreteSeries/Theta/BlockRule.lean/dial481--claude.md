---
{
  "module": "src/Lib/DiscreteSeries/Theta/BlockRule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/BlockRule.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/BlockRule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The block rule for corresponding parameters

The block rule compares two discrete series parameters at one place through their shifted entries.
This file proves that it is equivalent to matching for the oscillator pair, that it is kept by a
swap, a negation and a shift, and gives its form for a pair with one character. In the code all
entries are doubled, so that they are integers.

Notions from other files:
* `HCParam s`: an integer vector l = 2λ indexed by the domain of the signs s; `toHCParam s l` is l
  read as such a vector.
* `HasGap h`: the entries of l are distinct, of the parity of n − 1 for n entries, and those of
  opposite signs differ by at least 2h.
* `FockDualPair.std t s γ δ`: the oscillator pair with rows for the signs t, columns for the signs
  s, row shift γ and column shift δ + n' for n' rows (the constants added on the diagonal).
* `IsMatch`: both parameters have gap 500(n+n')³ and each row and each column is either matched,
  with a sign condition, or lies in the central range left by the difference of the ranks.
* `centredParam`: the entry of a row less twice the row shift, plus the number of columns; `swap`
  exchanges rows and columns.
* `IsMatchedPair`: the centred entries of a row and a column are opposite, and their signs times the
  centred row entry exceed the absolute difference of the ranks.

## Relation to the literature

Known result: the shape of the theta correspondence of discrete series parameters. Only statements
about the parameters, as integer vectors, are proved here. Sources: J.-S. Li, Theta lifting for
unitary representations with nonzero cohomology, Duke Math. J. 61 (1990); A. Paul, First occurrence
for the dual pairs (U(p,q), U(r,s)), Canad. J. Math. 51 (1999), 636–657.


### `doubledBlock`

 The block [d] = ((d−1)/2, (d−3)/2, …, (1−d)/2), with its entries doubled. 

### `centredBlock`

 The block e + [d] of length d and centre e, with its entries doubled. 

### `shiftedEntry`

 Twice the entries of a parameter λ, l = 2λ, shifted by minus the weight of the other space's
character: for m the rank of the other space and γ = wt χ + m/2 this is l − 2γ + m. 

### `IsBlockRule`

 The block rule at one place, for spaces S, T of ranks n, n' with signs s, t, parameters
l = 2λ, l' = 2λ', and γ = wt χ_S + n/2, γ' = wt χ_T + n'/2. It compares the entries of λ shifted
by −wt χ_T with those of λ' shifted by −wt χ_S. 

### `IsBlockRule.hasGap_left`

 λ has distinct entries in (n−1)/2 + ℤ, and those of opposite signs differ by at least
  500(n+n')³. 

### `IsBlockRule.hasGap_right`

 λ' has distinct entries in (n'−1)/2 + ℤ, and those of opposite signs differ by at least
  500(n+n')³. 

### `IsBlockRule.entries_of_le`

 If n ≤ n', the shifted entries for T are those for S together with the block [n'−n]. 

### `IsBlockRule.entries_of_ge`

 If n' ≤ n, the shifted entries for S are those for T together with the block [n−n']. 

### `IsBlockRule.sign_of_pos`

 A positive shifted entry that occurs on both spaces has the same sign on S and T. 

### `IsBlockRule.sign_of_neg`

 A negative shifted entry that occurs on both spaces has opposite signs on S and T. 

### `mem_doubledBlock`

 The points of (d−1)/2 + ℤ of modulus below d/2 form [d]; here all is doubled. 

### `image_neg_centredBlock`

 Negation sends the block e + [d] to the block −e + [d]. 

### `lt_sign_mul_iff`

 For a natural number d, signs u, v and an integer y: u v y > d says that |y| > d and that
u v is the sign of y. 

### `exists_matched_of_entries_eq`

 From the block rule to matching, for vectors a on C and b on R with distinct entries, where R
has d more elements than C. Suppose three things: the entries of b have the parity of d − 1; they
are those of a together with those of `doubledBlock d` = {d−1, d−3, …, 1−d} (the block [d],
doubled); and whenever a_c = b_r, s_c = t_r if this entry is positive and s_c = −t_r if it is
negative. Then each b_r either equals some a_c with t_r s_c b_r > d or has |b_r| < d, and each a_c
equals some b_r with t_r s_c b_r > d. 

### `entries_eq_of_exists_matched`

 From matching to the block rule, for vectors a on C and b on R, where R has d more elements
than C and b has distinct entries of the parity of d − 1. Suppose that each entry of b is equal to
one of a with t s b > d or has modulus below d, and each entry of a is equal to one of b with
t s b > d. Then the entries of b are those of a together with the block [d], and a common entry
has equal signs if it is positive, opposite ones if it is negative. 

### `shiftedEntry_injective`

 The shifted entries of a parameter with a gap are distinct. 

### `even_shiftedEntry_add_sub_one`

 If the space of λ has rank n = m + d, then its entries shifted for a space of rank m lie in
(d−1)/2 + ℤ, that is, the doubled entries have the parity of d − 1. 

### `centredParam_swap_std`

 The centred column parameter of −λ for the oscillator pair is minus the shifted entry. 

### `isMatchedPair_std_iff`

 For the oscillator pair with rows for T and columns for S, a row r of λ' and a column c of −λ
are matched if and only if the doubled shifted entries agree and t_r s_c times them exceeds
|n'−n|. 

### `isMatch_std_iff`

 λ' and −λ match for the oscillator pair (`IsMatch`) if and only if both have gap 500(n+n')³,
each doubled shifted entry of λ' is matched with one of λ or has modulus below n'−n, and each
doubled shifted entry of λ is matched with one of λ' or has modulus below n−n'. 

### `IsMatch.std_symm`

 If λ', −λ match for the oscillator pair of (T, S), then λ, −λ' match for that of (S, T). 

### `IsBlockRule.symm`

 The block rule is symmetric: for spaces S, T of ranks n, n' with signs s, t, parameters l = 2λ,
l' = 2λ', and γ = wt χ_S + n/2, γ' = wt χ_T + n'/2, if `IsBlockRule γ γ' l l'` holds then so does
`IsBlockRule γ' γ l' l`, with the roles of the two spaces exchanged. 

### `IsMatch.exists_row_of_le`

 If n ≤ n' and λ', −λ match for the oscillator pair, then each column c is matched with a row r:
the doubled shifted entries agree, and t_r s_c times them exceeds n'−n. 

### `isBlockRule_iff_isMatch_of_le`

 The case n ≤ n' of `isBlockRule_iff_isMatch`: the block rule holds if and only if λ' and −λ
match for the oscillator pair with rows for T and columns for S. 

### `isBlockRule_iff_isMatch`

 Parameters λ, λ' on (S, T) satisfy the block rule for γ, γ' if and only if λ', −λ match for the
oscillator pair with rows for T and columns for S. 

### `IsBlockRule.neg`

 The block rule `IsBlockRule γ γ' l l'` is stated for spaces S, T of ranks n, n' with signs s, t,
doubled parameters l = 2λ, l' = 2λ', and γ = wt χ_S + n/2, γ' = wt χ_T + n'/2. It compares the
entries of λ shifted by −wt χ_T with those of λ' shifted by −wt χ_S. If it holds, then −λ, −λ'
satisfy it on (S⁻, T) for n − γ, n' − γ', that is, for the inverse characters: shifted entries and
the signs of S are negated. Here S⁻ is S with all signs negated, and `toHCParam s l` is l read as a
parameter for the signs s. 

### `IsBlockRule.neg_signs`

 The block rule is unchanged when all signs are reversed. Here `l` and `l'` are doubled
Harish-Chandra parameters (l = 2λ, l' = 2λ') for the signs `s` and `t`. The block rule
`IsBlockRule γ γ'` compares the entries of λ shifted by −wt χ_T with those of λ' shifted by −wt χ_S,
where γ = wt χ_S + n/2 and γ' = wt χ_T + n'/2. The claim: if `l`, `l'` satisfy the block rule, then
the same integer vectors, regarded via `toHCParam` as parameters for the signs `-s` and `-t`,
satisfy it for the same `γ`, `γ'`. 

### `IsBlockRule.shift`

 If γ and γ' are raised by integers u and u', then λ + u' and λ' + u still satisfy the block
rule: the shifted entries do not change. 

### `IsBlockRule.shiftedEntry_ne_zero`

 If the block rule holds with n ≤ n', no shifted entry of λ is zero: it is matched with one of
λ', and a matched entry is nonzero. 

### `isBlockRule_iff_of_offsets`

 The block rule for n ≤ n', recentred at an integer e, with offsets p = n − 2γ + 2e and
p' = n' − 2γ' + 2e: both parameters have gap 500(n+n')³, the entries l' + p are the l + p'
together with the doubled entries of the block e + [n'−n], and where an l c + p' equals an
l' r + p, the signs of c and r differ exactly if this number is below 2e. 

### `isBlockRule_iff_of_character`

 The block rule (`IsBlockRule`) for n ≤ n' when γ = e + ⌊n/2⌋ and γ' = e + ⌊n'/2⌋, as for
characters whose weights for spaces of ranks n, n' are e less the fractional parts of n/2, n'/2. It
holds iff four conditions hold. The doubled parameters l = 2λ, l' = 2λ' have gap 500(n+n')³
(distinct entries ≡ card − 1 mod 2, |λ i − λ j| ≥ gap when signs differ). The entries l' + (n mod 2)
are the l + (n' mod 2) together with `centredBlock e (n'−n)`, the doubled entries of the block of
length n'−n centred at e. A column c and a row r with a common entry have s c ≠ t r exactly if it is
below 2e. 

### `isBlockRule_iff_of_character_conj`

 The block rule for n ≤ n' when γ = e + ⌈n/2⌉ and γ' = e + ⌈n'/2⌉, as for characters whose
weights for spaces of ranks n, n' are e plus the fractional parts of n/2, n'/2. It holds iff three
conditions hold. First, both parameters have gap 500(n+n')³. Second, the entries of l' − (n mod 2)
are those of l − (n' mod 2) together with those of `centredBlock e (n'−n)` = {2e + d−1, 2e + d−3, …,
2e + 1−d} for d = n'−n (the block e + [d], doubled). Third, whenever l_c − (n' mod 2) = l'_r − (n
mod 2), s_c ≠ t_r exactly if this common entry is below 2e. 
