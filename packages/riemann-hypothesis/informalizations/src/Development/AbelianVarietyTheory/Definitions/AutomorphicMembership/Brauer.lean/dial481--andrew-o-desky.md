---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/Brauer.lean",
  "declarations": [
    "GlobalTheory.Mem.LiteralAutomorphy.LitCoh"
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

## Local and global cohomological hypotheses

[Definition / hypothesis GC.D011](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)

The cohomological hypothesis is the conjunction of the following twelve assertions. Each assertion is required for every choice of the data it specifies. All Galois groups have their profinite topology, and cohomology with topological coefficients is continuous cohomology. For a set $X$, put $c(X)=|X|$ when $X$ is finite and $c(X)=0$ when $X$ is infinite.

**(1) Normalized global duality.** Require ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)).

**(2) Local finiteness.** Require condition (1) of ([Local cohomology conditions at finite primes](https://andrewodesky.com/rh/lean/ReciprocityTheory.Gal.LocalFiniteness/)).

**(3) Local duality.** Require condition (2) of ([Local cohomology conditions at finite primes](https://andrewodesky.com/rh/lean/ReciprocityTheory.Gal.LocalFiniteness/)).

**(4) ([Local Euler characteristic](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_euler/)).** Require condition (3) of ([Local cohomology conditions at finite primes](https://andrewodesky.com/rh/lean/ReciprocityTheory.Gal.LocalFiniteness/)).

For assertions (5), (6) and (8), let $F$ be a number field, $\Omega/F$ an algebraic closure, $\ell$ a prime, $r\ge1$ an integer, and $R=\mathbb Z/\ell^r\mathbb Z$. Let $S$ be a finite set of finite primes of $F$ containing every prime above $\ell$. Let $G_{F,S}$ be the Galois group of the maximal subextension of $\Omega/F$ unramified at finite primes outside $S$. Let $M$ be any finite discrete $R$-module with a continuous $G_{F,S}$-action.

**(5) Global finiteness.** The groups $H^i(G_{F,S},M)$ are finite for $i=0,1,2$. If $\ell\ne2$, then $H^n(G_{F,S},M)=0$ for every $n\ge3$.

For assertions (6) and (8), for each infinite place $w$, choose $c_w\in\operatorname{Gal}(\Omega/F)$ such that, when $w$ is real, there is an embedding $j:\Omega\hookrightarrow\mathbb C$ inducing $w$ on $F$ and satisfying $j(c_w x)=\overline{j(x)}$ for every $x\in\Omega$. Write $r_2(F)$ for the number of complex places and set $$A_\infty(M)=\left(\prod_{w\text{ real}}|M^{c_w}|\right)|M|^{r_2(F)},$$ where $c_w$ acts on $M$ through its image in $G_{F,S}$.

**(6) Global Euler characteristic.** For every choice of the $c_w$ just described, $$c(H^0(G_{F,S},M))\,c(H^2(G_{F,S},M))\,|M|^{[F:\mathbb Q]} =c(H^1(G_{F,S},M))\,A_\infty(M).$$

**(7) Unramified local conditions.** Let $F,\Omega,\ell,r,R$ be as above, let $v$ be a finite prime with $v\nmid\ell$, and choose a valuation ring $A\subseteq\Omega$ above $v$. Write $D$ and $I$ for its decomposition and inertia groups. Let $M$ be any finite discrete $R$-module with continuous $D$-action on which $I$ acts trivially. Put $M'=\operatorname{Hom}_R(M,R)(1)$, with its contragredient and cyclotomic actions, and define $$H^1_{\rm ur}(D,M)=\ker\bigl(H^1(D,M)\longrightarrow H^1(I,M)\bigr),$$ and similarly for $M'$. Under the dual-first cup product $$H^1(D,M')\times H^1(D,M)\longrightarrow H^2(D,R(1)),\qquad (y,x)\longmapsto y\smile x,$$ using evaluation $(\varphi,m)\mapsto\varphi(m)$, the submodules $H^1_{\rm ur}(D,M')$ and $H^1_{\rm ur}(D,M)$ are each the full annihilator of the other.

**(8) Greenberg–Wiles identity.** In the global setting above, assume $\ell\ne2$. Choose a character $\mu:G_{F,S}\to R^\times$ whose pullback to $\operatorname{Gal}(\Omega/F)$ is the cyclotomic character modulo $\ell^r$, and put $M'=\operatorname{Hom}_R(M,R)$ with action $(g\varphi)(m)=\mu(g)\varphi(g^{-1}m)$. Choose a valuation ring $A_v$ above every $v\in S$, and let $D_v$ be its decomposition group. Write $M_v,M'_v$ for the restricted modules. Choose arbitrary $R$-submodules $L_v\subseteq H^1(D_v,M_v)$ and define $$L_v^\perp=\{y\in H^1(D_v,M'_v):y\smile x=0\text{ for every }x\in L_v\},$$ with the same dual-first evaluation cup product as in (7). Define $$\operatorname{Sel}_L(M)=\{x\in H^1(G_{F,S},M):\operatorname{res}_v x\in L_v\text{ for every }v\in S\},$$ and define $\operatorname{Sel}_{L^\perp}(M')$ in the same way. For all these choices, and every choice of the $c_w$ above, $$\begin{aligned} c(\operatorname{Sel}_L(M))\,c(H^0(G_{F,S},M')) \left(\prod_{v\in S}c(H^0(D_v,M_v))\right)A_\infty(M) &=c(\operatorname{Sel}_{L^\perp}(M'))\,c(H^0(G_{F,S},M)) \prod_{v\in S}c(L_v). \end{aligned}$$

**(9) Finiteness over finite local extensions.** Require the assertion of ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)) for every prime $\ell$ and every finite extension $K/\mathbb Q_\ell$ inside the chosen algebraic closure, with finite discrete coefficients.

**(10) Duality over finite local extensions.** Require the assertion of ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)) for every such $\ell,K$ and finite discrete coefficient module.

**(11) Euler characteristic over finite local extensions.** Require the assertion of ([Local Euler characteristic](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_euler/)) for every such $\ell,K$ and finite discrete coefficient module.

**(12) Local finite-cohomology conditions.** For every prime $\ell$, make any choice satisfying Hypothesis (local period data) in ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)), and let $K/\mathbb Q_\ell$ be any finite subextension of the chosen algebraic closure. Use its rings $B,D$, filtration and cyclotomic character. All representations in this assertion are finite-dimensional continuous $\mathbb Q_\ell$-linear representations of $G_K$, with their finite-dimensional vector-space topologies. Use the de Rham condition and $D_{\rm dR}(V)$ defined in that entry. Put $$\operatorname{Fil}^0(V\otimes D)=\operatorname{im}\bigl(V\otimes_{\mathbb Q_\ell}\operatorname{Fil}_K^0D\longrightarrow V\otimes_{\mathbb Q_\ell}D\bigr).$$ A continuous $1$-cocycle $a:G_K\to V$ is *finite* if there is $z\in V\otimes_{\mathbb Q_\ell}B$ such that $$a(g)\otimes1=gz-z\qquad(g\in G_K).$$ Let $Z_f^1(V)$ be the space of these cocycles, and let $H_f^1(V)$ be its quotient by the coboundaries $g\mapsto gv-v$.

(a) If $V$ is de Rham, then $H_f^1(V)$ is finite-dimensional and $$\dim_{\mathbb Q_\ell}H_f^1(V)=\dim_{\mathbb Q_\ell}V^{G_K} +\dim_{\mathbb Q_\ell}D_{\rm dR}(V) -\dim_{\mathbb Q_\ell}\bigl(D_{\rm dR}(V)\cap\operatorname{Fil}^0(V\otimes D)\bigr).$$

(b) Let $V'$ be a second such representation, let $V$ be de Rham, and let $P:V\times V'\to\mathbb Q_\ell$ be a bilinear pairing of equal-dimensional spaces, nondegenerate in both variables, satisfying $$P(gx,gy)=\chi_\ell(g)P(x,y).$$ For continuous cocycles $a:G_K\to V$ and $b:G_K\to V'$, put $$(a\smile_P b)(g,h)=P(a(g),g b(h)).$$ Say that this cup product is a continuous coboundary if there is a continuous $f:G_K\to\mathbb Q_\ell$ with $$(a\smile_P b)(g,h)=\chi_\ell(g)f(h)-f(gh)+f(g).$$ Then $a$ is finite if and only if $a\smile_P b$ is a continuous coboundary for every finite $b$, and $b$ is finite if and only if $a\smile_P b$ is a continuous coboundary for every finite $a$.

(c) In the setting of (b), let $T\subset V$ and $T'\subset V'$ be stable, finite free $\mathbb Z_\ell$-submodules spanning their ambient spaces, with $$T'=\{y\in V':P(T,y)\subseteq\mathbb Z_\ell\}.$$ Give $V'/T'$ the discrete topology. A locally constant $1$-cocycle $c:G_K\to V'/T'$ is called finite if $$c(g)=b(g)\bmod T'+gx-x\qquad(g\in G_K)$$ for some $b\in Z_f^1(V')$ and $x\in V'/T'$. A continuous $T$-valued cocycle is finite when it belongs to $Z_f^1(V)$.

For a continuous $T$-valued cocycle $d$ and a locally constant cocycle $c:G_K\to V'/T'$, define $$z_{d,c}(g,h)=P(d(g),g\widetilde c(h))\bmod\mathbb Z_\ell\in(\mathbb Q_\ell/\mathbb Z_\ell)(1),$$ where $\widetilde c(h)\in V'$ is any representative of $c(h)$. The dual-lattice condition makes this expression independent of that representative. Say that $z_{d,c}$ is a coboundary if there is a locally constant $f:G_K\to\mathbb Q_\ell/\mathbb Z_\ell$ with $$z_{d,c}(g,h)=\chi_\ell(g)f(h)-f(gh)+f(g).$$ Then $c$ is finite if and only if $z_{d,c}$ is a coboundary for every finite $T$-valued cocycle $d$. Also, $d$ is finite if and only if $z_{d,c}$ is a coboundary for every finite locally constant cocycle $c:G_K\to V'/T'$.
