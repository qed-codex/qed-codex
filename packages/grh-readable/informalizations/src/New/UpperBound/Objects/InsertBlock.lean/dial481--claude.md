---
{
  "module": "src/New/UpperBound/Objects/InsertBlock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Inserting a block into a parameter

The parameters of all chains and grids of spaces are built in one way. There are a stem and a finite
set C of centres, each with a length and a kind, down or up. For B ⊆ C the vector λ⁺_B consists of
the stem and the blocks c + [l_c], c ∈ B, and the sign of an entry is −1 to the power of the number
of centres outside B that are down and above it or up and below it. The parameter λ_B is λ⁺_B
lowered by ½ or by 0, as the parity of the rank requires. Everything is at one infinite place, and
entries are doubled.

* `New.CentreSystem`, `New.CentreSystem.IsSeparated`, `New.CentreSystem.IsParam`: the data, the
  conditions on parities and distances, and the parameter λ_B on a space with these signs, up to a
  common sign σ.
* `New.CentreSystem.IsParam.isBlockRule_insert_of_down`,
  `New.CentreSystem.IsParam.isBlockRule_neg_insert_of_up`: the parameters before and after the
  insertion of a block correspond (`New.IsBlockRule`): the parameters themselves for a down centre,
  their negatives for an up centre.

Notions from other files:
* `HCParam s`: integer vectors l = 2λ indexed by the coordinates of a space with signs s.
* `HCParam.HasGap l h`: the entries of λ are distinct and lie in (n − 1)/2 + ℤ, n the rank, and
  entries at coordinates of opposite signs are at least h apart.
* `centredBlock e d`: the doubled entries of e + [d], where [d] = ((d−1)/2, (d−3)/2, …, (1−d)/2).
* `IsBlockRule γ γ' l l'`, for spaces of ranks n, n': both parameters have a large gap; after
  shifting λ by n'/2 − γ' and λ' by n/2 − γ, the longer one is the shorter one together with a block
  centred at 0; and the two coordinates of a common shifted entry have equal signs if the entry is
  positive and opposite signs if it is negative.


### `CentreSystem`

 A stem and a finite set of centres at one place. Each centre has a value, a length and a kind,
down or up. The entries of the stem are doubled; the values of the centres are not. 

### `CentreSystem.centres`

 The finite set C of centres. 

### `CentreSystem.centre`

 The value of a centre. 

### `CentreSystem.length`

 The length of the block that belongs to a centre. 

### `CentreSystem.isUp`

 The kind of a centre: `true` for up, `false` for down. 

### `CentreSystem.stem`

 The doubled entries of the stem. 

### `block`

 The doubled entries of the block c + [l_c], centred at the value of c and of length l_c. 

### `entries`

 The doubled entries of λ⁺_B: the stem and the blocks of the centres in B. 

### `rank`

 The rank n_B: the length of the stem plus the lengths of the blocks in B. 

### `lowering`

 The doubled difference of λ⁺_B and λ_B: it is 1 if the length of the stem and #B are odd, and
0 otherwise. 

### `CountsFor`

 The centre c counts for the doubled entry y: it is down and above y/2, or up and below y/2. 

### `sign`

 The sign of the doubled entry y of λ⁺_B: it is −1 exactly if an odd number of the centres
outside B count for y. 

### `IsSeparated`

 All lengths have one parity, the stem lies in ½ + ℤ or in ℤ as they are even or odd, and each
centre c is at a distance of at least (h + l_c)/2 from the stem and from the other blocks. 

### `IsSeparated.length_mod_two`

 The blocks have lengths of the same parity as the stem. 

### `IsSeparated.odd_add_card`

 The doubled entries of the stem are odd if its length is even, and even if it is odd. 

### `IsSeparated.stem_far`

 The centres are far from the stem. 

### `IsSeparated.block_far`

 The centres are far from the blocks of the other centres. 

### `IsParam`

 The vector l lists 2λ_B on a space of rank n_B, whose signs are those of the entries of λ⁺_B
times the common sign σ. 

### `IsParam.card_eq`

 The space has rank n_B. 

### `IsParam.image_eq`

 Before the lowering the entries are those of λ⁺_B. 

### `IsParam.sign_eq`

 The sign of a coordinate is σ times the sign of its entry. 

### `IsSeparated.subset`

 Dropping centres keeps the separation: if `X` is separated with gap h, then so is the system
with the same data and a subset C of the centres. 

### `sign_eq_ite_sign_insert`

 Inserting the block of a centre c outside B changes the sign of the doubled entry y exactly if
c counts for y (it is down and above y/2, or up and below y/2). 

### `IsSeparated.add_length_le_abs_sub_two_mul_centre`

 In a system with separation h, a centre c outside B is at a distance of at least (h + l_c)/2
from every entry y/2 of λ⁺_B (the stem and the blocks of the centres in B). 

### `IsSeparated.disjoint_entries_block`

 In a separated system the block of a centre c outside B is disjoint from the entries of
λ⁺_B. 

### `IsSeparated.card_entries`

 In a separated system the stem and the blocks of the centres in B are pairwise disjoint, so the
number of entries of λ⁺_B is the rank n_B, the sum of the lengths of the stem and the blocks. 

### `IsSeparated.odd_add_card_of_mem_entries`

 In a separated system every doubled entry y of λ⁺_B (the stem and the blocks of the centres
in B) has the parity opposite to that of the length of the stem. 

### `IsSeparated.rank_mod_two`

 In a separated system the residue mod 2 of the rank n_B is that of the length of the stem minus
the lowering (1 if the length of the stem and #B are odd, 0 otherwise). 

### `IsParam.add_lowering_mem`

 If l lists 2λ_B, each of its entries becomes an entry of 2λ⁺_B when the lowering is added. 

### `IsParam.neg_signs`

 If l lists 2λ_B on the space with signs s and common sign σ, then it lists 2λ_B on the opposite
space, with signs −s and common sign −σ (`toHCParam (-s) l` is l, read for the signs −s). 

### `IsParam.exists_not_countsFor_iff_of_sign_ne`

 If l lists 2λ_B and the coordinates x, x' have different signs, then some centre outside B
counts for exactly one of the two corresponding entries of 2λ⁺_B. 

### `IsParam.hasGap`

 Let X be a system with separation h and B a set of its centres. Let l list 2λ_B on a space of
rank n: λ_B consists of the stem and the blocks of the centres in B, lowered by ½ or 0, and the
sign of a coordinate is σ times −1 to the number of centres outside B that count for its entry.
Then l has gap h: its entries are distinct and congruent to n − 1 mod 2, and the entries of λ_B at
coordinates of opposite signs are at least h apart. 

### `IsSeparated.lowering_eq_rank_emod_two`

 In a separated system let c be a centre outside B, and B' = B ∪ {c}. The lowering of either set
is the rank of the other mod 2: that for B is n_B' mod 2, and that for B' is n_B mod 2. So raising
a parameter by ½ if the other space has odd rank undoes the lowering. 

### `IsParam.card_le_card_insert`

 If l lists 2λ_B and l' lists 2λ_B', for a centre c outside B and B' = B ∪ {c}, then the rank of
the space of l is at most that of the space of l'. 

### `IsParam.image_eq_union_and_sign_ne_iff`

 Let l and l' list 2λ_B and 2λ_B' (`X.IsParam`, common sign `σ`) with coordinate signs `s` and
`t`. Here X is separated with bound h (`X.IsSeparated h`), and B' = B ∪ {c} for a centre
c ∈ `X.centres` outside B ⊆ `X.centres`. Raise each entry of l by `card n'` % 2 and each entry of l'
by `card n` % 2. Then the raised entries of l' are those of l together with
`centredBlock (X.centre c) (card n' - card n)`. Take coordinates x of l and r of l' with equal
raised entries. Then `s x ≠ t r` exactly if `X.CountsFor c` holds for that entry. 

### `IsParam.isBlockRule_insert_of_down`

 Let X be separated with bound h (`IsSeparated h`), B ⊆ `X.centres`, c a centre outside B with
`X.isUp c = false`, B' = B ∪ {c}. Let l list 2λ_B and l' list 2λ_B' for one sign σ on spaces of
ranks `card n`, `card n'`. Here λ_B is the stem of X together with the blocks of the centres in B,
lowered by ½ or 0. If h ≥ 500(`card n` + `card n'`)³, then l and l' satisfy the block rule with
γ = `X.centre c` + ⌊`card n`/2⌋ and γ' = `X.centre c` + ⌊`card n'`/2⌋. 

### `IsParam.isBlockRule_neg_insert_of_up`

 Let X have separation h, let B be a set of its centres, c a centre outside B that is up, B' = B
∪ {c}. Let l list 2λ_B and l' list 2λ_B' for one sign σ on spaces of ranks n, n', where λ_B is the
stem with the blocks of B, lowered by ½ or 0. If h ≥ 500(n + n')³, then −l and −l' satisfy the block
rule with γ = −c + ⌈n/2⌉, γ' = −c + ⌈n'/2⌉: both have the gap 500(n + n')³, the shifted entries of
−l' are those of −l and a block centred at 0, and the coordinates of a common shifted entry have
equal signs if it is positive and opposite signs if it is negative. 
