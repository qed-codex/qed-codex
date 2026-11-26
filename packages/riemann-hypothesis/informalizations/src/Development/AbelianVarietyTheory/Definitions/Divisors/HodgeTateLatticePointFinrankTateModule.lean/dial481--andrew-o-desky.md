---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/HodgeTateLatticePointFinrankTateModule.lean",
  "declarations": [
    "GlobalTheory.HTLat.Point.bLie",
    "GlobalTheory.HTLat.Point.latT"
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

## Eigenspace submodules and integral frames

[Definition / hypothesis AV.D024](https://andrewodesky.com/rh/lean/GlobalTheory.EigenSplit.eigenSub/)

An action on a vector space gives eigenspace intersections and, when the coefficient algebra splits, projected submodules. Integral frames describe a submodule within the span of chosen vectors.

**Eigenspace intersections.** Let $O$ and $\Lambda$ be commutative rings, let $C$ be a field with a specified homomorphism $\iota:O\to C$, and let $V$ be a $C$-vector space, viewed as an $O$-module through this homomorphism. Fix a ring homomorphism $\rho:\Lambda\to\operatorname{End}_C(V)$ and an $O$-submodule $X\subseteq V$. For a ring homomorphism $\chi:\Lambda\to C$, put $$V_\chi=\{x\in V:\rho(a)x=\chi(a)x\text{ for every }a\in\Lambda\},\qquad X^{\mathrm{sub}}_\chi=X\cap V_\chi.$$

**Projected submodules.** Let $I$ be an index set and let $\sigma_i:\Lambda\to C$, for $i\in I$, be ring homomorphisms such that $$\alpha:C\otimes_{\mathbb Z}\Lambda\longrightarrow C^I,\qquad \alpha(c\otimes a)_i=c\sigma_i(a),$$ is bijective. Here $C^I$ is the algebra of all functions $I\to C$, with pointwise operations. For each $i$, let $e_i$ be the inverse image under $\alpha$ of the function equal to $1$ at $i$ and $0$ elsewhere. Extend $\rho$ to the $C$-algebra homomorphism $$\widetilde\rho:C\otimes_{\mathbb Z}\Lambda\longrightarrow\operatorname{End}_C(V),\qquad \widetilde\rho(c\otimes a)(x)=c\rho(a)x.$$ The eigenspace projection and projected submodule at $i$ are $$\pi_i=\widetilde\rho(e_i),\qquad X^{\mathrm{quot}}_i=\pi_i(X)=\{\pi_i(x):x\in X\}.$$

**Integral frames.** For an $O$-submodule $Y\subseteq V$ and a finite tuple $w_1,\ldots,w_n\in V$, the integral-frame condition is that the vectors are $C$-linearly independent and $$\sum_{i=1}^n Ow_i=Y\cap\operatorname{span}_C\{w_1,\ldots,w_n\}.$$ For the empty tuple, both spans are zero.

**Scalar-extension submodules.** Let $p$ be a rational prime, suppose $O$ is a $\mathbb Z_p$-algebra, and suppose the map $O\to C$ respects the $\mathbb Z_p$-algebra structures. For a $\mathbb Z_p$-module $T$ with an action $\Lambda\to\operatorname{End}_{\mathbb Z_p}(T)$, set $$V=C\otimes_{\mathbb Z_p}T,\qquad X=\operatorname{im}\left(O\otimes_{\mathbb Z_p}T\longrightarrow V\right),\qquad o\otimes t\longmapsto \iota(o)\otimes t,$$ The induced action on $V$ is $\rho(a)(c\otimes t)=c\otimes at$. Its eigenspace intersections and projected submodules have the definitions above.

## Auxiliary semiabelian models and Hodge–Tate comparison vectors

[Definition / hypothesis PHT.D082](https://andrewodesky.com/rh/lean/GlobalTheory.HTLat.Point/)

The following data define comparison vectors from the Lie algebra of an integral group scheme to the scalar extension of the Tate module of an abelian variety.

**Valued field and polarization.** Fix a rational prime $p$, an algebraically closed field $C$ of characteristic zero, and a multiplicative valuation $v:C\to\mathbb R_{\ge0}$ with $v(p)<1$. Let $O$ be a commutative ring and let $\iota:O\to C$ be an injective ring homomorphism with image $\{c:v(c)\le1\}$. Assume $O$ is complete and separated for $(p)$, and fix compatible $\mathbb Z_p$-algebra structures on $O$ and $C$. Fix a commutative ring $\Lambda$ with involution $a\mapsto a^*$.

Choose an abelian variety $A/C$ of dimension $g\ge0$ with a line bundle $L$ that is relatively ample, admits a rigidification, is locally symmetric and has trivial translation kernel. These terms have the meanings in ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), ([Relative ampleness by affine section charts](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.RelAmple/)) and ([Rigidification, symmetry and translation kernels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.Rigidified/)). Give $A$ a unital ring action $\rho_A:\Lambda\to\operatorname{End}_C(A)$. To specify its compatibility with the polarization, put $$\mathscr B_L=m_A^*L\otimes\operatorname{pr}_1^*L^{-1}\otimes\operatorname{pr}_2^*L^{-1}\otimes z^*L$$ on $A\times_C A$, where $z$ is the constant identity map. Require, for every $a\in\Lambda$, $$\bigl(\rho_A(a)\times\operatorname{id}\bigr)^*\mathscr B_L\simeq\bigl(\operatorname{id}\times\rho_A(a^*)\bigr)^*\mathscr B_L.$$

**Integral models and their formal comparison.** Choose a semiabelian scheme $G/O$, a group isomorphism $\gamma:A\simeq G_C$, and a unital $\Lambda$-action on $G$ compatible with $\rho_A$ through $\gamma$. Choose also a commutative group scheme $G^{\mathrm t}/O$ with a split torus extension structure as defined in ([Split torus extensions with rigidified line coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.SplitExt/)), and a unital $\Lambda$-action on $G^{\mathrm t}$.

For every commutative $O$-algebra $R$ in which $p$ is nilpotent, give a $\Lambda$-equivariant group isomorphism $$c_R:G^{\mathrm t}(R)\simeq G(R),$$ natural in $R$. For an arbitrary commutative $O$-algebra $R$, say that $x\in G^{\mathrm t}(R)$ and $y\in G(R)$ correspond if, for every $m\ge0$, their reductions satisfy $$y\bmod p^m=c_{R/p^mR}(x\bmod p^m).$$ For $w\in G^{\mathrm t}(O)$, let $Q_w\in G(O)$ be its unique corresponding point and put $$j(w)=\gamma^{-1}\bigl((Q_w)_C\bigr)\in A(C).$$

**Weil-pairing convention.** For an integer $N\ge1$ and $x,y\in A[N](C)$, the value $e_{N,L}(x,y)\in C^\times$ is normalized as follows. A theta lift of $x$ is a nowhere-zero section $$\theta_x\text{ of }L^{\otimes N}\otimes t_x^*L^{\otimes(-N)},$$ where $t_x$ is translation by $x$; define a theta lift of $y$ similarly. Such lifts exist, and for every choice of the two lifts one has $$\theta_x\,t_x^*\theta_y=e_{N,L}(x,y)\,\theta_y\,t_y^*\theta_x.$$ Both sides are sections of $L^{\otimes N}\otimes t_{x+y}^*L^{\otimes(-N)}$ under the natural tensor identifications.

**Tate pairing.** Choose $\varepsilon_n\in C^\times$ for $n\ge0$ with $\varepsilon_0=1$, $\varepsilon_{n+1}^p=\varepsilon_n$ and $\varepsilon_1$ a primitive $p$th root of unity. Put $$T=T_p(A)=\{(t_n)_{n\ge0}:t_n\in A[p^n](C),\ [p]t_{n+1}=t_n\},\qquad V=C\otimes_{\mathbb Z_p}T.$$ The $\mathbb Z_p$-bilinear form $b_\varepsilon:T\times T\to\mathbb Z_p$ is determined by $$\varepsilon_n^{\overline{b_\varepsilon(s,t)}_n}=e_{p^n,L}(s_n,t_n)\qquad(n\ge0),$$ where the exponent is the residue modulo $p^n$, represented by an integer from $0$ to $p^n-1$. Write $\langle\ ,\ \rangle_\varepsilon$ for its $C$-bilinear scalar extension to $V$.

**Characters and comparison vectors.** For every $t\in T$, let $\chi_t=(\chi_{t,n})_n$ be the unique compatible torsion character of $G^{\mathrm t}$, in the sense of ([Compatible torsion characters and logarithmic differentials](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Pdiv.Tv/)), characterized by $$\iota\bigl(\chi_{t,n}(w)\bigr)=e_{p^n,L}\bigl(j(w),t_n\bigr)\qquad\bigl(n\ge0,\ w\in G^{\mathrm t}[p^n](O)\bigr).$$ Here $w$ is viewed as a point of $G^{\mathrm t}(O)$ when applying $j$. Define the $\mathbb Z_p$-linear map $\alpha_0:T\to\Omega(G^{\mathrm t})$ by $\alpha_0(t)=d\log\chi_t$. For $x\in\operatorname{Lie}_O(G^{\mathrm t})$, the comparison vector $b(x)\in V$ is the unique vector satisfying $$\langle b(x),1\otimes t\rangle_\varepsilon=\iota\bigl(\alpha_0(t)(x)\bigr)\qquad(t\in T).$$
