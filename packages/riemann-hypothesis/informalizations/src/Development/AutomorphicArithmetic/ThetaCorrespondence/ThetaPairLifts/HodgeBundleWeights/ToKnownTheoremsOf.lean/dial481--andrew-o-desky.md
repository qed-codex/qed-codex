---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean",
  "declarations": [
    "GlobalTheory.CovTop.PublishedHodgeBundleTheorems"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Hypothesis list C: sixty assumed statements on resolution of singularities, arithmetic intersection theory, positivity of line bundles, toroidal compactifications, abelian schemes and p-divisible groups

[Definition / hypothesis ARAK.D046](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.ResolutionCharZero/)

Assume the following fifteen hypotheses for ([The covolume bound, given hypothesis list C](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt/)).

**Arithmetic varieties in coordinates.** Items (3), (4) and (8) use the following description. Fix a finite set $K$ and finite sets $\iota_k$ for $k\in K$, and let $S=\mathbb{Z}[x_{k,i}:k\in K,\ i\in\iota_k]$ with its grading by $\mathbb{N}^K$.

- An *arithmetic variety of dimension $d$ in coordinates* is a multihomogeneous prime ideal $P$ of $S$, with $K$ nonempty, such that every block contains a variable $x_{k,i}\notin P$, $P\cap\mathbb{Z}=0$, and $\dim S/P=d+|K|$. It is the ideal of an integral closed subscheme $X_P$ of the product of projective spaces $\prod_k\mathbb{P}^{|\iota_k|-1}_{\mathbb{Z}}$ that dominates $\operatorname{Spec}\mathbb{Z}$; the last condition says that $X_P$ has dimension $d$. We write $X_P(\mathbb{C})$ for the set of $z\in\prod_k\mathbb{C}^{\iota_k}$ with every block $z_k$ nonzero at which all elements of $P$ vanish.
- When a field $\Omega$ and elements $y_{k,i}\in\Omega$ are given, $P_y$ is the kernel of $S\to\Omega[T_k:k\in K]$, $x_{k,i}\mapsto y_{k,i}T_k$. The $y_{k,i}$ are *birational coordinates* if every element of $\Omega$ is a quotient $g(y)/h(y)$ of multihomogeneous polynomials of the same degree; then $\Omega$ is the function field of $X_{P_y}$.
- A *metrised line bundle* $A=(a,h_A)$ consists of $a\in\mathbb{Z}^K$ and a positive function $h_A$ on the set of $z$ with every block nonzero such that $h_A(cz)=\prod_k|c_k|^{a_k}h_A(z)$ for $c\in(\mathbb{C}^\times)^K$. It stands for the line bundle $\mathcal{O}(a)$ with the metric $\|s\|(z)=|s(z)|/h_A(z)$ on multihomogeneous polynomials $s$ of degree $a$. It is *smooth* if $h_A$ is $C^\infty$, and *invariant under conjugation* if $h_A(\bar z)=h_A(z)$. A *section* of $A$ on $X_P$ is a multihomogeneous $s\in S$ of degree $a$ with $s\notin P$.
- The sections of $\tau A$ in $\Omega$, for birational coordinates $y$ and $\tau\ge0$, form the group $\Gamma_\tau(A)$ of all $s\in\Omega$ such that $s\prod_k y_{k,c_k}^{-\tau a_k}$ lies in the ring $\mathbb{Z}[y_{k,i}/y_{k,c_k}]$ for every choice of indices $c_k\in\iota_k$ with all $y_{k,c_k}\ne0$; $\Gamma^{\nu}_\tau(A)$ is defined in the same way with the integral closures of these rings in $\Omega$. An element $s$ is *small* if $|g(z)|\le|h(z)|\,h_A(z)^{\tau}$ for every $z\in X_{P_y}(\mathbb{C})$ and every pair of multihomogeneous polynomials $g,h$ with $g(y)=s h(y)$ and $\deg g=\deg h+\tau a$. Put $\hat h^0(\tau A)=\log\operatorname{card}_0\{s\in\Gamma_\tau(A)\ \text{small}\}$, and $\hat h^0_\nu(\tau A)$ likewise with $\Gamma^\nu_\tau(A)$. Here $\operatorname{card}_0$ is cardinality for finite sets and zero for infinite sets, $\log 0=0$, and division by zero in the displayed sequences is zero.
- An *intersection pairing* is a rule that assigns a real number $(\hat L_1\cdots\hat L_n\cdot X_P)$ to every $K$, $(\iota_k)$, ideal $P$ and metrised line bundles $L_1,\dots,L_n$, with three properties for arithmetic varieties $P$ of dimension $n$ and smooth $L_j$: it is symmetric in the $L_j$; it is additive in each $L_j$ under tensor product; and for every section $s$ of $L_n$, $$(\hat L_1\cdots\hat L_n\cdot X_P)=\sum_{W}m_W\,c_W-I(P,s;L_1,\dots,L_n),$$ where $W$ runs over the components of the divisor of $s$ on $X_P$ with multiplicities $m_W$, $c_W=(\hat L_1\cdots\hat L_{n-1}\cdot X_W)$ if $W\cap\mathbb{Z}=0$ and $c_W=(L_1\cdots L_{n-1}\cdot X_W)\log p$ if $W$ contains the prime $p$, and $I$ is an integral over $X_P(\mathbb{C})$ (components, multiplicities, the geometric intersection number and the integral were not expanded). This is the inductive definition of arithmetic intersection numbers.
- $A$ is *semipositive relative to $P_0\subseteq P$* if it is smooth and the Levi form of $\log h_A$ is nonnegative at every point of $X_P(\mathbb{C})$ on the vectors tangent to the cone of $P_0$ (tangency not expanded). It is *nef on the fibres* of $X_P$ if $\mathcal{O}(a)$ has nonnegative degree on every one-dimensional $X_W$ with $W\supseteq P$ multihomogeneous prime of positive characteristic, and *nef on the generic fibre* if a degree (an integral over $X_W(\mathbb{C})$, not expanded) is nonnegative for every arithmetic variety $W\supseteq P$ of dimension 2.

**Arithmetic varieties as schemes.** Item (13) uses schemes. Let $k$ be an integral domain that is finitely generated as a $\mathbb{Z}$-module. An *arithmetic variety of relative dimension $D$ over $k$* is an integral scheme $X$ with a closed immersion into some $\mathbb{P}^N_k$, flat over $\mathbb{Z}$, of Krull dimension $D+1$. A *Hermitian line bundle* $\hat L$ on $X$ is a line bundle with, for every ring homomorphism $\sigma\colon k\to\mathbb{C}$, a smooth metric datum on the complex points for $\sigma$, compatible with complex conjugation (the metric datum was not expanded). A *height function* for $\hat L$ is a real function $h$ on the points of $X$ such that, for integral closed subschemes $Z$ with generic point $\eta_Z$: if $Z$ is a scheme of dimension $d$ over a finite field $\kappa$ then $h(\eta_Z)=(L|_Z)^d\log\#\kappa$; if $Z$ has characteristic $0$ and dimension 1 then $h(\eta_Z)$ is the arithmetic degree of $\hat L|_Z$; and if $Z$ has characteristic $0$ and dimension $e+1\ge2$ then for every $m$ and every rational section $r$ of $L^m|_Z$, $m\,h(\eta_Z)=\sum_z\operatorname{mult}_z(\operatorname{div}r)\,h(z)$ minus an archimedean integral (not expanded). We write $\hat L^{D+1}=a$ if some height function for $\hat L$ takes the value $a$ at the generic point of $X$. A section of $L$ is *small* if its norm is at most 1 at every complex point for every $\sigma$. $\hat L$ is *nef* if its metrics are semipositive (not expanded), $L$ has nonnegative degree on every vertical curve, and $\hat L$ has nonnegative arithmetic degree on every integral closed subscheme of characteristic $0$ and dimension 1.

**The statements.**

**(1)** Assume ([Resolution in characteristic zero](https://andrewodesky.com/rh/lean/PositivityTheory.Resplug.ResolutionBlowup.resolutionCharZero/)).

**(2)** *Principalisation of an ideal sheaf in characteristic 0.* Let $X$ be smooth of relative dimension $d$, quasi-compact and separated over a field $k$ of characteristic $0$, let $I$ be an ideal sheaf whose support contains no irreducible component of $X$, and let $E$ be a closed subset with simple normal crossings at each of its points. There are $s\colon X'\to X$ and a closed subset $E'$ of $X'$, obtained by a sequence of blow-ups of a restricted kind relative to $E$ (read in part), such that $X'$ is smooth over $k$, the pulled-back ideal $I\mathcal{O}_{X'}$ is locally generated by one non-zero-divisor, its support has simple normal crossings, and $s$ is an isomorphism over the complement of the support of $I$.

**(3)** *A Poincaré-Lelong identity.* Let $P$ be an arithmetic variety of dimension $n+2$ in coordinates, let $L_1,\dots,L_n,A,B$ be smooth metrised line bundles invariant under conjugation, with $B$ of degree $0$, and let $s$ be a section of $A$. The project attaches to $e$ real functions $\varphi_1,\dots,\varphi_e$ and a real function $g$ a number $J_P(\varphi;g)$, defined through a linear projection of $X_P(\mathbb{C})$ (not expanded). The statement is $$J_P\bigl(\log h_B,\log h_{L_1},\dots,\log h_{L_n};\ \log\|s\|\bigr)=\sum_{W}m_W\,J_W\bigl(\log h_{L_1},\dots;\ \log h_B\bigr)-J_P\bigl(\log h_A,\log h_{L_1},\dots;\ \log h_B\bigr),$$ the sum over the components $W$ of the divisor of $s$ with $W\cap\mathbb{Z}=0$. If $J_P(\varphi;g)=\int_{X_P(\mathbb{C})}g\,dd^c\varphi_1\wedge\dots\wedge dd^c\varphi_e$, this is Stokes' theorem combined with the Poincaré-Lelong formula $dd^c\log\|s\|^{-1}=c_1(A)-\delta_{\operatorname{div}s}$, up to the normalisation of $dd^c$.

**(4)** Assume all three assertions of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(4a)** Assume assertion 1 of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(4b)** Assume assertion 2 of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(4c)** Assume assertion 3 of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(5)** Assume ([Arithmetic intersection and volume](https://andrewodesky.com/rh/lean/PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright/)).

**(6)** Assume the orthogonality assertion (2) of ([Hodge–Tate maps, orthogonality and a cokernel bound](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate/)).

**(7)** Assume ([A polarized retract hypothesis over valuation rings](https://andrewodesky.com/rh/s/def-polarized-retract-valuation-ring.html)).

**(8)** Assume ([A nef section-dimension asymptotic in homogeneous coordinates](https://andrewodesky.com/rh/s/def-nef-normalized-section-asymptotic.html)).

**(9)** Assume ([Integral Siegel compactifications with quadratic period charts](https://andrewodesky.com/rh/s/def-integral-siegel-compactifications.html)).

**(10)** Assume the assertion “Compactification with a logarithmic Kodaira–Spencer map” in item 3 of ([Geometric and counting assumptions for the covolume bound](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.VolumeEstimateHypotheses/)).

**(11)** Assume ([Seminegativity of a semiabelian Lie bundle](https://andrewodesky.com/rh/lean/GlobalTheory.Nef.semiAbelianLieSeminegative/)).

**(12)** Assume ([A point-separation hypothesis for klt pairs](https://andrewodesky.com/rh/s/def-klt-point-separation.html)).

**(13)** Assume both statements below.

**(13a)** *Birational invariance of arithmetic self-intersection.* Let $R$ be a commutative domain finite as a $\mathbb Z$-module, and let $D\in\mathbb N$. Let $X$ and $X'$ be integral schemes with projective structure maps $p:X\to\operatorname{Spec}R$ and $p':X'\to\operatorname{Spec}R$. Require both schemes to be flat over $\mathbb Z$ and to have absolute dimension $D+1$. For every ring homomorphism $\sigma:R\to\mathbb C$, require that both $X_\sigma(\mathbb C)$ and $X'_\sigma(\mathbb C)$ are covered by the $D$-dimensional algebraic coordinate charts in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)).

Let $\pi:X'\to X$ be any morphism over $R$ such that, for some nonempty open $U\subseteq X$, the restriction $\pi^{-1}(U)\to U$ is an isomorphism. For every Hermitian line bundle $\overline L$ on $X$ and every $a\in\mathbb R$, if $a$ is an arithmetic self-intersection of $\overline L$, then it is an arithmetic self-intersection of $\pi^*\overline L$. Use the metric, height and self-intersection conventions of ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)); the pulled-back metric is obtained by composing each local potential with $\pi$ on complex points.

**(13b)** *The top power of the first Chern form integrates to the degree.* Let $F$ be a field, let $Y/F$ be a smooth geometrically integral projective variety of dimension $d\in\mathbb N$, with a chosen closed immersion into some $\mathbb P_F^N$, and let $\sigma:F\hookrightarrow\mathbb C$ be an embedding. Let $\Delta$ be a Cartier divisor on $Y$, let $L$ be a line bundle, and choose a nonzero rational section $r$ of $L$ with Cartier divisor $\Delta$.

Choose a smooth metric $\phi$ on $L$ at $\sigma$, using the local-potential transition and smoothness conditions in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)) at this embedding. Let $\mu^+_{\phi,\sigma,d}$, $\mu^-_{\phi,\sigma,d}$ and $\mathcal I_{\phi,\sigma,d}$ be the signed Chern measures and integral in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)), applied to these local potentials. The constant function $1$ is integrable over all of $Y_\sigma(\mathbb C)$ against each of these two measures, and $$\mathcal I_{\phi,\sigma,d}\bigl(Y_\sigma(\mathbb C),1\bigr)=\deg_F(L^d).$$ Here the geometric top intersection on the right has the Euler-characteristic definition in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)); it is the $d$-fold self-intersection of $\Delta$.

**(14)** Assume all twenty-eight assertions of ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). The labels below refer to the assertions of ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)) in their numbered order.

**(14.1)** Assertion 1: Unitary compactification.

**(14.2)** Assertion 2: Lower bound for arithmetic volume.

**(14.3)** Assertion 3: Volume of a nef bundle.

**(14.4)** Assertion 4: Arithmetic intersection laws.

**(14.5)** Assertion 5: Abelian de Rham assertions.

**(14.6)** Assertion 6: Ray class fields.

**(14.7)** Assertion 7: Potential semiabelian reduction.

**(14.8)** Assertion 8: Strong approximation.

**(14.9)** Assertion 9: Finite-field character series.

**(14.10)** Assertion 10: Good metrics and flag intersections.

**(14.11)** Assertion 11: Hermitian isometries.

**(14.12)** Assertion 12: Quadratic norm equations.

**(14.13)** Assertion 13: Extension of homomorphisms.

**(14.14)** Assertion 14: Simplicity in the closed lowest alcove.

**(14.15)** Assertion 15: A principal polarization has one section.

**(14.16)** Assertion 16: Torsion points.

**(14.17)** Assertion 17: Deformations over divided-power thickenings.

**(14.18)** Assertion 18: Prismatic and Hodge comparison.

**(14.19)** Assertion 19: Kawamata–Viehweg vanishing.

**(14.20)** Assertion 20: Nef numerical assertions.

**(14.21)** Assertion 21: Logarithmic $L^2$ extension.

**(14.22)** Assertion 22: Arithmetic Hilbert–Samuel.

**(14.23)** Assertion 23: Chow forms.

**(14.24)** Assertion 24: Cycle heights.

**(14.25)** Assertion 25: Algebraization of holomorphic sections.

**(14.26)** Assertion 26: Vanishing and isolated non-klt divisors.

**(14.27)** Assertion 27: Principalization.

**(14.28)** Assertion 28: Formal algebraization.

**(15)** *Deformations along divided-power thickenings.* For every commutative ring $R$, every ideal $I$ with nilpotent divided powers, and every surjection $R\to R_0$ with kernel $I$, assume the three deformation assertions of (14.17).

## Global hypotheses for Hodge-bundle estimates

[Definition / hypothesis ARAK.D241](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)

Hypothesis (global Hodge-bundle inputs). Assume all twenty-eight assertions below, with the universal quantifiers indicated in each. These are assumptions in the Hodge-bundle estimates that cite this hypothesis.

1. Unitary compactification. Use the moduli data and coefficient-field models in ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)). For every such datum of signature $(p,q)$ with $p+q\ge1$, every level, every moduli scheme and every coefficient field $K$, there is such a model $Y/K$ smooth of relative dimension $\lfloor[E:\mathbb Q]/2\rfloor pq$. Its reduced boundary $Y\setminus j(X)$ has simple normal crossings. Its semiabelian extension $G/Y$, with its polarization line, satisfies the logarithmic Kodaira–Spencer condition in ([Flag models and logarithmic Kodaira–Spencer maps](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)), with base ring $K$ and open subset $j(X)$.

For assertions 2–4, an arithmetic variety of relative dimension $D\in\mathbb N$ consists of a commutative domain $R$ finite as a $\mathbb Z$-module and an integral projective $R$-scheme $X$, flat over $\mathbb Z$, of absolute dimension $D+1$. Use the Hermitian metrics, arithmetic heights, self-intersections, semipositivity in dimension $D$, nefness on finite fibres and nefness in dimension $D$ of ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)). Write $\widehat{\operatorname{vol}}(\overline L)=V_D(\overline L)$ for its extended-real arithmetic volume on that page.

2. Lower bound for arithmetic volume. For every such $X$, every Hermitian line bundle $\overline L$ whose metric is semipositive in dimension $D$ and which is nef on finite fibres, and every arithmetic self-intersection $a\in\mathbb R$ of $\overline L$, $$a\le\widehat{\operatorname{vol}}(\overline L).$$
3. Volume of a nef bundle. For every such $X$, every Hermitian line bundle $\overline L$ nef in dimension $D$, and every arithmetic self-intersection $a\in\mathbb R$ of $\overline L$, $$\widehat{\operatorname{vol}}(\overline L)=a.$$
4. Arithmetic intersection laws. Assume clauses (4a)–(4g) below for every arithmetic variety $X/R$ of relative dimension $D\in\mathbb N$ in the preceding setup. Use the metric, height, self-intersection, divisor and signed-integral definitions of ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)).

