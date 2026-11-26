---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/ExistsPrimitiveRootPow.lean",
  "declarations": [
    "GlobalTheory.Published.PoitouTateDuality"
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

## Normalized Poitou–Tate duality for finite Galois modules

[Definition / hypothesis GC.D065](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)

The normalized Poitou–Tate condition is the following assertion. Let $F$ be any number field, $\Omega/F$ an algebraic closure, $\ell$ a prime, and $r\ge1$. Assume $\ell\ne2$ or $F$ is totally complex, and choose a primitive $\ell^r$th root of unity $\zeta\in\Omega$. Put $R=\mathbb Z/\ell^r\mathbb Z$ and $G_F=\operatorname{Gal}(\Omega/F)$. Write $R(1)$ for the discrete module $R$ on which $G_F$ acts through the cyclotomic character modulo $\ell^r$.

For a valuation ring $A\subseteq\Omega$, let $D_A=\{g\in G_F:g(A)=A\}$, with its profinite topology. There is a family of $R$-linear maps $$\operatorname{inv}_A:H^2(D_A,R(1))\longrightarrow R,$$ indexed by all such $A$. At every $A$ above a finite prime of $F$, this map is bijective and has the normalization in ([A normalized local second-cohomology isomorphism](https://andrewodesky.com/rh/lean/GlobalTheory.T.normalised_local_invariant_exists/)), with the chosen root $\zeta$. All cohomology groups below are continuous group cohomology groups.

**(1) Compatibility under automorphisms.** Let $\sigma$ be a field automorphism of $\Omega$ with $\sigma(F)=F$, and let $c\in R$ satisfy $\sigma(\zeta)=\zeta^c$, where the exponent may be any integer representative of $c$. For $A$ above a finite prime, put $A'=\sigma(A)$. If continuous $2$-cocycles $z$ on $D_A$ and $z'$ on $D_{A'}$, with coefficients in $R(1)$, satisfy $$z'(\sigma g\sigma^{-1},\sigma h\sigma^{-1})=c\,z(g,h)\qquad(g,h\in D_A),$$ then $$\operatorname{inv}_{A'}([z'])=\operatorname{inv}_A([z]).$$

The same family of maps has the following properties for every choice of the data below. Let $S$ be a finite set of finite primes of $F$ containing all primes above $\ell$, and choose a valuation ring $A_v$ of $\Omega$ above each $v\in S$. Put $D_v=D_{A_v}$. Let $G_{F,S}$ be the Galois group of the maximal subextension of $\Omega/F$ unramified at finite primes outside $S$, with its profinite topology. Choose a character $\mu:G_{F,S}\to R^\times$ whose pullback to $G_F$ is the cyclotomic character modulo $\ell^r$.

Let $M$ be any finite discrete $R$-module with a continuous $G_{F,S}$-action. Its twisted dual is the discrete module $$M'=\operatorname{Hom}_R(M,R),\qquad (g\varphi)(m)=\mu(g)\varphi(g^{-1}m).$$ For either coefficient module, write $$H^i(M)=H^i(G_{F,S},M),\qquad P^i(M)=\prod_{v\in S}H^i(D_v,M),$$ where local actions are obtained through $D_v\to G_{F,S}$. Let $\operatorname{loc}_i:H^i(M)\to P^i(M)$ be restriction, and write $X^*=\operatorname{Hom}_R(X,R)$ for the $R$-linear dual of an $R$-module $X$.

**(2) The nine-term sequence.** Define $R$-linear maps $t_i:P^i(M)\to H^{2-i}(M')^*$ by $$\begin{aligned} t_0(x)(y)&=\sum_{v\in S}\operatorname{inv}_{A_v}(x_v\smile\operatorname{res}_v y),\\ t_1(x)(y)&=\sum_{v\in S}\operatorname{inv}_{A_v}(\operatorname{res}_v y\smile x_v),\\ t_2(x)(y)&=\sum_{v\in S}\operatorname{inv}_{A_v}(x_v\smile\operatorname{res}_v y). \end{aligned}$$ The maps $t_0,t_2$ use the evaluation pairing $(m,\varphi)\mapsto\varphi(m)$; $t_1$ uses $(\varphi,m)\mapsto\varphi(m)$. There are $R$-linear maps $\delta_1,\delta_2$ making the sequence $$\begin{aligned} 0&\longrightarrow H^0(M)\xrightarrow{\operatorname{loc}_0}P^0(M)\xrightarrow{t_0}H^2(M')^*\\ &\xrightarrow{\delta_1}H^1(M)\xrightarrow{\operatorname{loc}_1}P^1(M)\xrightarrow{t_1}H^1(M')^*\\ &\xrightarrow{\delta_2}H^2(M)\xrightarrow{\operatorname{loc}_2}P^2(M)\xrightarrow{t_2}H^0(M')^*\longrightarrow0 \end{aligned}$$ exact. The maps $\delta_1,\delta_2$ may depend on $S$, the chosen valuation rings, $\mu$, and the module with its action.

**(3) Finite localization-kernel dualities.** For $i=1,2$, define $$\operatorname{Sha}^i_S(M)=\ker\bigl(\operatorname{loc}_i:H^i(M)\to P^i(M)\bigr),$$ and define $\operatorname{Sha}^i_S(M')$ in the same way. All four groups are finite, and there are $R$-linear isomorphisms $$\operatorname{Sha}^2_S(M)\simeq\operatorname{Sha}^1_S(M')^*,\qquad\operatorname{Sha}^2_S(M')\simeq\operatorname{Sha}^1_S(M)^*.$$ Their cardinalities satisfy $$\#\operatorname{Sha}^2_S(M)=\#\operatorname{Sha}^1_S(M'),\qquad\#\operatorname{Sha}^2_S(M')=\#\operatorname{Sha}^1_S(M).$$

**(4) Higher cohomology.** For every $n\ge3$, $$H^n(G_{F,S},M)=0.$$
