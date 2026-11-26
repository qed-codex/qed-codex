---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/ExistsIsClosedImmersionGenericPoint.lean",
  "declarations": [
    "GlobalTheory.HermLB",
    "GlobalTheory.HermLB.ArchIntegrable",
    "GlobalTheory.HermLB.IsArithHeight",
    "GlobalTheory.HermLB.IsNef",
    "GlobalTheory.HermLB.IsSelfInter",
    "GlobalTheory.HermLB.SemiPos",
    "GlobalTheory.HermLB.archInt",
    "GlobalTheory.HermLB.curveDeg",
    "GlobalTheory.HermLB.fs",
    "GlobalTheory.HermLB.shift",
    "GlobalTheory.HermLB.smallSec",
    "GlobalTheory.IsArithVar",
    "GlobalTheory.Weight.SemiPosReg"
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

## Arithmetic image models and Hermitian metrics

[Definition / hypothesis ARAK.D005](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)

Let $K$ be a number field, let $X$ be an integral scheme, and let $p:X\to\operatorname{Spec}\mathcal O_K$ be a morphism. Write $K(X)$ for its function field and $X_\sigma(\mathbb C)$ for its complex points at an embedding $\sigma:K\hookrightarrow\mathbb C$.

**Hermitian metrics.** Present a line bundle $\mathscr L$ by an open cover $(U_i)_{i\in I}$ and units $g_{ij}$ on $U_i\cap U_j$, with $g_{ii}=1$ and $g_{ij}g_{jk}=g_{ik}$ on triple intersections. A section $s$ is represented by regular functions $s_i$ on $U_i$ satisfying $s_i=g_{ij}s_j$ on overlaps.

For every $\sigma$ and $i$, choose a real-valued function $\phi_{\sigma,i}$ on all of $X_\sigma(\mathbb C)$. On the overlaps require $$\phi_{\sigma,j}(y)=\phi_{\sigma,i}(y)-\log|g_{ij}(y)|^2.$$ At every point of $U_i(\mathbb C)$, the function $\phi_{\sigma,i}$ must locally be a smooth real function of finitely many regular functions: on a Zariski-open neighborhood choose $a_1,\ldots,a_r$ and a smooth real function $F$ on an open subset of $\mathbb C^r$, and require $\phi_{\sigma,i}(z)=F(a_1(z),\ldots,a_r(z))$ near that point. Require also $$\phi_{\bar\sigma,i}(\bar y)=\phi_{\sigma,i}(y)\qquad(y\in U_i(\mathbb C)).$$ Here $\bar y$ is the conjugate complex point, over $\bar\sigma$. These data give the pointwise norm $$\|s(y)\|_\sigma^2=|s_i(y)|^2\exp(-\phi_{\sigma,i}(y))\qquad(y\in U_i(\mathbb C)).$$

For $t\in\mathbb R$, write $\overline{\mathscr L}(t)$ for the same line bundle with every $\phi_{\sigma,i}$ replaced by $\phi_{\sigma,i}+2t$. For $h\in\mathbb N$, a small section of $\overline{\mathscr L}(t)^{\otimes h}$ is a section $s\in H^0(X,\mathscr L^{\otimes h})$ such that $$\|s(y)\|_{\sigma,\mathscr L^{\otimes h}}\le\exp(ht)\qquad(\sigma:K\hookrightarrow\mathbb C,\ y\in X_\sigma(\mathbb C)),$$ where the norm on the left is the unshifted tensor-power norm.

**Metrics from generating sections.** Let $r\in\mathbb N$ and let $b_0,\ldots,b_{r-1}$ be sections of $\mathscr L$ whose nonvanishing loci cover $X$. For every ring homomorphism $\tau:\mathcal O_K\to\mathbb C$, choose $A_\tau\in\mathrm{GL}_r(\mathbb C)$. For each $\tau$, require a unitary matrix $U_\tau$ such that $$A_{\bar\tau}=\overline{A_\tau}U_\tau,\qquad \bar\tau(a)=\overline{\tau(a)}.$$ The Fubini–Study metric defined by these sections and matrices has local potentials $$\phi_{\tau,i}(y)=\log\left(\sum_{a=0}^{r-1}\left|\sum_{j=0}^{r-1}(A_\tau)_{ja}b_{j,i}(y)\right|^2\right),$$ where $b_{j,i}$ is the local coefficient of $b_j$ on $U_i$, extended by zero outside $U_i$. Thus $\phi_{\tau,i}=0$ outside $U_i$. On projective space $\mathbb P^N_{\mathcal O_K}$, use the coordinate sections of $\mathcal O(1)$: on $U_i=\{X_i\ne0\}$ their local coefficients are $b_{j,i}=X_j/X_i$, for $0\le j\le N$. Restriction along a morphism pulls back the line bundle and these metric potentials.

**Models of linear evaluations.** Let $V$ be a $K$-vector space with a compatible $\mathcal O_K$-module structure, let $W\subseteq V$ be an $\mathcal O_K$-submodule, and let $\Omega$ be a field containing $K$. Choose a $K$-linear map $\operatorname{ev}:V\to\Omega$, a family of functions $\mathcal N=(N_\sigma:V\to\mathbb R)_\sigma$, a natural number $D$, a field homomorphism $\psi:\Omega\to K(X)$ and a map $$s:W\longrightarrow H^0(X,\mathscr L).$$ These data form an arithmetic image model if the following conditions hold.

- The scheme $X$ is projective over $\mathcal O_K$, flat over $\mathbb Z$, normal, and has absolute dimension $D+1$.
- The map $\psi$ is bijective. For every $a\in\mathcal O_K$, $\psi(a)$ is the rational function obtained by pulling back $a$ along $p$.
- For every $w,w'\in W$ and every chart $U_i$ containing the generic point of $X$, the local coefficients, viewed as rational functions, satisfy $$\psi(\operatorname{ev}(w))\,s(w')_i=\psi(\operatorname{ev}(w'))\,s(w)_i.$$
- The nonvanishing loci of the sections $s(w)$, for $w\in W$, cover $X$.
- There is a frame $(b,g,A)$ for $(\mathcal N,W)$ in ([Image degrees and Chow heights of linear evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)). If $N$ is its basis length and $n$ its number of integral generators, put $\ell_k=\sum_jg_{jk}b_j\in W$. There is a matrix $c\in M_{n\times N}(K)$ with $$b_j=\sum_{k=0}^{n-1}c_{kj}\ell_k\qquad(0\le j<N).$$ For every embedding $\sigma$, every chart $i$ and every $y\in X_\sigma(\mathbb C)$, require $$\phi_{\sigma,i}(y)=\log\left(\sum_{a=0}^{N-1}\left| \sum_{k=0}^{n-1}\left(\sum_{m=0}^{N-1}\sigma(c_{km})(A_\sigma)_{ma}\right)s(\ell_k)_i(y) \right|^2\right).$$ In this last identity, each local coefficient $s(\ell_k)_i$ is extended by zero outside $U_i$. Thus the identity also prescribes $\phi_{\sigma,i}(y)=0$ there.

## Arithmetic heights and self-intersections of Hermitian line bundles

[Definition / hypothesis ARAK.D041](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)

Let $R$ be a commutative ring, let $X$ be an integral scheme and let $p:X\to\operatorname{Spec}R$ be a morphism. A Hermitian line bundle $\overline L$ on $X$ has the open-cover, local-potential, smoothness and conjugation conventions of ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)), with $\sigma$ ranging over all ring homomorphisms $R\to\mathbb C$. Write $X_\sigma(\mathbb C)$ for the corresponding complex points. Arithmetic heights assign a real number to every point of $X$ by the three rules below; a self-intersection is a value of such a height at the generic point.