**Intersection functionals.** For any Hermitian line bundle $\overline L$ and family of real functions $u=(u_\sigma)_\sigma$, put $$J_{\overline L}(u)=\sum_\sigma^{\mathrm{fin}}\mathcal I_{L,\sigma,D}(X_\sigma(\mathbb C),u_\sigma),\qquad g(\overline L)=J_{\overline L}(1).$$ The sums, integrals and integrability conditions have the conventions of that shared definition.

For every finite index set $I$ and family $(\overline L_i)_{i\in I}$, let $P_I=\mathbb R[T_i:i\in I]$. For $n\in\mathbb Z^I$, write $$\overline L(n)=\bigotimes_{i\in I}\overline L_i^{\otimes n_i},\qquad \ell_n=\sum_{i\in I}n_iT_i.$$ Negative powers use the dual metric; the empty tensor product is the trivial line with unit norm. An *arithmetic intersection functional* is an $\mathbb R$-linear map $\Phi:P_I\to\mathbb R$ that vanishes on every homogeneous polynomial of degree other than $D+1$ and, for every $n\in\mathbb Z^I$, has $\Phi(\ell_n^{D+1})$ as an arithmetic self-intersection of $\overline L(n)$. A *geometric intersection functional* is an $\mathbb R$-linear map $\Psi:P_I\to\mathbb R$ that vanishes on every homogeneous polynomial of degree other than $D$ and satisfies $$\Psi(\ell_n^D)=g(\overline L(n))\qquad(n\in\mathbb Z^I).$$

