---
{
  "module": "src/Lib/Weil/Unramified/HeckeTransfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/HeckeTransfer.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/HeckeTransfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hecke polynomials pass through a theta lift

Let `w` be a split place of norm q, let S and T be hermitian spaces of ranks n and n + k, and let
the characters `a`, `b` be unramified at `w`. On the vacuum at `w` of the Weil representation
`New.pairWeil S T a b`, the Hecke operators of S and of T count subspaces of the kernels of an
integral matrix and of its transpose modulo `w`. By the q-binomial theorem the Hecke polynomial for
T at `w` is then the rescaled polynomial for S at w̄ times ∏_{l<k}(1 − q^l X), which is
`New.SiegelWeil.qPochhammer q k X`. This identity passes to theta lifts.

## Main definitions and results

* `New.AutChar.frobValue`: the complex number `χ(ϖ_w) q_w^(N/2)`, with
  `χ = New.AutChar.spaceChar a N` and `N = Fintype.card n`.
* `New.SiegelWeil.heckePolyOp_pairWeilTarget`: the identity on the vacuum.
  `New.SiegelWeil.hecke_transfer_of_equivariant` is its image under an equivariant linear map.
* `New.SiegelWeil.hecke_transfer_of_pairing`, `New.SiegelWeil.lift_swap_heckePolyOp`: the transfer
  through an equivariant bilinear map and through the transposed theta lift.
* `New.SiegelWeil.hasHeckePolynomial_of_pairing`, `New.SiegelWeil.hasHeckePolynomial_formLift`: the
  Hecke polynomial of a lift.
* `New.SiegelWeil.hasHeckePolynomial_qPochhammer`: the Hecke polynomial of a fixed vector.

Notions from other files:
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.
* `New.ofSplitPlace`: the map GL_n(E_w) → G_f, g ↦ the unitary element that is g at w and 1 off w,
  w̄.
* `New.LocField`: the completion E_w of E at the finite place w.

## Relation to the literature

Known result: the unramified theta correspondence for GL_n, stated for operators. Compare R. Howe,
θ-series and invariant theory, Corvallis 1979; S. Rallis, Langlands' functoriality and the Weil
representation, Amer. J. Math. 104 (1982); S. Kudla, On the local theta-correspondence, Invent.
Math. 83 (1986).



## The value at a uniformiser of the character attached to a character of [U(1)]

In this section, `a` is a character of `[U(1)]` (`New.AutChar`), `n` is a finite index type of
cardinality `N`, and `w` is a finite place.


### `New.AutChar.frobValue`

 The complex number χ(ϖ_w)·q_w^{N/2}, where N is the cardinality of n,
χ = `New.AutChar.spaceChar` a N is the Hecke character x ↦ a(x/x̄)υ(x)^{−N} and ϖ_w the chosen
uniformiser at w. 


## Transfer of Hecke polynomials through the Weil representation

The Hecke polynomial `New.heckePolyOp π hw X` is the operator ∑_i (−X)^i q^(i choose 2) T_{w,i};
`New.heckePolyCoeff X U` = (−X)^i q^(i choose 2) for a subspace U of dimension i, and
`New.basicCosetRep U` is a coset representative in T_{w,i} with kernel U mod w.

Here `hw` is a proof that w is split.

`New.pairWeil S T a b` is the Weil representation of U(S) × U(T) twisted by the characters a, b; a
vacuum at w is a datum fixed by `projOn {w}`, the averaging operator over integral vectors at w and
w̄; K_w = `New.maxCompactAt n w` is the part above w and w̄ of the maximal compact subgroup.


 ### Hecke polynomials as sums over subspaces of the residue space 

### `CharUnramifiedAt.apply_locFullIdele`

 A Hecke character unramified at w takes at x ∈ E_w^× the value χ(ϖ_w)^(ord_w x). 

### `heckePolyEval_sum_finrank_eq`

 If the `i`-th term is the sum of `y U` over the subspaces `U` of 𝔽_w^n of dimension `i`, then
the sum `New.heckePolyEval` is the sum of `heckePolyCoeff X U • y U` over all subspaces. 

### `heckePolyOp_eq_sum`

 On K_w-fixed vectors the Hecke polynomials at a split place w and at its conjugate are sums over
the subspaces U of 𝔽_w^n, with coefficients `New.heckePolyCoeff` and coset representatives the
transpose, respectively the inverse, of γ_U = `New.basicCosetRep U`. 

### `CharUnramifiedAt.det_maxCompactAt_eq_one`

 If the base change of a is unramified at the split place w, then a ∘ det is trivial on K_w. 

 ### The Hecke polynomials on the vacuum 

### `qPochhammer_add`

 The product of `1 - q ^ j * X` over `j < k + l` splits into the first `k` factors and the
product of length `l` at `q ^ k * X`. 

### `sum_heckePolyCoeff_mul_ite_integral_eq`

 The `q`-binomial theorem weighted by integrality at `w`. Let `y` be a matrix over `E_w` with
columns indexed by `ι₂`, `c : ℂ`, and `γ_U = basicCosetRep U`. The sum over the subspaces `U` of
`𝔽_w^ι₂` of `heckePolyCoeff X U * c ^ dim U` times the indicator that `y γ_U⁻¹` is integral is
`qPochhammer q (card ι₂ - r) (X * c)` times the indicator that `y` is integral, where `r` is the
rank of `y` modulo `w`. 

### `matrixToVec_mem_integralBox_singleton`

 An adelic matrix lies in the box of vectors integral at w if and only if its component at w has
integral entries. 

### `spaceChar_div_sqrt_ideleAbs_pow`

 Let the base change of a be unramified at w, let χ = `a.spaceChar N` with N the cardinality of
n, and let x ∈ E_w^× have order i. Then χ(x)·|x|^(−N/2) = z^i with z = `a.frobValue n w`. 

### `pairWeil_transposeGL_basicCosetRep`

 Translates of the vacuum by the group of T. Let w be split, the base change of a unramified at
w, and f a vacuum at w. Let U be a subspace of 𝔽_w^m of dimension i and γ_U = `New.basicCosetRep U`.
Then γ_Uᵀ sends f to `schrodingerOp {w} Ψ f` (`New.Space.schrodingerOp`), where Ψ is the function
x ↦ z^i·𝟙(xᵀγ_U⁻¹) on finite adelic matrices, read at w. Here 𝟙 is the indicator of the integral
matrices over E_w and z = `a.frobValue n w`. 

### `pairWeil_basicCosetRep_inv`

 Translates of the vacuum by the group of S. Let w be split, the base change of b unramified at
w, and f a vacuum at w. Let U be a subspace of 𝔽_w^n of dimension i and γ_U = `New.basicCosetRep U`.
Then γ_U⁻¹ sends f to `schrodingerOp {w} Ψ f` (`New.Space.schrodingerOp`), where Ψ is the function
x ↦ z^i·𝟙(xγ_U⁻¹) on finite adelic matrices, read at w. Here 𝟙 is the indicator of the integral
matrices over E_w and z = `b.frobValue m w`. 

### `sum_heckePolyCoeff_smul_pairWeil`

 Let w be split of norm q, let the base changes of a and b be unramified at w, and let f be a
vacuum at w (fixed by `projOn {w}`). Let γ_U = `basicCosetRep U`, the representative, with kernel U
mod w, of a coset in the double coset of diag(ϖ1_j, 1), where j = dim U. Let `segmentDatum d c` be
`schrodingerOp {w} Ψ f` (`New.Space.schrodingerOp`), where Ψ(x) is ∏_{l<r}(1 − q^l cX) with
r = d − rank(x mod w) if the matrix x is integral at w, and 0 otherwise. Then the sum over the
subspaces U of 𝔽_w^m of `heckePolyCoeff X U` = (−X)^j q^(j choose 2) times the `pairWeil` action of
γ_Uᵀ at w in the group of T sends f to `segmentDatum d c` with d = `card m` and
c = `a.frobValue n w` = χ(ϖ_w)q^{N/2}, where N = `card n` and χ is x ↦ a(x/x̄)υ(x)^{−N}.

The same holds in the group of S with the subspaces of 𝔽_w^n, with γ_U⁻¹, d = `card n` and
c = `b.frobValue m w`. 

### `sum_heckePolyCoeff_smul_pairWeil_transposeGL`

 The local identity behind the transfer, in the group of T. Let w be split of norm q, let the
base changes of a and b be unramified at w, and let f be a vacuum at w. Write
γ_U = `New.basicCosetRep U`. The sum over the subspaces U of 𝔽_w^m of `heckePolyCoeff X U` times
the action of γ_Uᵀ sends f to `schrodingerOp {w} Ψ f` (`New.Space.schrodingerOp`). Here Ψ(x) is
∏_{l<r}(1 − q^l X α) if the matrix x is integral at w, and 0 otherwise, where α = `a.frobValue n w`
and r is `card m` minus the rank of x modulo w. 

### `sum_heckePolyCoeff_smul_pairWeil_inv`

 The local identity behind the transfer, in the group of S. Let w be split of norm q, let the
base changes of a and b be unramified at w, and let f be a vacuum at w. Write
γ_U = `New.basicCosetRep U`. The sum over the subspaces U of 𝔽_w^n of `heckePolyCoeff X U` times
the action of γ_U⁻¹ sends f to `schrodingerOp {w} Ψ f` (`New.Space.schrodingerOp`). Here Ψ(x) is
∏_{l<r}(1 − q^l X β) if the matrix x is integral at w, and 0 otherwise, where β = `b.frobValue m w`
and r is `card n` minus the rank of x modulo w. 

### `pairWeilSource`

 The Weil representation `New.pairWeil S T a b` restricted to the finite adelic points of the
unitary group of S. 

### `pairWeilTarget`

 The Weil representation `New.pairWeil S T a b` restricted to the finite adelic points of the
unitary group of T. 

### `heckePolyOp_pairWeilTarget`

 Let S and T be hermitian spaces of ranks n and m = n + k, and let a, b be automorphic characters
whose base changes are unramified at the split place w of norm q. Let f in 𝒮(Hom(S, T)) be fixed by
`projOn {w}`. Then f is spherical at w for the Weil action `New.pairWeil` S T a b, (g, h) ↦ a(det h)
b(det g)⁻¹ ω(x ↦ hxg⁻¹), restricted to the finite unitary groups of T (`pairWeilTarget`) and of S
(`pairWeilSource`). Moreover P^T_w(X/α) f = ∏_{l<k}(1 − q^l X) · P^S_{w̄}(q^k X/β) f, where P is the
Hecke polynomial `New.heckePolyOp`, ∑_i (−X)^i q^(i choose 2) T_i, at w (for T) and at w̄ (for S).
Here α = `a.frobValue n w` and β = `b.frobValue m w`, where `c.frobValue N w` = χ(ϖ_w) q^{N/2} with
χ(x) = c(x/x̄) υ(x)^{−N}. 

 ### Transfer through equivariant maps and lifts 

### `hecke_transfer_of_equivariant`

 Hecke transfer through an equivariant map. Let w be split, let S have rank n and T rank
m = n + k, let a and b be unramified at w, and let f be a vacuum at w. Let Λ be linear with
Λ(ω(g,h)f) = π(g)ρ(h)Λf for all finite adelic g, h. Then Λf is K_w-fixed for π and ρ, and
P_w^ρ(X)Λf = ∏_{l<k}(1 − q^l αX)·P_{w̄}^π(q^k αβ⁻¹X)Λf, where P is the Hecke polynomial
`New.heckePolyOp`, q the norm of w, α = `a.frobValue n w` and β = `b.frobValue m w`. 

### `hecke_transfer_of_pairing`

 Hecke transfer through a pairing. Let w be split of norm q, S of rank n, T of rank m = n + k, a,
b unramified at w, and f a vacuum at w. Let B be bilinear on M × W, where M is a space of data that
contains f, and suppose that for finite g, h the translate ω(g,h)f lies in M and
ρ(h)B(f,v) = B(ω(g,h)f, π(g)v). If v is K_w-fixed, then B(f,v) is K_w-fixed and
P_w^ρ(X) B(f,v) = ∏_{l<k}(1 − q^l αX) · B(f, P_w^π(q^k αβ⁻¹X) v), where P is the Hecke polynomial
`New.heckePolyOp`, α = `a.frobValue n w` and β = `b.frobValue m w` (`New.AutChar.frobValue`). 

### `lift_swap_heckePolyOp`

 Hecke transfer through the transposed theta lift, which sends functions on the group of T to
functions on the group of S. Let w be split of norm q, S of rank n, T of rank m = n + k, and a, b
unramified at w̄. Let f be a vacuum at w̄, that is, fixed by the averaging operator `projOn {w̄}`
over integral vectors at w and w̄, and let y be automorphic of rapid decay on the group of T and,
for right translation `finRightRep` by the finite adelic group, K_w-fixed. Then the lift F of y is
K_w-fixed, and the lift of P_w(X) y is ∏_{l<k}(1 − q^l αX) · P_w(q^k αβ⁻¹X) F. Here
P_w(X) = ∑_{i ≤ rank} (−X)^i q^{i choose 2} T_{w,i} is `New.heckePolyOp`,
α = `a.frobValue n (star w)` and β = `b.frobValue m (star w)` (χ(ϖ_{w̄}) q^{N/2} for the Hecke
character χ attached to a, resp. b, in rank N = n, resp. m). 

### `hasHeckePolynomial_of_pairing`

 Let S and T be hermitian spaces of ranks n and m = n + k, and let a, b be automorphic characters
whose base changes are unramified at the split place w of norm q. Let f in 𝒮(Hom(S, T)) be fixed by
`projOn {w}`, and let ω = `New.pairWeil` S T a b, (g, h) ↦ a(det h) b(det g)⁻¹ ω(x ↦ hxg⁻¹). Let B :
M × W → Z be bilinear, where M is a submodule containing f, with ω(g, h)f ∈ M and ρ(h)B(f,
v) = B(ω(g, h)f, π(g)v) for finite g, h. If v is spherical at w and each Hecke polynomial
`New.heckePolyOp`(X) acts on it by p(X), then B(f, v) is spherical at w with eigenvalue
∏_{l<k}(1 − q^l αX) · p(q^k αβ⁻¹X). Here α = `a.frobValue n w`, β = `b.frobValue m w`, and
`c.frobValue N w` = χ(ϖ_w) q^{N/2} with χ(x) = c(x/x̄) υ(x)^{−N}. 

### `hasHeckePolynomial_formLift`

 Let w be split with norm q, let S have rank n and T rank m = n + k, and let a and b be
unramified at w. Let f in 𝒮(Hom(S, T)) be fixed by P^{w} (`projOn {w}`) and be an arrow e → e'
(`New.IsArrow`) for the theta kernel `pairThetaKer S T a b`, where e, e' are functions on G_∞. If
the form y of type e is spherical at w with Hecke eigenvalue p(X), so is its lift `formLift … f y`
(the theta lift, a pairing of data and forms, equivariant for `formRep` because f is an arrow), with
eigenvalue ∏_{l<k}(1 − q^l αX)·p(q^k αβ⁻¹X), where α = `a.frobValue n w` and
β = `b.frobValue m w`. 

 ### The Hecke polynomial of a character 

### `SiegelWeil.hasHeckePolynomial_of_apply_eq_smul_det`

 Let w be a split place of norm q, and let ρ be a character of [U(1)] whose base change
x ↦ ρ(x/x̄) is unramified at w. A vector v on which the finite adelic unitary group of rank n acts
by g ↦ ρ(det g) is spherical at w, and the Hecke polynomial acts on it by ∏_{l<n}(1 − q^l cX), where
c is the value of the base change of ρ at the uniformiser of w. In rank one this is 1 − cX. 

### `SiegelWeil.hasHeckePolynomial_qPochhammer`

 At a split place w of norm q, a vector fixed by the finite adelic unitary group of rank n is
spherical, and the Hecke polynomial acts on it by ∏_{l<n}(1 − q^l X). 

 ### A maximum principle 

### `SiegelWeil.maximum_principle`

 Maximum principle. Let v be a real function bounded above, let finitely many a_i satisfy
∑|a_i| < l, and let l·v(g) ≤ ∑|a_i| v(r(g,i)) for all g. Then v ≤ 0. 
