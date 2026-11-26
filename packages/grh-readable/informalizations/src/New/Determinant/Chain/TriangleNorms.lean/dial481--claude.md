---
{
  "module": "src/New/Determinant/Chain/TriangleNorms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Orders of block triangular groups and Gram forms of chains in triangles

The group `New.parabolic (New.blockNumber j)` consists of the invertible block upper triangular
matrices whose diagonal blocks are one copy of `N` and `j` copies of `T`. Its order is
`#GL N R * (#GL T R) ^ j` times a power of `#R` whose exponent does not depend on the commutative
ring `R`.

An abstract triangle of spaces `F i n` has arrows `a t i n : F i n → F i (n + 1)` along row `i` and
`d t i n : F i (n + 1) → F (i + 1) n` down to the next row. The map `j i` embeds `V` in `F i 0`. The
arrows depend on a parameter `t : I`. An abstract relation `M c f` between functions `c : I → ℂ` and
`f : I → ℝ`, unital and multiplicative, is read "`c` has modulus `f`". For nonzero weights, weighted
chains along a row are injective on `V`. If the constants of the squares have prescribed moduli
`L r k`, the squares obey an adjoint law and the Gram forms of the first arrows are given, then the
Gram form of a full chain and the modulus of its constant are computed by induction. In the
application `F i n` is attached to the interval `[i + 1, i + n]`, the arrow `a` adds the greatest
element, and `d` stands for the adjoint of the map that adds the least element.

## Main definitions and results

* `New.exists_card_parabolic_blockNumber_eq`: the order of the group of block triangular matrices
  `New.parabolic (New.blockNumber j)`.
* `New.Exchange.IsTriangle`, `New.Exchange.weightedChain`: the conditions of a triangle; the
  weighted chain of a row.
* `New.Exchange.HasSquareModuli`: the moduli of the constants of the squares and the adjoint law.
* `New.Exchange.IsTriangle.eq_zero_of_weightedChain_eq_zero`: for nonzero weights, chains are
  injective on `V`.
* `New.Exchange.IsTriangle.exists_inner_weightedChain_eq`: for nonzero weights and under
  `HasSquareModuli`, the Gram form of a full chain is that of the product of the Gram operators
  `S t k` of the arrows `a t k 0`, times a ratio of weights and a constant of modulus `∏ L r k`.

Notions from other files:
* `New.BlockIndex N T j`, `New.blockNumber j`: the disjoint union of `N` and `j` copies of `T`, and
  the number of the block of an index (`0` on `N`, and `l` on the `l`-th copy of `T`).
* `New.compUpTo L j`: for linear maps `L i : M i → M (i + 1)`, the composite
  `L (j - 1) ∘ ⋯ ∘ L 0 : M 0 → M j`.


 ## Order of a group of block triangular matrices 

### `blockTriangular_fromBlocks_blockNumber_succ_iff`

 A matrix indexed by `BlockIndex N T (j + 1) = BlockIndex N T j ⊕ T`, the union of `N` and
`j + 1` copies of `T`, is block upper triangular for the numbering `blockNumber` of the blocks
exactly when its upper left corner is block upper triangular and its lower left corner vanishes. 

### `card_parabolic_blockNumber_succ`

 An invertible block upper triangular matrix with blocks `N` and `j + 1` copies of `T` is a
triple: such a matrix with `j` copies of `T`, an arbitrary upper right block and an invertible last
diagonal block. Hence the orders multiply. 

### `exists_card_parabolic_blockNumber_eq.`

 The group `parabolic (blockNumber j)` of invertible block upper triangular matrices with one
diagonal block indexed by `N` and `j` diagonal blocks indexed by `T` has order
`#GL N R * (#GL T R) ^ j * #R ^ k`, with `k` independent of the commutative ring `R`. 

 ## Triangles of arrows: injectivity and Gram forms of chains 

### `SquareCommutes`

 The square at `(i, n)` commutes up to `β`: on `F i (n + 1)`, `w t n` times `a ∘ d` equals
`w t (n + 2) / conj (β t)` times `d ∘ a`. Where `β t = 0` the second scalar is `0`. 

### `SquareAdjoint`

 The adjoint law of the square at `(i, n)` with constant `κ`: every `z` in `F i (n + 2)` has an
adjoint vector `x` for `a`, and `⟪d x, y⟫ = κ t * ⟪d z, a y⟫` for all `y`. 

### `IsTriangle`

 A triangle of size `m` of inner product spaces `F i n` with arrows
`a t i n : F i n → F i (n + 1)` and `d t i n : F i (n + 1) → F (i + 1) n`, weights `w t n` and
isometries `j i : V → F i 0`. The squares commute up to scalars. On the copies of `V`, `a` is
adjoint to `d`, and `d ∘ a` maps each copy injectively to the next. 

### `IsTriangle.square_commutes`

 Each square, for `i + n + 2 ≤ m`, commutes up to a scalar function. 

### `IsTriangle.first_adjoint`

 On the copies of `V`, the first arrow `a` of row `i` is adjoint to `d`. 

### `IsTriangle.comp_mem_range`

 `d ∘ a` maps the copy of `V` in row `i` to the copy of `V` in row `i + 1`. 

### `IsTriangle.eq_zero_of_first`

 `d ∘ a` has trivial kernel on the copy of `V` in row `i`. 

### `HasSquareModuli`

 The moduli of the constants of the squares of a triangle of size `m`, and the adjoint law. 

### `HasSquareModuli.modulus_one`

 The constant `1` has modulus `1`. 

### `HasSquareModuli.modulus_mul`

 Moduli multiply. 

### `HasSquareModuli.exists_modulus_commutes`

 The square at `(i, n)`, for `i + n + 2 ≤ m`, commutes up to a scalar function of modulus
  `L (i + 1) (i + 1 + n + 1)`. 

### `HasSquareModuli.square_adjoint`

 Each square, for `i + n + 2 ≤ m`, obeys the adjoint law with a constant of modulus `1`. 

### `weightedChain`

 The composite `F i 0 → F i n` of the first `n` arrows `a t i k` (`k < n`) of row `i`, each
multiplied by its weight `w t k`. 

### `ChainCommutes`

 `d` moves past the `n`-chain (the weighted composite of the first `n` arrows `a` of a row) up to
`β`: the `n`-chain of row `i + 1` after `d ∘ a` is `w t (n + 1) / (w t 1 * w t 0 * conj (β t))`
times `d` after the `(n + 1)`-chain of row `i`. Where `β t = 0` this scalar is `0`. 

### `ChainAdjoint`

 The arrow `a t i n` that follows the `n`-chain is adjoint to `d` on chains, up to `κ`:
`⟪z, a X⟫ = κ * ⟪d z, Y⟫` for all `z` and all `y` in `V`. Here `X` is the `n`-chain of row `i` at
`j i y`, and `Y` is the `n`-chain of row `i + 1` at `j (i + 1) y`. 

### `ChainCommutes.succ`

 Take weights `w t n`, arrows `a t i n : F i n → F i (n + 1)` along row `i` and maps
`d t i n : F i (n + 1) → F (i + 1) n` down a row, all depending on a parameter `t`. Let `X i n` be
the `n`-chain of row `i`, the weighted composite of its first `n` arrows. Suppose that for each `t`
`X (i + 1) n ∘ d ∘ a = (w (n + 1) / (w 1 * w 0 * conj β)) • d ∘ X i (n + 1)` on `F i 0`
(`ChainCommutes`) and `w n • a ∘ d = (w (n + 2) / conj β') • d ∘ a` on `F i (n + 1)`
(`SquareCommutes`). Then the first law holds with `n + 1` for `n` and `β * β'` for `β`. 

### `ChainAdjoint.succ`

 Let `X i n` be the weighted composite of the first `n` arrows `a` of row `i`, applied to
`j i y`. Suppose `⟪z, a (X i n)⟫ = κ * ⟪d z, X (i + 1) n⟫` for all `y` and `z` (`ChainAdjoint`) and
that every `z` in `F i (n + 2)` has a vector `x` with `⟪a v, z⟫ = ⟪v, x⟫` and
`⟪d x, v'⟫ = κ' * ⟪d z, a v'⟫` for all `v`, `v'` (`SquareAdjoint`). Then the first law holds with
`n + 1` for `n` and `κ * κ'` for `κ`. 

### `IsTriangle.exists_chainAdjoint`

 Take a triangle of size `m` (`IsTriangle`): spaces `F i n` with arrows `a` along the rows and
maps `d : F i (n + 1) → F (i + 1) n`, such that `⟪v, a (j i y)⟫ = ⟪d v, j (i + 1) y⟫` on the
isometric copies `j i` of `V`. Read `M c f` as "the function `c` of the parameter `t : I` has
modulus `f`". Suppose that this relation is unital and multiplicative, that the squares commute up
to constants with the moduli `L`, and that every `z` at the corner of a square has a vector `x` with
`⟪a v, z⟫ = ⟪v, x⟫` and `⟪d x, v'⟫ = κ' * ⟪d z, a v'⟫`, where `M κ' 1` (`HasSquareModuli`). Then
for `i + n < m` there is `κ` with `M κ 1` and `⟪z, a (X i n)⟫ = κ * ⟪d z, X (i + 1) n⟫`
(`ChainAdjoint`), where `X i n` is the weighted composite of `n` arrows of row `i` at `j i y`. 

### `chainCommutes_zero`

 For nonzero weights, `d` moves past the empty chain with constant `1`. 

### `IsTriangle.exists_chainCommutes`

 Take a triangle of size `m` with nonzero weights (`IsTriangle`): arrows `a` along the rows and
maps `d : F i (n + 1) → F (i + 1) n` whose squares commute up to scalars, and isometries
`j i : V → F i 0`. Let `X i n` be the weighted composite of the first `n` arrows of row `i`. For
`i + n < m` there is a function `β` of the parameter with
`X (i + 1) n ∘ d ∘ a = (w (n + 1) / (w 1 * w 0 * conj β)) • d ∘ X i (n + 1)` on `F i 0`
(`ChainCommutes`). 

### `HasSquareModuli.exists_chainCommutes`

 Take weights `w t n ≠ 0`, arrows `a t i n : F i n → F i (n + 1)` and maps
`d t i n : F i (n + 1) → F (i + 1) n`, with a parameter `t : I`. Suppose that the relation `M c f`,
read "`c` has modulus `f`", is unital and multiplicative and that for `i + n + 2 ≤ m` the square
`w n • a ∘ d = (w (n + 2) / conj β') • d ∘ a` on `F i (n + 1)` holds with some `β'` of modulus
`L (i + 1) (i + n + 2)` (part of `HasSquareModuli`). Let `X i n` be the weighted composite of the
first `n` arrows of row `i`. For `i + n < m` some `β` whose modulus is the product of the
`L (i + 1) k` over `i + 1 < k ≤ i + 1 + n` satisfies
`X (i + 1) n ∘ d ∘ a = (w (n + 1) / (w 1 * w 0 * conj β)) • d ∘ X i (n + 1)` (`ChainCommutes`). 

### `IsTriangle.exists_chainCommutes_and_chainAdjoint`

 Take a triangle of size `m` with nonzero weights (`IsTriangle`): arrows `a` along the rows and
maps `d` down a row whose squares commute up to scalars, with `a` adjoint to `d` on the copies `j i`
of `V`. Let `X i n` be the weighted composite of the first `n` arrows of row `i`. For `i + n < m`
there are `β` and `κ`, functions of the parameter `t : I`, such that `X (i + 1) n ∘ d ∘ a = (w
(n + 1) / (w 1 * w 0 * conj β)) • d ∘ X i (n + 1)` (`ChainCommutes`). Moreover, under
`HasSquareModuli`, `κ * β` has modulus the product of the `L (i + 1) k` over `i + 1 < k ≤ i + 1 + n`
and `⟪z, a (X i n)⟫ = κ * ⟪d z, X (i + 1) n⟫` at the images of any `y` in `V` (`ChainAdjoint`). 

### `IsTriangle.eq_zero_of_weightedChain_eq_zero`

 Take a triangle of size `m` with nonzero weights (`IsTriangle`): spaces `F i n`, arrows `a`
along the rows and maps `d` down a row whose squares commute up to scalars, and isometries
`j i : V → F i 0` such that `d ∘ a` maps the image of `j i` injectively to that of `j (i + 1)`.
For `i + n ≤ m` and any parameter `t : I`, the weighted composite of the first `n` arrows of row
`i` is injective on the image of `V`: if it kills `j i y`, then `y = 0`. 

### `IsTriangle.ne_zero_of_chainCommutes`

 Take a triangle of size `m` with nonzero weights and `V ≠ 0` (`IsTriangle`): arrows `a` along
the rows and maps `d` down a row whose squares commute up to scalars, and isometries
`j i : V → F i 0` such that `d ∘ a` maps the image of `j i` injectively to that of `j (i + 1)`. Let
`X i n` be the weighted composite of the first `n` arrows of row `i` and let `i + n < m`. If `X
(i + 1) n ∘ d ∘ a = (w (n + 1) / (w 1 * w 0 * conj β)) • d ∘ X i (n + 1)` on `F i 0`, then `β`
vanishes at no parameter `t : I`. 

### `IsTriangle.ne_zero_of_squareCommutes`

 Take a triangle of size `m` with nonzero weights and `V ≠ 0` (`IsTriangle`): arrows `a` along
the rows and maps `d` down a row whose squares commute up to scalars, with `d ∘ a` mapping each copy
`j i` of `V` injectively to the next. If for `i + n + 2 ≤ m` the square at `(i, n)` satisfies
`w n • a ∘ d = (w (n + 2) / conj β') • d ∘ a` on `F i (n + 1)`, then `β'` has no zero, so both sides
differ by a nonzero factor. 

### `IsTriangle.inner_weightedChain_succ`

 For a parameter `t : I`, the Gram form of the `(n + 1)`-chain of row `i` is expressed through
the `n`-chain of row `i + 1`. This holds for `i + n < m` in a triangle of size `m` with nonzero
weights. Let `X i n` be the weighted composite of the first `n` arrows of row `i`. Suppose `X
(i + 1) n ∘ d ∘ a = (w (n + 1) / (w 1 * w 0 * conj β)) • d ∘ X i (n + 1)` on `F i 0`
(`ChainCommutes`). Suppose `⟪v, a (X i n (j i y))⟫ = κ * ⟪d v, X (i + 1) n (j (i + 1) y)⟫` for all
`y`, `v` (`ChainAdjoint`). Suppose also `j (i + 1) x' = d (a (j i x))`. Then the form of the longer
chain at `(x, z)` is `κ * β * (w 0 * w 1 * w n / w (n + 1))` times the form of the shorter chain at
`(x', z)`. 

### `IsTriangle.exists_inner_weightedChain_eq`

 Take a triangle of size `m` with nonzero weights (`IsTriangle`): arrows `a` along the rows and
maps `d` down a row, with `a` adjoint to `d` on the isometric copies `j i` of `V`. Suppose that the
relation `M c f`, read "`c` has modulus `f`", is multiplicative, that the squares
`w n • a ∘ d = (w (n + 2) / conj β) • d ∘ a` at `(i, n)` hold with `β` of modulus
`L (i + 1) (i + n + 2)`, and that they obey the adjoint law `SquareAdjoint` with constants of
modulus `1` (`HasSquareModuli`). Let `s : U → V` be a map, `S t i` endomorphisms of `U` for the
parameters `t : I`, and `C i` functions of modulus `1`, with
`w 0 * ⟪a x, a (s y)⟫ = C i * ⟪x, s (S t i y)⟫` for each row `i < m`. For `i + n = m` the weighted
composite of the `n` arrows of row `i` has the Gram form `κ * (w 0 * w 1 ^ n / w n) * ⟪x, s (T y)⟫`,
`T = S t i ⋯ S t (m - 1)`. The modulus of `κ` is the product of the `L r k` over `i < r < k ≤ m`. 
