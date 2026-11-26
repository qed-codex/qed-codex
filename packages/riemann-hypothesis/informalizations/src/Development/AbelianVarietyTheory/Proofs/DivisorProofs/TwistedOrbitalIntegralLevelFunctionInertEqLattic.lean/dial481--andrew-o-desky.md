---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwistedOrbitalIntegralLevelFunctionInertEqLattic.lean",
  "declarations": [
    "GlobalTheory.TwOrbLevel.twOrb_level_eq_stSum"
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

## A twisted level sum as a Hermitian lattice count

[Theorem ANT.1484](https://andrewodesky.com/rh/lean/GlobalTheory.TwOrbLevel.twOrb_level_eq_stSum/)

Let $E/F$ be the CM extension of a CM field and its maximal real subfield, unramified at every finite place, and let $w$ be a nonsplit finite place of $E$. Fix the following local comparison datum: a complete discrete valuation ring $O$ with finite residue field of size $q^2$, fraction field $L$ of characteristic zero, and an involution $c$ preserving $O$ and acting nontrivially on its residue field. Choose an isomorphism $e:L\to E_w$ intertwining $c$ with the induced conjugation, carrying $O$ precisely to the valuation ring, preserving the normalized additive valuations, each assigned value zero at zero, and satisfying $Nw=q^2$.

Let $k\ge0$ and $t\in O\setminus\{0\}$ be fixed by $c$, lie in the maximal ideal and have valuation $k$. Let $A$ be a finite commutative $L$-algebra with compatible $O$-algebra structure, an involution $\sigma$ extending $c$, and an element $g\in A$. Put $u=1+tg$. Let $Q\in E_w[T]$ be monic, separable and of degree $m$, and suppose $$\overline{Q(0)}Q=\overline Q^{\mathrm{rev}},\quad L[u]=A,\quad Q^{e^{-1}}(u)=0,\quad\dim_LA=m,\quad u\sigma(u)=1.$$ Here the bar acts on coefficients, and the superscript denotes transport of coefficients by $e^{-1}$.

Put $K=\operatorname{GL}_m(O_{E_w})$, let $\theta(y)=\Phi\overline y^{-T}\Phi^{-1}$, where $\Phi_{ij}=(-1)^i$ when $i+j+1=m$ and is zero otherwise, with indices $0\le i,j<m$, put $N_\theta(y)=y\theta(y)$, and let $$K(k)=\{h\in K:v_w(h_{ij}-\delta_{ij})\ge k\text{ for all }i,j\},\qquad f_k(y)=1_{\{y\in K,\ N_\theta(y)\in K(k)\}}.$$ The $K$-normalized sum of twisted orbital terms with $\det(T-N_\theta(y))=Q$ equals the following rational lattice sum, viewed in $\mathbb C$.

For each class of $\sigma$-fixed units $a\in A^\times$ modulo $a\sim a\,b\sigma(b)$, let $\mathcal X_a$ be the finitely generated full $O$-lattices $\Lambda\subset A$ stable under multiplication by $g$ and self-dual for $H_a(x,y)=\operatorname{Tr}_{A/L}(ax\sigma(y))$. Put $T=\{b\in A^\times:b\sigma(b)=1\}$, let $T_0$ be its subgroup of units integral over $O$ with integral inverses, and sum over the $T$-orbits in $\mathcal X_a$. The equality is $$\mathcal O_Q^\theta(f_k) =\sum_{[a]}\sum_{[\Lambda]\in T\backslash\mathcal X_a} [T_0:T_0\cap\operatorname{Stab}_T(\Lambda)].$$