**Metric operations.** The functions $u_\sigma$ used below range over all families such that, at every complex point, $u_\sigma$ is locally a smooth real function of finitely many regular functions, in the sense used for metric potentials in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)), and $$u_{\bar\sigma}(\bar y)=u_\sigma(y).$$ Write $\overline M[u]$ for $M$ with local potentials $\phi^M_{\sigma,i}+u_\sigma$, so its squared norm is multiplied by $e^{-u_\sigma}$. Write $\overline{\mathcal O}[u]$ for this modification of the trivial line with unit norm. The constant shift $\overline L(t)$ has potentials $\phi^L_{\sigma,i}+2t$ and multiplies norms by $e^{-t}$. Two Hermitian line bundles are *isometric* if there is a line-bundle isomorphism preserving their pointwise norms at every embedding and every complex point.

**(4a) Existence.** Every Hermitian line bundle has an arithmetic height. Every finite family of Hermitian line bundles admits an arithmetic intersection functional and a geometric intersection functional.

**(4b) A metrized trivial factor.** For every finite family $(\overline L_i)$, every $u$ as above, every arithmetic intersection functional $\Phi$ for $(\overline{\mathcal O}[u],\overline L_i)$ and every $n\in\mathbb Z^I$, $$\Phi(T_*\ell_n^D)=\tfrac12J_{\overline L(n)}(u).$$ Here and below $T_*$ is an additional indeterminate for the distinguished first bundle, separate from all $T_i$.

