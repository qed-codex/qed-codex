---
{
  "module": "src/Lib/SiegelWeil/Tower/ConstantTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/ConstantTerm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/ConstantTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The constant term of a theta integral, unfolded along isotropic lines

The constant term, along an isotropic line of the source space `W'`, of the theta kernel and of the
theta integral over the unitary group of the target space.

* `New.Exchange.constTermAt`: the term of a rational vector of the target; it is 0 unless the vector
  is isotropic.
* `New.Exchange.hasSum_constTermAt`, `New.Exchange.integral_thetaIntegral_lineRadical`: the constant
  term of the theta kernel is the sum of these, and, if the kernel is bounded on the target group
  (`IsTargetBounded`), that of the theta integral is the integral of this sum over the target group.
* `New.Exchange.radicalSubgroup`, `New.Exchange.radicalHaar`: the radical of the stabiliser of a
  line of the target space and its Haar measure; `New.Exchange.lintegral_radicalHaar_conj_lineLevi`
  gives the module of conjugation by the Levi factor.
* `New.Exchange.exists_unfold_constant_term`: if the term of the zero vector vanishes and the
  integrand is integrable, the sum unfolds along the isotropic lines (one orbit, by Witt's theorem)
  to an integral in Iwasawa coordinates.

Throughout, `A : W'.Splitting W Unit` writes the source space `W'` as a hyperbolic plane plus `W`.
Where the target space is `V'`, it is split in the same way by `X : V'.Splitting V Unit`, and
`splittingLine X` is the isotropic line spanned by the vector `X.k`. The bracket `[U(V)]` denotes
the quotient of the adelic unitary group `G E t` of `V` by its rational points.

Notions from other files:
* `New.Space.Splitting`: A decomposition V = (lE^p ⊕ kE^p) ⊥ iV₀ over E: isotropic frames l, k with
  l*Jk = 1, an isometry i from V₀ orthogonal to both, and rk V = rk V₀ + 2p.
* `New.Space.Splitting.radicalElement`, `New.Exchange.lineRadical`, `New.Exchange.lineLevi`:
  elements of the unipotent radical and of the Levi factor of the stabiliser of the isotropic line.
* `New.Space.Splitting.homSlice`: The term f[x], a datum on Hom(W, V), of a datum f on Hom(W', V)
  at the value x on k; θ(f) is the sum of the θ(f[x]) over rational x, and
  `New.Space.Splitting.thetaTerm` is θ((ω(g, h) f)[x]), with ω the Weil representation
  `New.pairWeil` of the pair.
* `New.pairTheta`, `New.Exchange.thetaIntegral`: the theta kernel θ(ω(g, h) f) and its integral
  over h in [U(V)].
* `New.Exchange.lineTerm`: for an adele ξ, the map `lineTerm A X true ξ` from data on Hom(W', V') to
  data on Hom(W, V) sends f to the zero term (the mean along the line of `X`) of the term
  f[ξ • X.k]; the model `false` does the same with the roles of the two lines exchanged.

## Relation to the literature

Known; see `Lib.SiegelWeil.Tower.LargeSideConstantTerm` for sources.


### `radicalMeasure`

 The probability measure on the parameters of `lineRadical`: the product of the measures of
adelic matrices modulo rational matrices. Integration against it is the mean over the radical of
the stabiliser of the line modulo its rational points, that is, the constant term. 

### `constTermAt`

 The term of the rational vector `x` of `V` in the constant term along the line of `A`: zero
unless `x` is isotropic, and then the mean of the term of `x` in the theta kernel of `f` over the
radical modulo its centre and its rational points. 

### `thetaTerm_lineRadical`

 The term of the rational vector `x` in the theta kernel at the point `lineRadical A q` of the
radical: the central coordinate `q.2` acts by the character `ψ (tr (xᴴ J x q.2))`, where `ψ` is the
standard additive character and `J` the Gram matrix of `V`, and `q.1` gives the point at which the
term `f[x] = A.homSlice V (V.x⁻¹ x) f` is evaluated. The matrices `V.x⁻¹` and `W.x⁻¹` pass to the
adelic coordinates in which the forms are the standard ones, `stdForm`; `matrixToVec` flattens a
matrix to a vector. The right side does not involve the characters `a`, `b`. 

### `constTermAt_eq_integral`

 The term `constTermAt A x f` is the integral of the term of `x` in the theta kernel of `f` over
the whole radical modulo its rational points, for any automorphic characters `a` and `b`. 

### `hasSum_constTermAt`

 The terms `constTermAt` of all rational vectors of `V` sum to the constant term of the theta
kernel of `f`, that is, to its integral over the radical of the stabiliser of the line of `A`
modulo rational points. 

### `constTermAt_zero`

 The term of the zero vector is the theta functional of `Hom(W, V)` at the term of `f` at `0`. 

### `constTermAt_smul_k`

 For `ξ ≠ 0`, the term of the rational vector `ξ • X.k` on the isotropic line of `X` in the
constant term along the line of `A` (`constTermAt A`, defined as the mean of its theta term over the
radical) equals the theta functional of `Hom(W, V)` at `lineTerm A X true ξ f`. That is the
translate of `f` by `ξ • X.kAdelic * A.kCoord` (`X.kAdelic` is the adelic vector spanning the line
of `X`, `A.kCoord` the coordinate along the `k`-frame of `A`), followed by the zero terms along the
line of `A` and then of `X`. 

### `integral_thetaIntegral_lineRadical`

 Suppose the theta kernel of `f` grows at most like a power of the height on the group of `W'`,
uniformly on the group of `V` (`IsTargetBounded`). Then the constant term at `g` along the line of
`A` of the theta integral of `f` (characters `a`, `b` of [U(1)]) equals the integral over `h` in
`[U(V)]` of the sum of `constTermAt` over the rational vectors `x` of `V` for
`pairWeil W' V a b (g, h) f`. That constant term is the mean over the radical `lineRadical` modulo
its rational points. A term `constTermAt` is zero unless `x` is isotropic, and otherwise the mean of
the term of `x` in the theta kernel over the radical modulo its centre and rational points. Here
`[U(V)]` is the adelic unitary group `G E t` of `V` modulo its rational points. 

### `RadicalCoord`

 Coordinates on the radical of the stabiliser of a line: a column and a hermitian scalar. 

### `hermitianPart`

 The hermitian part `(b + b*) / 2`. 

### `radicalPoint`

 The point of the radical of the stabiliser of the line of `X` with given coordinates. 

### `radicalPoint_hermitianPart`

 The point `X.radicalElement c b` depends only on the hermitian part of `b`. 

### `isClosedEmbedding_radicalPoint`

 The coordinates `radicalPoint X` embed a column and a hermitian scalar as a closed subset of
the adelic unitary group of `V'`. 

### `radicalPoint_mul`

 The group law of the radical in coordinates: the columns add, and the hermitian scalars add
with a correction, the hermitian part of the product of `j` (the chosen element of `E` with
`star j = -j`) and the pairing of the two columns for the standard form. 

### `radicalSubgroup`

 The radical of the stabiliser of the line of `X`, as a subgroup of the adelic unitary group of
`V'`: the range of the coordinates `radicalPoint X`. 

### `mem_radicalSubgroup_iff`

 The radical consists of the elements `X.radicalElement c b`, with `b` not necessarily
hermitian. 

### `radicalHomeomorph`

 The coordinates `radicalPoint X` as a homeomorphism onto the radical. 

### `radicalHaar`

 The measure on the radical that corresponds to the additive Haar measure on its coordinates. 

### `isHaarMeasure_radicalHaar`

 The measure `radicalHaar X` is a left Haar measure on the radical. 

### `lintegral_radicalHaar`

 An integral over the radical, written in the coordinates `radicalPoint X`. 

### `lintegral_radicalHaar_conj_lineLevi`

 Conjugation by the Levi element `lineLevi X (u, h)`, for an idele `u` and a point `h` of the
adelic unitary group of `V`, multiplies integrals over the radical by `|u| ^ (rk V + 1)`, where
`|u| = ideleAbs u` is the module of `u`. 

### `eq_one_of_levi_mem_radical`

 The Levi factor meets the radical only in the identity: if the Levi element `lineLevi X p` lies
in the radical, then `p = 1`. 

### `lintegral_levi_unfold`

 Unfolding on the product of the ideles and the adelic unitary group of `V`: the Haar integral
of a measurable `f` is the integral, against the product of the quotient measures, of the sum of
`f (d * m)` over the pairs `d` of a principal idele and a rational point of the group. 

### `splittingLine`

 The rational isotropic line of the splitting `X`: the span of the vector `X.k`. 

### `lineStabilizer`

 The rational points of the stabiliser of the isotropic line `splittingLine X`, as a subgroup of
the adelic unitary group of `V'`. 

### `mem_lineStabilizer_iff`

 The rational stabiliser of the isotropic line of `X` consists of the rational points (`V'.Γ`)
that multiply the vector `X.kAdelic` spanning the line by a unit of `E`. 

### `instance : DiscreteTopology (lineStabilizer X)`

 The rational stabiliser of the line is discrete, as a subset of the rational points. 

### `continuous_lineLevi`

 The embedding `lineLevi X` of the Levi factor is continuous. 

### `exists_eq_radicalElement_mul_lineLevi_mul`

 The Iwasawa decomposition for the isotropic line of `X`: every `g` is the product of an element
of the radical, a Levi element and an element of the maximal compact subgroup. 

### `lineLevi_mem_lineStabilizer`

 The Levi element of a principal idele `u` and a rational point `g₀` lies in the rational
stabiliser of the isotropic line of `X`. 

### `exists_radicalElement_eq_mul_lineLevi`

 An element of the rational stabiliser of the isotropic line of `X` is moved into the radical by
the Levi element of a principal idele and a rational point. 

### `isCocompact_lineStabilizer_subgroupOf`

 The radical is compact modulo its intersection with the rational stabiliser of the isotropic
line of `X`. 

### `exists_integral_lineStabilizer`

 Iwasawa coordinates modulo the rational stabiliser `P` of the isotropic line of `X`. Let `F` be
measurable and left invariant under the radical (the `X.radicalElement x y`) and under `P`. Put
`Θ ((u, h), κ) = |u| ^ (rk V + 1) F (lineLevi X (u, h) κ)`, and let `ν` be the product of the
quotient measures for ideles `u` modulo `Eˣ` and for `h` modulo the rational points, and of the
Haar measure for `κ` in the maximal compact subgroup. If `Θ` is integrable, then `F` is integrable
modulo `P`, and its integral is `c` times that of `Θ`, where `c ≠ 0` does not depend on `F`. 

### `lineSum`

 The sum of the terms `constTermAt` of the datum `f` moved by `(g, h)`, over the rational
vectors that span `y`. 

### `lineSum_splittingLine`

 The vectors that span the isotropic line of `X` are the `ξ • X.k` with `ξ` in `Eˣ`, so `lineSum`
over this line is the sum of their terms `constTermAt A` for `pairWeil W' V' a b (g, h) f`. This sum
equals the sum over `ξ ∈ Eˣ` of the theta values `θ (W.hom V)` of `lineTerm A X true ξ` applied to
that datum. Here `lineTerm A X true ξ` is translation by `ξ • X.kAdelic * A.kCoord` (`X.kAdelic` is
the adelic vector spanning the line of `X`, `A.kCoord` the coordinate along the `k`-frame of `A`),
followed by the zero term along the line of `A` and then the one along the line of `X`. 

### `lineSum_smul`

 `lineSum A a b f g y h` is the sum, over the rational vectors spanning the subspace `y`, of
their terms `constTermAt A` in the constant term of the datum `pairWeil W' V' a b (g, h) f`. This
sum is unchanged when a rational point `γ` of the unitary group of `V'` moves `y` to `γ • y` and `h`
to `V'.ratEmbed γ * h`, where `V'.ratEmbed γ` is the image of `γ` in the adelic group. 

### `measurable_lineSum`

 The sum of the terms along a line is a measurable function of the point `h`. 

### `lineTerm_pairWeil_radicalElement`

 Moving a datum `f` by an element of the radical of the stabiliser of the isotropic line of `X`
in the Weil representation `pairWeil` does not change `lineTerm A X true ξ f`, the zero term along
that line of the term of `f` at `ξ • X.kAdelic`. 

### `splittingLine_mem_orbit`

 Suppose the term `constTermAt A 0` of the zero vector in the constant term of
`pairWeil W' V' a b (g, h) f` vanishes. Suppose also that the subspace `y` has nonzero `lineSum`,
the sum of the terms `constTermAt A` of this datum over the rational vectors spanning `y`. Then `y`
is spanned by a nonzero isotropic vector, so by Witt's theorem a rational point of the unitary group
`U V'.J` moves it to the isotropic line `splittingLine X` spanned by `X.k`. 

### `exists_unfold_constant_term`

 Unfolding along the isotropic lines. Let `F h` be the datum `f` moved by `(g, h)`. In Iwasawa
coordinates `((u, h), κ)` with measure `ν` (ideles `u` modulo `Eˣ`, `h` modulo the rational points,
`κ` in the maximal compact subgroup), let `Θ` be `|u| ^ (rk V + 1)` times the sum over `ξ` in `Eˣ`
of the theta values of `lineTerm A X true ξ` at `F (lineLevi X (u, h) κ)`, which belong to the
vectors `ξ • X.k` that span the isotropic line of `X`. If the term `constTermAt A` of the zero
vector vanishes and `Θ` is integrable, then the integral of the sum of the terms of all rational
vectors, over the group of `V'` modulo its rational points, is `c` times the integral of `Θ`, where
`c ≠ 0` depends only on the splittings `A` and `X`. 