**Divisors and logarithmic norms.** On an integral scheme $Z$, present a Hermitian line bundle $\overline M$ on an open cover $(U_i)$ with transition units $g_{ij}$. Write $K(Z)$ for the function field. A nonzero rational section $r$ is a family $r_i\in K(Z)^\times$ satisfying $r_i=g_{ij}r_j$ wherever the overlap contains the generic point. Its Cartier divisor has local equation $r_i$. Its Cartier support consists of the points where this divisor is not locally given by a unit.

If $Z$ is locally Noetherian, write $m_z(r)$ for its divisor multiplicity at $z$. This is zero outside codimension one. At a codimension-one point, put $A=\mathcal O_{Z,z}$ and write a local equation as $a/b$ with $a,b\in A\setminus\{0\}$; then $$m_z(r)=\operatorname{length}_A(A/aA)-\operatorname{length}_A(A/bA).$$

For each line bundle on $q:Z\to\operatorname{Spec}R$, each $\sigma:R\to\mathbb C$ and each $y\in Z_\sigma(\mathbb C)$, fix once a trivializing open $U_i$ containing the underlying point of $y$, independently of the rational section. If $\phi^M_{\sigma,i}$ is the local metric potential, put $$\ell_{M,r,\sigma}(y)=\log|\operatorname{val}_y(r_i)|-\tfrac12\phi^M_{\sigma,i}(y).$$ Here $\operatorname{val}_y(f)$ is evaluation of a rational function when it is regular at the underlying point, and is zero otherwise. The real logarithm has $\log0=0$. This convention also defines $\ell_{M,r,\sigma}$ at zeros and poles. Write $S_{r,\sigma}$ for the complex points whose underlying points lie outside the Cartier support of $r$.

