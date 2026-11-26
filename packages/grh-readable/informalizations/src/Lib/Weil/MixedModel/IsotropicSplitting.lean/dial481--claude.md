---
{
  "module": "src/Lib/Weil/MixedModel/IsotropicSplitting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/IsotropicSplitting.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/IsotropicSplitting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hyperbolic space and splittings of a hermitian space along isotropic subspaces

A hermitian space `V : New.Space E n s` has Gram matrix `V.J` over `E` and an adelic frame `V.x`
taking it to `New.stdForm E s`. `New.G E s` is the adelic unitary group of that form, and `V.Γ` is
its group of rational points. Here `E` is a CM field (`CMType E`), and `WeilData E` supplies the
purely imaginary `j` (`star j = -j`) used below. The file constructs hyperbolic space together with
its frame, and defines adelic matrices that are orthonormal at the infinite places and integral at
the finite ones. It then studies a splitting, or Witt decomposition,
`V = (range l ⊕ range k) ⊥ i V₀` with `l` and `k` isotropic and dual: it gives the frames and
coordinates of the splitting in adelic form, the Levi and unipotent elements of the stabiliser of
`range k`, the law of a mixed model, and points adapted to the splitting.

## Main definitions and results

* `New.hyperbolicSpace`: the hyperbolic space of rank `2 p` as a `New.Space`, that is, with an
  adelic frame that carries its Gram matrix to the standard form of signs `New.hyperbolicSigns p`
  (`p` times `+1`, `p` times `-1`).
* `New.Exchange.IsOrthoIntegral`: adelic matrices with orthonormal columns at the infinite places
  and integral finite part. The frame of `New.hyperbolicSpace` and its inverse are such
  (`New.Exchange.isOrthoIntegral_hyperbolicSpace`), and the property is stable under products, block
  sums and choice of columns.
* `New.Space.Splitting.levi`, `New.Space.Splitting.radicalElement`: Levi and unipotent elements;
  every `g` with `g k = k a` is a product of the two
  (`New.Space.Splitting.exists_eq_radicalElement_mul_levi`), and the unipotent elements make up the
  unipotent radical (`New.Space.Splitting.exists_eq_radicalElement_iff`).
* `New.Space.Splitting.IsAdapted`: elements of `G` adapted to a splitting and to `t` in `GL_p(𝔸)`;
  they exist (`New.Space.Splitting.exists_isAdapted_and_frame_eq`).
* `New.Space.Splitting.siegelParabolic_sup_symm_eq_top`: if `V₀` is zero, the stabilizers of the
  spans of `k` and of `l` generate the rational unitary group of `V`.
* `New.Space.Splitting.exists_isCompact_rat_mul_radicalElement_mem`: the rational points of the
  unipotent radical are cocompact.

Notions from other files:
* `New.stdForm E s`: the diagonal adelic matrix that is `diag s` at every infinite place and the
  identity at the finite places.
* `New.G.adeleMatrix`: the `n × n` adelic matrix of an element of the adelic unitary group
  `New.G E s`.
* `New.evalInf w`: evaluation of an adele at the infinite place `w`, a ring map to `ℂ`.
* `Ô E`: the integral finite adeles.

## Relation to the literature

Known; see `Lib.Adelic.Witt.IwasawaDecomposition` and `Lib.Weil.MixedModel.ZeroTerm` for sources.


 ## Hyperbolic space; matrices orthonormal at infinity and integral 

### `hyperbolicSigns`

 The sign function on two copies of p that is +1 on the first copy and −1 on the second. 

### `hyperbolicSpace`

 Hyperbolic space of rank `2 p`: the Gram matrix has blocks `(0, 1; 1, 0)`, and the adelic frame
carries it to the standard form with signs `+1` on the first `p` and `−1` on the last `p`
coordinates. The frame is `(1/√2) (1, −1; 1, 1)` at every infinite place and `(1, −c; ϵ, c ϵ̄)` at
the finite places, with `c` the integral unit `New.Weil.normNegOne` (`c̄ c = −1`) and
`ϵ = stdLattice.traceOneAdele` (`ϵ + ϵ̄ = 1`). 

### `Exchange.IsOrthoIntegral`

 An adelic matrix `M` is orthonormal at infinity and integral: `M_wᴴ M_w = 1` at every infinite
place `w`, where `M_w` is the complex matrix of the components of `M` at `w`, and every entry of
`M` has its finite part in `Ô E`. 

### `Exchange.isOrthoIntegral_hyperbolicSpace_x`

 The adelic frame `x` of hyperbolic space is orthonormal at infinity and integral. 

### `Exchange.isOrthoIntegral_hyperbolicSpace_x_inv`

 The inverse `x⁻¹` of the adelic frame of hyperbolic space is orthonormal at infinity and
integral. 

### `Exchange.isOrthoIntegral_hyperbolicSpace`

 For the hyperbolic space `hyperbolicSpace E p` of rank `2 p` (Gram matrix with blocks
`(0, 1; 1, 0)`), consider its adelic frame `x`, which carries the Gram matrix to the signed standard
form with signs `+1` on the first `p` and `−1` on the last `p` coordinates. Both `x` and its inverse
`x⁻¹` are orthonormal at infinity and integral: at each infinite place `w` the complex matrix `M_w`
of components satisfies `M_wᴴ M_w = 1` (unitary for the standard definite form), and every entry has
finite part in `Ô E`. 

### `conjTranspose_map_mul_map`

 The first half of `IsOrthoIntegral A`: `A_wᴴ A_w = 1` at each infinite place `w`, where `A_w` is
the complex matrix `A.map (evalInf w)`. 

### `snd_mem_Ô`

 The second half of `IsOrthoIntegral A`: every entry of `A` has its finite part in `Ô E`. 

### `mul`

 A product of matrices orthonormal at infinity and integral is again such. 

### `block_diag`

 A block sum of matrices orthonormal at infinity and integral is again such. 

### `of_eq_submatrix_mul_of_injective`

 If `B = A.submatrix id e * C`, that is, the matrix of the columns `e j` of `A` times `C`, where
`e` is injective, and `A` and `C` are orthonormal at infinity and integral, then so is `B`. 

### `of_eq_submatrix_mul`

 `of_eq_submatrix_mul_of_injective`, where `simp` proves that `e` is injective when `he` is not
given. 

 ## Splitting along isotropic subspaces: Levi and unipotent parts 

### `G.conjTranspose_adeleMatrix_mul_stdForm_mul_adeleMatrix`

 An element `g` of the adelic unitary group preserves the standard form: `gᴴ S g = S`, with
`S = stdForm E s`. 

### `stdForm_mul_stdForm_mul`

 The standard form `S = stdForm E s` is its own inverse: `S (S a) = a`. 

### `G.adeleMatrix_inv`

 The inverse of `g` has the matrix `S gᴴ S`, with `S = stdForm E s`. 

### `Space.ratMap_mulVec_vecAtPoint`

 For a matrix `i` over `E`, its adelic form `V.ratMap V₁ i = x⁻¹ i x₁`, with `x`, `x₁` the adelic
frames of `V`, `V₁`, sends the adelic vector `x₁⁻¹ y` of a rational vector `y` to the adelic
vector `x⁻¹ (i y)`. 

### `Space.gram_at_point_eq_map`

 For matrices `A`, `B` over `E`, the Gram matrix of `x⁻¹ A` and `x⁻¹ B` for the standard form is
the adelic image of the Gram matrix `Aᴴ J B` of `V`; here `x` is the adelic frame of `V`. 

### `Space.map_conjTranspose_mul_map_J_mul_map`

 A Gram matrix `Aᴴ J B` of `V`, mapped to the adeles, in the right-bracketed form of a product
of the mapped factors. 

### `Space.map_conjTranspose_mul_map_J_mul_map_mul`

 `Space.map_conjTranspose_mul_map_J_mul_map` followed by a further factor `X`. 

 ### Splittings 

### `Space.Splitting`

 A Witt decomposition `V = (l E^p ⊕ k E^p) ⊥ i V₀` over `E`: isotropic frames `l`, `k` with
`lᴴ J k = 1`, an isometry `i` from `V₀` orthogonal to both, and `rk V = rk V₀ + 2 p`. 

### `Space.Splitting.k`

 The frame k, whose columns span one isotropic subspace. 

### `Space.Splitting.l`

 The frame l, whose columns span the dual isotropic subspace. 

### `Space.Splitting.i`

 The matrix i of the embedding of V₀ into V. 

### `Space.Splitting.gram_kk`

 `k` is isotropic: `kᴴ J k = 0`. 

### `Space.Splitting.gram_ll`

 `l` is isotropic: `lᴴ J l = 0`. 

### `Space.Splitting.gram_lk`

 `l` and `k` are dual: `lᴴ J k = 1`. 

### `Space.Splitting.gram_ii`

 `i` is an isometry: `iᴴ J i` is the Gram matrix `V₀.J` of `V₀`. 

### `Space.Splitting.gram_ik`

 The image of i is orthogonal to k. 

### `Space.Splitting.gram_il`

 The image of i is orthogonal to l. 

### `Space.Splitting.card_eq`

 The rank of V is the rank of V₀ plus twice the number of columns of k. 

### `Exchange.hyperbolicSum`

 The orthogonal sum of hyperbolic space of rank 2p and V₀. 

### `Exchange.splittingOfGram`

 The splitting of `V` over `V₀` whose frames `l`, `k` and embedding `i` are the three column
blocks of a matrix `M` over `E`, given that `Mᴴ J M` is the Gram matrix of hyperbolic space plus
`V₀` (the hypothesis `h_gram`) and that the ranks agree (the hypothesis `h_card`). 

 ### Adelic frames and dual coordinates 

### `kAdelic`

 For a splitting of V, the adelic n×p matrix x⁻¹k, x the adelic frame of V: the isotropic
frame k in standard coordinates. 

### `lAdelic`

 For a splitting of V, the adelic n×p matrix x⁻¹l, x the adelic frame of V: the isotropic
frame l in standard coordinates. 

### `iAdelic`

 For a splitting of V over V₀, the adelic matrix ι = x⁻¹ i x₀, with x, x₀ the adelic frames:
the embedding i in standard coordinates. 

### `symm`

 The splitting of V obtained from a given one by exchanging the two isotropic frames k and l
and keeping the embedding i. 

### `kCoord`

 For a splitting, the adelic `p × n` matrix `lAdelicᴴ ε`, with `ε = stdForm E s`; it sends
`lAdelic a + iAdelic w + kAdelic b` to `b`. 

### `iCoord`

 For a splitting, the adelic `n₀ × n` matrix `ε₀ iAdelicᴴ ε`, the adjoint of the adelic embedding
`iAdelic` for the standard forms `ε`, `ε₀` of `V`, `V₀`; it sends
`lAdelic a + iAdelic w + kAdelic b` to `w`. 

### `lCoord`

 For a splitting, the adelic `p × n` matrix `kAdelicᴴ ε`, with `ε = stdForm E s`; it sends
`lAdelic a + iAdelic w + kAdelic b` to `a`. 

### `coord_mul_frame`

 For a splitting, the three coordinate matrices along k, l and V₀ are dual to the adelic frames
k, l, ι: each times its own frame is the identity, and times either other frame is zero. 

### `conjTranspose_coord`

 The adjoints of the three coordinate matrices, written through the adelic frames and the
standard forms. 

### `conjTranspose_kAdelic_mul_stdForm_mul`

 Pairing with `kAdelic` under the standard form is the `l`-coordinate matrix. 

### `conjTranspose_lAdelic_mul_stdForm_mul`

 Pairing with `lAdelic` under the standard form is the `k`-coordinate matrix. 

### `conjTranspose_iAdelic_mul_stdForm_mul`

 Pairing with `iAdelic` under the standard form is the `V₀`-coordinate matrix followed by the
standard form of `V₀`. 

### `coord_mul_frame_mul`

 The relations of `New.Space.Splitting.coord_mul_frame` followed by a further factor `X`, in the
right-bracketed form that `simp` meets. The first two groups say that a coordinate matrix applied to
a combination of the columns of one frame gives its coefficients. The last group says that the
pairing with `kAdelic` or `lAdelic` under the standard form is a coordinate matrix, and the pairing
with `iAdelic` is the `V₀` coordinate matrix followed by the standard form of `V₀`. 

### `sum_frame_mul_coord_eq_one`

 The frames and coordinate matrices of a splitting resolve the identity, so every adelic vector
is the sum of its components along `kAdelic`, `iAdelic` and `lAdelic`. 

### `ActsOnFrame`

 `g` acts on the isotropic frame `k` of the splitting by the matrix `c`: `g k = k c` in adelic
coordinates. 

### `lCoord_mul_adeleMatrix`

 If an element `g` of `G E s` acts on the adelic frame `kAdelic` by an invertible `a`
(`g k = k a`), then `g` multiplies the `l`-coordinate by `a⁻ᴴ`: `lCoord g = a⁻ᴴ lCoord`. 

### `ActsOnFrame.isUnit`

 If an element `g` of `G E s` acts on the adelic frame `kAdelic` by a matrix `a`
(`g k = k a`), then `a` is invertible. 

 ### The Levi subgroup, and composition of splittings 

### `levi`

 The Levi homomorphism `GL_p(𝔸) × G(V₀) → G(V)` of a splitting. The pair `(m, g₀)` goes to the
element that sends the frame `k` to `k m`, the embedded copy `ι` of `V₀` to `ι g₀` and the frame `l`
to `l (m⁻¹)ᴴ`; its matrix is `k m kCoord + ι g₀ iCoord + l (m⁻¹)ᴴ lCoord`. 

### `levi_mul_lAdelic`

 The Levi element of `(a, g)` sends the adelic frame `l` to `l (a⁻¹)ᴴ`. 

### `levi_mul_iAdelic`

 The Levi element of `(a, g)` sends the embedded copy `ι` of `V₀` to `ι g`. 

### `actsOnFrame_levi`

 The Levi element of `(a, g)` acts on the adelic frame `k` by `a`. 

### `comp`

 Composition of splittings. From a splitting `D` of `V` over `V₀` with frames of `p` columns and
a splitting `D'` of `V₀` over `V₁` with frames of `q` columns, the splitting of `V` over `V₁` with
frames `(k, i k')` and `(l, i l')` and embedding `i i'`. 

### `gram_eq_hyperbolicSum`

 The three frames `l`, `k`, `i` of a splitting, side by side in one matrix `M`, have the Gram
matrix of the orthogonal sum of hyperbolic space of rank `2 p` and `V₀`. 

 ### The unipotent radical and the Levi decomposition 

### `radicalElement`

 The unipotent element of `G` with parameters an adelic `n₀ × p` matrix `c` and an adelic `p × p`
matrix `b`. It fixes the frame `k`, sends the embedded copy `ι` of `V₀` to `ι + k cᴴ ε₀` and
the frame `l` to `l − ι c − k (½ j⁻¹ (b + bᴴ) + ½ cᴴ ε₀ c)`, where `ε₀` is the standard form of `V₀`
and `j` the purely imaginary element of the Weil data. Only the hermitian part `z = ½ (b + bᴴ)` of
`b` enters: in the basis `(k, ι, l)` the matrix has the rows `(1, c*, −j⁻¹ z − ½ c* c)`,
`(0, 1, −c)`, `(0, 0, 1)`, with `c* = cᴴ ε₀` the adjoint of `c` for the form of `V₀`. 

### `continuous_radicalElement`

 The unipotent element `radicalElement c b` depends continuously on the pair `(c, b)`. 

### `actsOnFrame_radicalElement`

 The unipotent element `radicalElement c b` fixes the adelic frame `k`. 

### `radicalElement_mul_iAdelic`

 The unipotent element `radicalElement c b` sends the embedded copy `ι` of `V₀` to `ι + k cᴴ ε₀`,
where `ε₀` is the standard form of `V₀`. 

### `radicalElement_mul`

 The Heisenberg group law of the unipotent elements: the parameters `c` add, and the parameters
`b` add with the extra term `j cᴴ ε₀ c'`, where `ε₀` is the standard form of `V₀` and `j` the purely
imaginary element of the Weil data. 

### `levi_conj_radicalElement`

 Conjugation by the Levi element of `(a, g)` sends `radicalElement c b` to
`radicalElement (g c aᴴ) (a b aᴴ)`. 

### `exists_levi_mul_radicalElement_eq`

 Every `radicalElement c b` is a commutator of a Levi element `m = levi (a, 1)` with a unipotent
element `u = radicalElement c b'`: `m * u = u * radicalElement c b * m`. 

### `radicalElement_zero_mul`

 For two unipotent elements, the first with `c = 0`, the product adds the parameters `b`. 

### `eq_of_mul_kAdelic_of_mul_iAdelic_of_mul_lAdelic`

 Two adelic `n × n` matrices are equal when they agree on each of the three adelic frames `k`,
`i` and `l` of a splitting. 

### `exists_eq_radicalElement_mul_levi`

 Levi decomposition of the stabiliser of `range k`. Let `g` in `G` act on the adelic frame `k` by
an adelic `p × p` matrix `a`, that is `g k = k a`. Then `g = radicalElement c b * levi (t, g₀)` for
some parameters `c`, `b`, where `t` in `GL_p(𝔸)` has matrix `a` and `g₀` in `G(V₀)` has as matrix
the `V₀`-block `iCoord * g * iAdelic` of `g`. 

### `exists_eq_radicalElement_iff`

 The unipotent radical of the stabiliser of `A = range k` consists of the `radicalElement c b`:
an element `g` of the adelic unitary group of `V` is of this form exactly when it fixes the frame
`k` and acts as the identity on `A^⊥ / A`, that is, its `V₀`-block `iCoord * g * iAdelic` is `1`. 

 ### The law of the mixed model, and adapted points 

### `IsMixedLaw`

 The law of a mixed Schrödinger model, for maps `T x : 𝒮 V → 𝒮 V₀` with `x` in `𝔸^p`. Write
`y = l a + ι w + k b`, so `a = lCoord y`, `w = iCoord y`, `b = kCoord y`. Then
`T x (ϱ y f) = β (2 x + a) b • ϱ w (T (x + a) f)`, with `β` the bicharacter of
`adelicHeisenberg E 1`: the `l`-part translates `x`, the `k`-part multiplies by a character, and the
`V₀`-part acts on the values. Here `𝒮 V` is the space of the Schrödinger model of `V`, and `V.ϱ y`
is the operator on it of the adelic vector `y`. In the code `2 x + a` is written `x + (x + a)`. 

### `IsMixedLaw.apply_rho_lAdelic_mulVec`

 If the family `T` obeys the law of a mixed model, then translating by a vector `l c` along the
isotropic frame `l` of the splitting shifts the argument of `T` by `c`. 

### `frameAt`

 For `g` in `G` and `t` in `GL_p(𝔸)`, the adelic matrix `g⁻¹ (l (t⁻¹)ᴴ, k t, ι)`, where `l`, `k`,
`ι` are `D.lAdelic`, `D.kAdelic`, `D.iAdelic`, with three column blocks. 

### `gram_frameAt`

 The Gram matrix of `frameAt g t` for the standard form: the hyperbolic block `(0, 1; 1, 0)` for
`l` and `k`, and the standard form of `V₀`. 

### `IsAdapted`

 An element `g` of `G` is adapted to `t` in `GL_p(𝔸)` when the matrix `g⁻¹ (l (t⁻¹)ᴴ, k t, ι)`
has orthonormal columns at every infinite place and integral finite entries. 

### `exists_isAdapted_and_frame_eq`

 Adapted points exist. Let `D` be a Witt decomposition `V = (l E^p ⊕ k E^p) ⊥ i V₀`, where `E` is
a CM field with Weil data, and let `t` be in `GL_p(𝔸)`. Then there are `γ` in `G` and a bijection
`e : (p ⊕ p) ⊕ n₀ ≃ n` of index sets such that: `γ` is adapted to `t` (`γ⁻¹ (l (t⁻¹)ᴴ, k t, i)`,
where `l`, `k`, `i` are the adelic frames `D.lAdelic`, `D.kAdelic`, `D.iAdelic`, has orthonormal
columns at every infinite place and integral finite entries); the signs `s` of `V` reordered by `e`
are `hyperbolicSigns p` followed by `s₀`; and the adelic matrix of `γ` with columns reordered by `e`
equals `((l (t⁻¹)ᴴ, k t) x, i)` (that is, `D.frameAt 1 t` times `x ⊕ 1`), with `x` the adelic frame
of `hyperbolicSpace E p`. 

 ### Rational elements 

### `levi_mem_Gamma`

 The Levi element of a rational matrix `a` in `GL_p(E)` and a rational point `g₀` of `V₀` is a
rational point of `V`. 

### `radicalElement_mem_Gamma`

 The unipotent element `radicalElement (x₀⁻¹ c) b`, for a matrix `c` over `E`, `x₀` the adelic
frame of `V₀` and `b` an adelic matrix with entries in `E` (hypothesis `hb`), lies in the rational
group `Γ` of `V`. 

### `exists_isCompact_rat_mul_radicalElement_mem`

 The rational points of the unipotent radical are cocompact. For a splitting `D` of `V` over
`V₀` along an isotropic subspace of any rank, there is a compact set `K` such that every element
`D.radicalElement c b` of the radical is moved into `K` by left multiplication with some
`D.radicalElement y z` that lies in the group `V.Γ` of rational points. 

### `kAdelic_mulVec_mem_ratVectors`

 The adelic frame `k` sends vectors with entries in `E` to rational vectors of `V`. 

 ## Two opposite parabolic subgroups generate the group of a split space 

### `eq_zero_of_star_dotProduct_self`

 The standard hermitian form `xᴴ x` over the CM field `E` is anisotropic. 

### `exists_skew_isUnit_add_smul`

 Let `a`, `c` be square matrices over the CM field `E` with `aᴴ c + cᴴ a = 0` and with no common
kernel. Then `a + t c` is invertible for some purely imaginary scalar `t`. 

### `siegelParabolic`

 The parabolic subgroup of a splitting `D` without middle part: the rational unitary `γ` that
map the maximal isotropic subspace spanned by the frame `D.k` onto itself. The opposite parabolic
subgroup, of the dual frame `D.l`, is `D.symm.siegelParabolic`. 

### `exists_mem_siegelParabolic_mul_l_eq`

 For a skew-hermitian matrix `b`, the translation `k ↦ k`, `l ↦ l + k b` of the frames of `D` is
given by an element of the parabolic subgroup of `D`. 

### `conjTranspose_mul_add_eq_zero`

 If `g k = k a + l c` for a unitary `g`, then `aᴴ c + cᴴ a = 0`, as `g k` is isotropic. 

### `exists_mul_mem_siegelParabolic`

 The big cell: if `g k = k a + l c` with `a` invertible, then some element of the opposite
parabolic subgroup moves `g` into the parabolic subgroup of `D`. 

### `k_mul_add_l_mul_eq_one`

 In a splitting without middle part every vector is the sum of its components along the frames
`k` and `l`. 

### `siegelParabolic_sup_symm_eq_top`

 Let `D` be a splitting of `V` without middle part. The stabilizers of the spans of the two
isotropic frames `D.k` and `D.l` generate the rational unitary group of `V`. 