**(4c) Constant shifts.** For every Hermitian line bundle $\overline L$, every $t\in\mathbb R$ and every arithmetic self-intersection $a\in\mathbb R$ of $\overline L$, the number $$a+(D+1)t\,g(\overline L)$$ is an arithmetic self-intersection of $\overline L(t)$.

**(4d) Rational sections.** For every Hermitian line bundle $\overline M$, every finite family $(\overline L_i)$, every arithmetic intersection functional $\Phi$ for $(\overline M,\overline L_i)$, every $n\in\mathbb Z^I$, every arithmetic height $h$ of $\overline L(n)$ and every nonzero rational section $r$ of $M$, the two signed integrability requirements defining $\mathcal A_{L(n)}(M,r;D)$ hold at every embedding, and $$\Phi(T_*\ell_n^D)=\sum_{z\in X}^{\mathrm{fin}}m_z(r)h(z)-\mathcal A_{L(n)}(M,r;D).$$ In particular, the integrals in this formula use the complement of the Cartier support of $r$, as in that definition.

**(4e) Pullback.** Let $X,Y$ be arithmetic varieties over the same $R$ of the same relative dimension $D$, and let $\pi:Y\to X$ be any $R$-morphism carrying $\eta_Y$ to $\eta_X$ and inducing a finite extension $K(Y)/K(X)$ of degree $d>0$. For every Hermitian line bundle $\overline L$ and every arithmetic self-intersection $a$ of $\overline L$, the number $da$ is an arithmetic self-intersection of $\pi^*\overline L$. For every finite family $(\overline L_i)$ and every arithmetic intersection functional $\Phi$ for it, $d\Phi$ is an arithmetic intersection functional for $(\pi^*\overline L_i)$.

**(4f) Isometries and substitution.** For every pair of isometric Hermitian line bundles $\overline L,\overline M$, every arithmetic height of $\overline L$ is an arithmetic height of $\overline M$. If $\Phi$ is any arithmetic intersection functional for a finite family $(\overline L_i)_{i\in I}$, then $\Phi(T_i^{D+1})$ is an arithmetic self-intersection of $\overline L_i$ for every $i$. For every family $(\overline M_i)_{i\in I}$ with $\overline M_i$ isometric to $\overline L_i$, the same $\Phi$ is an arithmetic intersection functional for $(\overline M_i)$.

For every finite set $J$, every integer matrix $(A_{ji})_{j\in J,i\in I}$ and every family $(\overline M_j)_{j\in J}$ with $\overline M_j$ isometric to $\overline L((A_{ji})_{i\in I})$, the functional $$Q\longmapsto\Phi\!\left(Q\big|_{S_j=\sum_{i\in I}A_{ji}T_i\ (j\in J)}\right),\qquad Q\in\mathbb R[S_j:j\in J],$$ is an arithmetic intersection functional for $(\overline M_j)$.