**Signed Chern integrals.** For a Hermitian line bundle $\overline L$ on $Z$ and $e\in\mathbb N$, use all the following algebraic coordinate charts on $Z_\sigma(\mathbb C)$. A chart consists of an affine open $U\subseteq Z$, regular functions $x_1,\ldots,x_e$ defining an etale map $U\to\mathbb A_R^e$, and a homeomorphism $c:V_c\to W_c$ between open subsets of $Z_\sigma(\mathbb C)$ and $\mathbb C^e$. Require $V_c\subseteq U(\mathbb C)$ and $c(y)=(x_1(y),\ldots,x_e(y))$. For every open $U'\subseteq Z$ and regular function $f$ on $U'$, require $f\circ c^{-1}$ to be holomorphic on $W_c\cap(c^{-1})^{-1}(U'(\mathbb C))$.

At $y\in V_c$, choose a line-bundle trivialization containing its underlying point and form the density $$\rho_{L,c}(y)=\frac{e!}{\pi^e}\operatorname{Re}\det\left( \frac{\partial^2(\phi^L_{\sigma,i}\circ c^{-1})}{\partial z_j\partial\bar z_k}(c(y))\right)_{1\le j,k\le e}.$$ The derivatives have the normalizations $\partial_{z_j}=\tfrac12(\partial_{u_j}-i\partial_{v_j})$ and $\partial_{\bar z_j}=\tfrac12(\partial_{u_j}+i\partial_{v_j})$. The density is independent of the chosen line-bundle trivialization. For each sign $\varepsilon\in\{1,-1\}$, push forward from $W_c$ along $c^{-1}$ the measure with Lebesgue density $$\max\{\varepsilon\rho_{L,c}(c^{-1}(z)),0\}.$$ Let $\mu^\varepsilon_{L,\sigma,e}$ be the supremum of these measures over all such charts, in the ordered set of measures on $Z_\sigma(\mathbb C)$. Write $\mu^+$ and $\mu^-$ for the signs $1$ and $-1$. For $e=0$, the empty determinant is $1$; an empty family of charts has supremum zero.

For a set $S\subseteq Z_\sigma(\mathbb C)$ and a real function $f$, define $$\mathcal I_{L,\sigma,e}(S,f)=\int_S f\,d\mu^+_{L,\sigma,e}-\int_S f\,d\mu^-_{L,\sigma,e}.$$ Integrability against this signed Chern expression means integrability against each of $\mu^+$ and $\mu^-$ separately. For another Hermitian line bundle $\overline M$ and a nonzero rational section $r$ of $M$, put $$\mathcal A_L(M,r;e)=\sum_\sigma^{\mathrm{fin}}\mathcal I_{L,\sigma,e}(S_{r,\sigma},\ell_{M,r,\sigma}).$$ The integrability condition for this expression requires the two integrabilities on $S_{r,\sigma}$ for every $\sigma$.

**Geometric top intersections.** For a field $\kappa$ acting on $\Gamma(Z,\mathcal O_Z)$, put $$\chi_\kappa(F)=\sum_{n\ge0}^{\mathrm{fin}}(-1)^n\dim_\kappa^0 H^n(Z,F),\qquad \deg_\kappa(M^d)=\sum_{S\subseteq\{1,\ldots,d\}}(-1)^{|S|}\chi_\kappa(M^{\otimes(-|S|)}).$$ Here $\dim_\kappa^0$ is vector-space dimension when finite, and zero otherwise. In degree zero the second formula is $\chi_\kappa(\mathcal O_Z)$.

**Arithmetic heights.** A function $h:X\to\mathbb R$ is an arithmetic height of $\overline L$ if the following hold for every integral scheme $Z$ and closed immersion $i:Z\hookrightarrow X$. Write $\eta_Z$ for its generic point and use the pulled-back metric on $L_Z=i^*L$.

1. For every finite field $\kappa$ with a $\kappa$-algebra structure on $\Gamma(Z,\mathcal O_Z)$ and every $d\in\mathbb N$ with $\dim Z=d$, $$h(i\eta_Z)=\deg_\kappa(L_Z^d)\log\#\kappa.$$
2. Suppose $Z$ is locally Noetherian, $\Gamma(Z,\mathcal O_Z)$ has characteristic zero, and $\dim Z=1$. For every nonzero rational section $r$ of $L_Z$, $$h(i\eta_Z)=\sum_{z\in Z}^{\mathrm{fin}}m_z(r)\log\operatorname{card}_0\kappa(z) -\sum_\sigma^{\mathrm{fin}}\sum_{y\in Z_\sigma(\mathbb C)}^{\mathrm{fin}}\ell_{L_Z,r,\sigma}(y).$$ Here $\kappa(z)$ is the residue field and $\operatorname{card}_0$ is its cardinality when finite, and zero otherwise.
3. Suppose $Z$ is locally Noetherian, $\Gamma(Z,\mathcal O_Z)$ has characteristic zero, and $\dim Z=e+1$ with $e\ge1$. For every $m\in\mathbb N$, including $m=0$, and every nonzero rational section $r$ of $L_Z^{\otimes m}$, the integrability condition for $\mathcal A_{L_Z}(L_Z^{\otimes m},r;e)$ holds, and $$m\,h(i\eta_Z)=\sum_{z\in Z}^{\mathrm{fin}}m_z(r)h(iz)-\mathcal A_{L_Z}(L_Z^{\otimes m},r;e).$$

A real number $a$ is an arithmetic self-intersection of $\overline L$ if there exists an arithmetic height $h$ of $\overline L$ such that $h(\eta_X)=a$. **Positivity and curve degrees.** Fix $D\in\mathbb N$. The metric of $\overline L$ is *semipositive in dimension $D$* if, for every $\sigma:R\to\mathbb C$, every $D$-dimensional algebraic coordinate chart $c:V_c\to W_c$ defined above, every chosen line-bundle trivialization $U_i$, every $y\in V_c\cap U_i(\mathbb C)$ and every $\xi\in\mathbb C^D$, $$\operatorname{Re}\sum_{j,k=1}^D \frac{\partial^2(\phi^L_{\sigma,i}\circ c^{-1})}{\partial z_j\partial\bar z_k}(c(y))\,\xi_j\overline{\xi_k}\ge0.$$

The bundle $\overline L$ is *nef on finite fibres* if, for every integral closed subscheme $i:Z\hookrightarrow X$ of absolute dimension $1$ and every finite field $\kappa$ with a $\kappa$-algebra structure on $\Gamma(Z,\mathcal O_Z)$, $$\deg_\kappa\bigl((i^*L)^1\bigr)\ge0.$$

For any locally Noetherian integral $R$-scheme $Z$, Hermitian line bundle $\overline M$ on $Z$ and nonzero rational section $r$ of $M$, write $\deg_{\rm ar}(\overline M;r)$ for the right-hand side of the curve formula in rule 2 above, with $L_Z$ replaced by $M$.

The bundle $\overline L$ is *nef in dimension $D$* if its metric is semipositive in dimension $D$, it is nef on finite fibres, and the following holds. For every locally Noetherian integral closed subscheme $i:Z\hookrightarrow X$ of absolute dimension $1$ such that $\Gamma(Z,\mathcal O_Z)$ has characteristic zero, there is a nonzero rational section $r$ of $i^*L$ with $$\deg_{\rm ar}(i^*\overline L;r)\ge0.$$

**Arithmetic volume.** For $m\in\mathbb N$, write $\widehat H^0(X,\overline L^{\otimes m})$ for the small sections in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)), with metric shift $t=0$ and all ring homomorphisms $\sigma:R\to\mathbb C$. Let $N_m$ be their cardinality if finite, and $+\infty$ otherwise. Define $$V_D(\overline L)=\limsup_{\substack{m\to\infty\\m\ge1}} \frac{(D+1)!}{m^{D+1}}\operatorname{Log}N_m\ \in[-\infty,+\infty].$$ The limsup is taken in the extended reals. Here $\operatorname{Log}n=\log n$ for $0<n<\infty$, $\operatorname{Log}0=-\infty$ and $\operatorname{Log}(+\infty)=+\infty$.