**(4g) Smooth variation.** For every Hermitian line bundle $\overline M$, every finite family $(\overline L_i)$, every $u$ as above, every arithmetic intersection functional $\Phi$ for $(\overline M,\overline L_i)$ and every arithmetic intersection functional $\Phi'$ for $(\overline M[u],\overline L_i)$, the function $u_\sigma$ is integrable against each of the two signed Chern measures of $\overline L(n)$ over all of $X_\sigma(\mathbb C)$, for every $\sigma$ and every $n\in\mathbb Z^I$. For all such $n$, $$\Phi'(T_*\ell_n^D)=\Phi(T_*\ell_n^D)+\tfrac12J_{\overline L(n)}(u).$$

5. Abelian de Rham assertions. Use ([Divided-power cohomology and its primitive submodules](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.IsNilDP/)) and ([Tangent evaluation and Chern pairings in divided-power cohomology](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.SqExt.val/)). Assume clauses (5a)–(5e) for every commutative ring $R$, every abelian scheme $A/R$ and every $g\in\mathbb N$ for which $A/R$ is smooth of constant relative dimension $g$. Put $H=H^1_{\rm dR}(A/R)$, $P=P_{\rm dR}(A)$, $D=D_{\rm dR}(A)$ and $F=F^1_{\rm prim}(A)$.

**(5a) Cohomology and cup product.** All of $H$ is primitive. It is finite projective, of rank $2g$ at every prime of $R$. There is an $R$-linear isomorphism $\bigwedge^2_R H\to H^2_{\rm dR}(A/R)$ sending $a\wedge b$ to $a\smile b$ for every $a,b\in H$.

**(5b) Hodge submodule and tangent evaluation.** The Lie exactness condition holds. The submodule $F\subseteq P$ has a complementary submodule and is finite projective, of rank $g$ at every prime of $R$.

**(5c) Base change.** For every commutative $R$-algebra $R'$ and every group scheme $A'/R'$ with a group homomorphism $u:A'\to A$ identifying it with $A\times_R R'$, the map $$R'\otimes_R P\longrightarrow P_{\rm dR}(A'),\qquad b\otimes c\longmapsto b\,u^*c,$$ is bijective, and $F^1_{\rm prim}(A')$ is the $R'$-linear span of $u^*F$.

**(5d) Divided-power rigidity.** For every ideal $I\subseteq R$ with nilpotent divided powers $\gamma$, every surjection $R\twoheadrightarrow R_0$ with kernel $I$, and every group scheme $A_0/R_0$ with a group homomorphism $i:A_0\to A$ identifying it with $A\times_R R_0$, the pullback $$i^*:P_{\rm dR}(A)\longrightarrow P_\gamma(A_0/\operatorname{Spec}R_0)$$ is bijective. The target is computed over the composite $A_0\to\operatorname{Spec}R_0\to\operatorname{Spec}R$, with divided powers $\gamma$ on the base ideal $I$.

**(5e) Chern pairings.** For every line bundle $L$ on $A$ and every Chern pairing $\psi$ for $L$ on $D$ in the zero-ideal specialization, $\psi$ vanishes on $\operatorname{Fil}(A)\times\operatorname{Fil}(A)$. It is perfect if $L$ has trivial translation kernel: for every commutative $R$-algebra $B$ and $x\in A(B)$, if $t_x^*L_B\otimes L_B^{-1}$ becomes trivial after an open covering of $\operatorname{Spec}B$, then $x=e$. Here $t_x$ is translation by $x$ on $A_B$, and perfect means that both maps $D\to\operatorname{Hom}_R(D,R)$ induced by the two arguments of $\psi$ are bijective.

6. Ray class fields. Assume the ray-class-field existence hypothesis in ([Ray-class extensions and their character values](https://andrewodesky.com/rh/lean/GlobalTheory.Published.RayClassFieldSt/)).
7. Potential semiabelian reduction. Use ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), ([Relative ampleness by affine section charts](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.RelAmple/)) and ([Rigidification, symmetry and translation kernels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.Rigidified/)). For every rational prime $\ell$, fix an algebraic closure $\overline{\mathbb Q}_\ell$ of $\mathbb Q_\ell$. Let $K\subseteq\overline{\mathbb Q}_\ell$ be any finite extension of $\mathbb Q_\ell$, let $g\in\mathbb N$, and let $A/K$ be an abelian scheme smooth of constant relative dimension $g$. Let $L$ be any relatively ample line bundle on $A$ admitting a rigidification, locally symmetric over $K$, and having trivial translation kernel. There are a finite extension $K'\subseteq\overline{\mathbb Q}_\ell$ of $\mathbb Q_\ell$ containing $K$ and a semiabelian scheme $G$ over $$\mathcal O_{K'}=\text{the integral closure of }\mathbb Z_\ell\text{ in }K'$$ with an isomorphism of $K'$-group schemes $$G\times_{\operatorname{Spec}\mathcal O_{K'}}\operatorname{Spec}K'\simeq A\times_{\operatorname{Spec}K}\operatorname{Spec}K'.$$
8. Strong approximation. Assume ([Strong approximation for special unitary groups](https://andrewodesky.com/rh/lean/GlobalTheory.StrongApproxSUProof.strongApproxSU/)).
9. Finite-field character series. Assume the squarefree polynomial form of ([Cuspidal characters of finite general linear groups](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)).
10. Good metrics and flag intersections. Use ([Rational frame systems and flag refinements](https://andrewodesky.com/rh/lean/GlobalTheory.FlagBundle.Fr/)) and ([Good Hermitian metrics and signed Chern integrals](https://andrewodesky.com/rh/lean/GlobalTheory.GoodMetric.IsMetricOn/)). Assume both assertions below.

**Chern integrals.** For every field $F$, embedding $\sigma:F\hookrightarrow\mathbb C$ and pair of smooth geometrically integral projective $F$-varieties $X,Y$, fix a finite index set $I$ and natural ranks $m=(m_i)_{i\in I}$. Let $E$ be a rational frame system of type $0$ on $X$, let $E'$ be one of type $m$ on $Y$, and let $(\phi,f)$ be a full-flag refinement from $E$ to $E'$. Let $x=(x_{i,a})$ be graded Cartier divisors for $E'$. For every open $O\subseteq X$, every good smooth positive Hermitian metric $H$ on $E$ over $O(\mathbb C)$, and every polynomial $R\in\mathbb R[c_{i,j}:i\in I,\ j\in\mathbb N]$, the Chern integral is finite in the defined signed-measure sense and satisfies $$\int_{O(\mathbb C)}R(c(H))=\deg_Y\bigl(R(e(x))P_m(x)\bigr).$$

**Flag intersections.** For every characteristic-zero field $F$, every such $X,Y,I,m,E,E',(\phi,f)$ and graded divisor family $x$, and all polynomials $Q\in\mathbb R[x_{i,a}]$ and $R\in\mathbb R[c_{i,j}:i\in I,\ j\in\mathbb N]$ with $$\operatorname{Alt}_m Q=R(e(x))\Delta_m(x),$$ one has $$\deg_Y Q(x)=\deg_Y\bigl(R(e(x))P_m(x)\bigr).$$

11. Hermitian isometries. Let $E$ be any CM number field, with conjugation $a\mapsto\bar a$, and let $r\in\mathbb N$. Let $G,G'\in M_r(E)$ be nonsingular Hermitian matrices: $\bar G=G^{\mathsf T}$ and $\bar G'=G'^{\mathsf T}$. Use the convention $$h_G(x,y)=x^{\mathsf T}G\bar y\qquad(x,y\in E^r).$$ Suppose that at every embedding $\tau:E\hookrightarrow\mathbb C$ the forms defined by $\tau(G)$ and $\tau(G')$ have the same signature. This means that for some $p\in\{0,\ldots,r\}$, depending on $\tau$, each admits a complex basis with Gram matrix $\operatorname{diag}(I_p,-I_{r-p})$. If $$\det G'=z\bar z\det G\qquad\text{for some }z\in E,$$ there is $\gamma\in\operatorname{GL}_r(E)$ such that $$h_G(\gamma x,\gamma y)=h_{G'}(x,y)\qquad(x,y\in E^r),$$ or equivalently $G'=\gamma^{\mathsf T}G\bar\gamma$.
12. Quadratic norm equations. For every number field $F$ and nonzero $\delta,x\in F$, if $x=a^2-\delta b^2$ is soluble over every real embedding and every finite completion of $F$, it is soluble over $F$ itself. No nonsquare assumption on $\delta$ is imposed.
13. Extension of homomorphisms. Use the semiabelian schemes of ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)). For every normal Noetherian scheme $S$, every dense open $U\subseteq S$, and every pair of semiabelian schemes $G,H/S$, every group homomorphism $f:G_U\to H_U$ extends uniquely to a group homomorphism $F:G\to H$ with $F|_U=f$. Here normal means that every local ring of $S$ is an integrally closed domain.
14. Simplicity in the closed lowest alcove. Let $\ell$ be any prime, let $k$ be any field of characteristic $\ell$, and let $N\ge0$. Let $\lambda=(\lambda_1,\ldots,\lambda_N)$ be a weakly decreasing integer tuple satisfying $$\lambda_i-\lambda_j+j-i\le\ell\qquad(1\le i<j\le N).$$ Put $d=\lambda_N$ when $N>0$ and $d=0$ when $N=0$, and set $\nu_i=\lambda_i-d\in\mathbb N$. Use the square polynomial dual Weyl module $\nabla_\nu(k)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)), in an $N\times N$ variable matrix $X=(X_{ai})$.

For every commutative $k$-algebra $A$ and $g\in\operatorname{GL}_N(A)$, define the action on $A[X_{ai}]$ by $$(\rho_A(g)P)(X)=\det(g)^dP(g^{\mathsf T}X).$$ For $P\in k[X_{ai}]$, write $P_A$ for its image under the coefficient map $k\to A$. For a $k$-subspace $M\subseteq\nabla_\nu(k)$, let $M_A$ be the $A$-span of $\{P_A:P\in M\}$.

The module $\nabla_\nu(k)$ is nonzero. If a $k$-subspace $M\subseteq\nabla_\nu(k)$ satisfies $$\rho_A(g)(P_A)\in M_A$$ for every commutative $k$-algebra $A$, every $g\in\operatorname{GL}_N(A)$ and every $P\in M$, then $M=0$ or $M=\nabla_\nu(k)$.

15. A principal polarization has one section. Use ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), ([Relative ampleness by affine section charts](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.RelAmple/)) and ([Rigidification, symmetry and translation kernels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.Rigidified/)). Let $k$ be any algebraically closed field, let $g\in\mathbb N$, and let $A/k$ be an abelian scheme smooth of constant relative dimension $g$. Let $L$ be any relatively ample line bundle on $A$ admitting a rigidification, locally symmetric over $k$ and having trivial translation kernel. Then $$\dim_k H^0(A,L)=1.$$
16. Torsion points. For every algebraically closed field $k$, every abelian variety $A/k$ of dimension $g$, and every $n\ge0$ whose image in $k$ is nonzero, the set of $k$-points killed by $n$ has cardinality $n^{2g}$.
17. Deformations over divided-power thickenings. Use ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)) and ([Divided-power cohomology and its primitive submodules](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.IsNilDP/)), including its primitive duals, reduction correspondence, comparison maps and lifted Hodge submodules. Let $p$ be any prime and $R$ any commutative ring in which $p$ is nilpotent. Let $I\subseteq R$ have nilpotent divided powers $\gamma$, and let $\pi:R\twoheadrightarrow R_0$ be a surjection with kernel $I$.

A lift of a group scheme $A_0/R_0$ consists of a group scheme $A/R$ and a map $i:A_0\to A$ identifying $A_0$ with $A\times_RR_0$ as a group scheme. For such a lift, an $R$-submodule $F\subseteq D_{\rm dR}(A)$ is *admissible* if it has a complementary $R$-submodule in $D_{\rm dR}(A)$ and $$\operatorname{Fil}(A_0)=\{d_0\in D_{\rm dR}(A_0):\text{some }d\in F\text{ corresponds to }d_0\text{ under reduction}\}.$$ Assume the following three assertions.

**(17a) Comparison and admissibility.** For every abelian lift $A/R$ smooth of constant relative dimension $g\in\mathbb N$, the primitive comparison $$c_A:P_{\rm dR}(A)\longrightarrow P_\gamma(A_0)$$ is bijective, and $\operatorname{Fil}(A)\subseteq D_{\rm dR}(A)$ is admissible.

**(17b) Realizing a submodule.** For every abelian lift $A'/R$ smooth of constant relative dimension $g\in\mathbb N$ and every admissible $F\subseteq D_{\rm dR}(A')$, there is an abelian lift $A/R$ of the same $A_0$, smooth of constant relative dimension $g$, such that $$\operatorname{Fil}_\gamma(A/A_0)=C_{A'}^{-1}(F)\quad\text{in }D_\gamma(A_0).$$

**(17c) Lifting homomorphisms.** For any abelian lifts $A/R$ and $B/R$, smooth of constant relative dimensions $g,g'\in\mathbb N$, and every group homomorphism $f_0:A_0\to B_0$ with $$f_{0,*}\bigl(\operatorname{Fil}_\gamma(A/A_0)\bigr)\subseteq\operatorname{Fil}_\gamma(B/B_0),$$ there is exactly one group homomorphism $f:A\to B$ satisfying $f\circ i_A=i_B\circ f_0$.

18. Prismatic and Hodge comparison. For every prime $\ell$, algebraically closed characteristic-zero field $C$ with a real nonarchimedean valuation, and ring of valuation integers $O\subseteq C$ with $\ell$ noninvertible and $O$ complete for $(\ell)$, put $O^\flat=\varprojlim_{x\mapsto x^\ell}O/\ell$ and $A_{\inf}=W_\ell(O^\flat)$. For every $\varepsilon\in O^\flat$ such that $(\varepsilon^{1/\ell})^\sharp$ is a primitive $\ell$th root of unity, set $$\xi=\sum_{a=0}^{\ell-1}[\varepsilon^{1/\ell}]^a,\qquad\varphi=\text{Witt Frobenius},\qquad\vartheta:A_{\inf}\to O.$$ There are contravariant functors $M$ to $A_{\inf}$-modules and $D$ to $O$-modules on $\ell$-divisible groups over $O$, Frobenius-semilinear maps $\varphi_G:M(G)\to M(G)$, and $\vartheta$-semilinear maps $r_G:M(G)\to D(G)$. The functor $M$ is additive; each $M(G)$ is finite free of rank the height of $G$; $\varphi(\xi)M(G)\subseteq\operatorname{im}\varphi_G$; $r_G$ is surjective with kernel $\xi M(G)$; and both maps commute with every group homomorphism. There is a functorial exact sequence $$0\longrightarrow\omega_G\xrightarrow{\iota_G}D(G)\xrightarrow{\pi_G}\operatorname{Lie}(G^\vee)\longrightarrow0,$$ with the usual pullbacks on invariant differentials and the dual-homomorphism maps on Lie algebras. There are identifications $M(\mathbb Q_\ell/\mathbb Z_\ell)\simeq A_{\inf}$ and $M(\mu_{\ell^\infty})\simeq A_{\inf}$ under which Frobenius is respectively $\varphi$ and $\varphi(\xi)\varphi$. Every $A_{\inf}$-linear Frobenius-compatible map $M(\mu_{\ell^\infty})\to M(\mathbb Q_\ell/\mathbb Z_\ell)$ comes from exactly one group homomorphism $\mathbb Q_\ell/\mathbb Z_\ell\to\mu_{\ell^\infty}$.
19. Kawamata–Viehweg vanishing. For every algebraically closed characteristic-zero field $k$, every integral smooth projective $k$-scheme $X$ of dimension $D$, every canonical line bundle $K_X$ and every nef and big line bundle $N$, one has $H^q(X,K_X\otimes N)=0$ for every $q>0$.
20. Nef numerical assertions. Over every algebraically closed field $k$, a product of $D$ nef line bundles has nonnegative intersection on every projective $D$-dimensional $k$-scheme. On every integral projective $D$-dimensional scheme, a nef line bundle $N$ is big exactly when $N^D>0$. On every projective $D$-dimensional scheme, a nef line bundle $L$ satisfies $$h^0(X,L^{\otimes m})=\frac{L^D}{D!}m^D+O(m^{D-1})\quad(m\to\infty).$$
21. Logarithmic $L^2$ extension. Let $Y$ be any compact Hausdorff second-countable complex manifold of dimension $n\ge1$, with its Borel measurable structure. Let an abelian group of line-bundle weights be represented on a holomorphic atlas by nonvanishing holomorphic cocycles $g_{L,ij}$ and smooth real metric potentials $\phi_{L,i}$, additive in $L$, with $\phi_{L,j}=\phi_{L,i}-\log|g_{L,ij}|^2$. Require a weight $\kappa$ whose cocycle is the coordinate-change Jacobian, and a measure $d\mu=e^{\phi_{\kappa,i}}dV_i$ in each chart. Assume some weight has positive definite Levi form everywhere. For any weights $E,L$ and holomorphic sections $s_1,\ldots,s_n$ of $L$, put $$S=\sum_{a=1}^n\|s_a\|_L^2,\qquad\psi=n\log S,\qquad Z=\{S=0\}.$$ Suppose $Z$ is finite, each local map $(s_1,\ldots,s_n)$ has nonzero Jacobian $J(P)$ at $P\in Z$, $S\le1$, $\delta>0$, and the Levi form of $\phi_E+\alpha\psi$ is semipositive off $Z$ for every $1\le\alpha\le1+\delta$. For every function $f:Y\to\mathbb C$, there is a holomorphic section $F$ of weight $\kappa+E$ whose coefficient in a chosen chart at each $P\in Z$ is $f(P)$, and $$\int_Y\frac{2^n\|F\|_{\kappa+E}^2e^{-\psi}}{1+(\delta\psi)^2}\,d\mu \le\frac{34}{\delta}\frac{2^{n+1}\pi^n}{(n-1)!}\sum_{P\in Z}\left|\frac{f(P)}{J(P)}\right|^2e^{-\phi_E(P)+n\phi_L(P)}.$$ The local coefficients and potentials on the right are taken in those same chosen charts; squared norms mean $|F_i|^2e^{-\phi_{\kappa+E,i}}$ and $|s_{a,i}|^2e^{-\phi_{L,i}}$. The integral is the nonnegative extended integral. The real logarithm and inverse use their total values $\log0=0$ and $0^{-1}=0$.
22. Arithmetic Hilbert–Samuel. For every arithmetic variety $X$ of relative dimension $D$, every Hermitian line bundle $\overline L$ that is nef in dimension $D$ as defined in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)) and has arithmetic self-intersection $a\in\mathbb R$, and every Hermitian line bundle $\overline N$, the sets $\widehat H^0(X,\overline L^{\otimes m}\otimes\overline N)$ are finite for all sufficiently large $m$, and $$\log\#\widehat H^0(X,\overline L^{\otimes m}\otimes\overline N)=\frac{a}{(D+1)!}m^{D+1}+o(m^{D+1}).$$ This is the conclusion of ([Arithmetic Hilbert–Samuel asymptotic](https://andrewodesky.com/rh/lean/GlobalTheory.arithHilbertSamuel_of_principalisation/)) taken as an assumption here.
23. Chow forms. For every characteristic-zero field $k$, integers $N,D\ge0$, and homogeneous ideal $I\subseteq k[X_0,\ldots,X_{N-1}]$ which becomes prime over an algebraic closure and whose quotient has Krull dimension $D+1$, there is a polynomial $f$ in $D+1$ blocks of $N$ hyperplane coefficients. It is homogeneous of degree $\deg\operatorname{Proj}(k[X]/I)$ in each block, remains irreducible over the algebraic closure, and vanishes at a tuple of hyperplanes exactly when those hyperplanes have a common nonzero vector satisfying every equation in $I$. Any other polynomial with these three properties and these block degrees is a nonzero scalar multiple of $f$.
24. Cycle heights. Clauses (4a) and (4d) hold. In addition, for all arithmetic varieties $X,Y$ of relative dimensions $D,e$, every morphism $\pi:Y\to X$ over the same base such that the closure of the image of the generic point $\eta_Y$ has dimension $e+1$ and $[\kappa(\eta_Y):\kappa(\pi(\eta_Y))]=d$ is finite and positive, every Hermitian $\overline L$ on $X$, and every arithmetic height $h$ of $\overline L$, the pullback $\pi^*\overline L$ has top self-intersection $d\,h(\pi(\eta_Y))$.
25. Algebraization of holomorphic sections. For every smooth projective complex scheme $X$ of constant relative dimension $D$, every compatible system of holomorphic coordinate charts on its analytification and every line bundle $B$, the natural map from algebraic global sections of $B$ to its holomorphic sections is bijective.
26. Vanishing and isolated non-klt divisors. Let $X/\mathbb C$ be any integral normal locally Noetherian projective scheme of dimension $n$. First, let $\Delta$ be an effective rational Weil divisor, $m,r$ positive integers, $G$ a Cartier divisor representing $m(K_X+\Delta)$, $N$ a line bundle, and $M_0$ nef and big. If, for every complete integral curve $C$, $$N\cdot C=\frac{G\cdot C}{m}+\frac{M_0\cdot C}{r},$$ there is an ideal sheaf $\mathcal J$ whose support is exactly the non-klt locus of $(X,\Delta)$ and such that $H^i(X,\mathcal J\otimes N)=0$ for every $i>0$. The condition that $G$ represents the displayed multiple means that there is a single nonzero rational top form $\eta$ such that $G=m(\operatorname{div}\eta+\Delta)$ as Weil divisors. Second, assume $n\ge1$, $(X,\Delta)$ is klt, $x$ is a closed point, $r$ is a positive integer, and $N_0$ is nef and big. For every function $c:\mathbb N\to\mathbb R$ with $c(e)>0$ for $1\le e\le n$, if $$c(e)^e<\frac{N_0^e\cdot Z}{r^e}$$ for every irreducible closed $e$-dimensional $Z$ containing $x$ and every $e\ge1$, and $\sum_{e=1}^n e/c(e)\le1$, there are $m>0$, an effective Cartier divisor $D_0$, and an open neighborhood $U$ of $x$ such that $D_0/m$ and $N_0/r$ have equal intersections with every complete integral curve, $(X,\Delta+D_0/m)$ is log canonical on $U$, and its only non-klt point in $U$ is $x$.
27. Principalization. Assume ([Principalization on a smooth projective variety](https://andrewodesky.com/rh/lean/PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisation_closed/)) for every characteristic-zero field, every smooth integral projective variety and every nonzero ideal sheaf, including the unit ideal.
28. Formal algebraization. For every Noetherian commutative ring $R$ complete for an ideal $I$, put $R_e=R/I^{e+1}$. Every compatible system of proper $R_e$-schemes $Y_e$, with $Y_e=Y_{e+1}\times_{R_{e+1}}R_e$, and line bundles $N_e\simeq\beta_e^*N_{e+1}$ with $N_0$ relatively ample has a proper algebraization $X/R$ and a relatively ample line bundle $M$ with $Y_e\simeq X\times_RR_e$ and $N_e\simeq M|_{Y_e}$, compatibly with the transition maps $\beta_e$. Also, for every proper $X/R$, every separated finite-type $Z/R$, and every compatible family of maps $X\times_RR_e\to Z$ over $R$, there is exactly one $R$-morphism $X\to Z$ inducing them.
