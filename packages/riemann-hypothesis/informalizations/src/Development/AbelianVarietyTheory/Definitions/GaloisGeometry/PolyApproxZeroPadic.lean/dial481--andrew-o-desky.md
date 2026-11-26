---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/PolyApproxZeroPadic.lean",
  "declarations": [
    "GlobalTheory.Cong.PolyApprox"
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

## Systems of Hecke eigenvalues on a definite unitary group and their l-adic polynomial approximation

[Definition / hypothesis AGR.D280](https://andrewodesky.com/rh/lean/GlobalTheory.Cong.Levels/)

Throughout, $E$ is a CM field with maximal totally real subfield $E^+$, $\ell$ is a prime, $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ is an isomorphism of fields, $|\cdot|_\ell$ is the $\ell$-adic absolute value of $\overline{\mathbb Q}_\ell$, and $a\ge1$ is an integer. The definite unitary group $\mathcal U$ in $a$ variables over $E$, the representations of $GL_a(E_w)$ that occur in a space of functions on $\mathcal U$ at a finite place $w$, and Satake multisets are those of ([Satake multisets and weights of definite unitary forms](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.SatU/)); split places, the place $w^+$ of $E^+$ below $w$ and the multisets $R_w(B)$ are those of ([Special automorphic representations of a definite unitary group at two places above l](https://andrewodesky.com/rh/lean/GlobalTheory.CongL.FieldOK/)). This page defines the systems of Hecke eigenvalues of a space of functions on $\mathcal U$ and the approximation of one family of $\ell$-adic numbers by linear combinations of others.

**Level families.** A *level family* is a family $K=(K_w)$ of subgroups $K_w\subseteq GL_a(E_w)$, one for every finite place $w$ of $E$. Let $w_0$ and $v'$ be finite places of $E$, and let $U$ be a complex vector space of functions on $\mathcal U$. The space $U$ *has level $K$ away from $w_0$ and $v'$* if, for every split place $w$ of $E$ with $w^+\ne w_0^+$ and $w^+\ne v'^+$, every smooth irreducible representation $(\sigma,V)$ of $GL_a(E_w)$ that occurs in $U$ at $w$ has a nonzero vector fixed by $K_w$.

**Systems of Hecke operators.** Let $K$ be a level family. A *system of Hecke operators for $K$*, indexed by a set $J$, consists of the following for every $j\in J$:

- a split finite place $w_j$ of $E$ that does not divide $\ell$;
- a function $f_j\colon GL_a(E_{w_j})\to\mathbb C$ with finite support such that $|\iota^{-1}(f_j(g))|_\ell\le1$ for all $g$;
- a function $z_j$ that assigns a complex number $z_j(\sigma)$ to every smooth irreducible complex representation $(\sigma,V)$ of $GL_a(E_{w_j})$, such that $$\sum_{g}f_j(g)\,\sigma(g)v=z_j(\sigma)\,v\qquad\text{for every }v\in V\text{ fixed by }K_{w_j}.$$

The system is *rational* if every value $f_j(g)$ is a rational number.

**Systems of eigenvalues.** Let $U$ be a complex vector space of functions on $\mathcal U$. A family $\theta=(\theta_j)_{j\in J}$ of elements of $\overline{\mathbb Q}_\ell$ is a *system of eigenvalues of $U$* for a system of Hecke operators indexed by $J$ if $\theta_j=\iota^{-1}(z_j(\sigma))$ for every $j\in J$ and every smooth irreducible representation $\sigma$ of $GL_a(E_{w_j})$ that occurs in $U$ at $w_j$.

**Power sums of a Satake multiset.** For every complex vector space $U$ of functions on $\mathcal U$ and every finite place $w$ of $E$ at which $U$ has a Satake multiset, fix one Satake multiset $B(U,w)$ of $U$ at $w$. For an integer $n$, put $$s_n(U,w)=\sum_{z\in R_w(B(U,w))}z^{\,n}$$ if $U$ has a Satake multiset at $w$, and $s_n(U,w)=0$ otherwise.

**Polynomial approximation.** Let $I$ be a set, let $\eta\in\overline{\mathbb Q}_\ell^{\,I}$ and let $\mathcal S\subseteq\overline{\mathbb Q}_\ell^{\,I}$. The family $\eta$ is *polynomially approximated by $\mathcal S$* if, for every real number $\varepsilon>0$, there are a finite subset $\mathcal S_0\subseteq\mathcal S$ and coefficients $c_\xi\in\overline{\mathbb Q}_\ell$, $\xi\in\mathcal S_0$, such that $$\Bigl|P(\eta)-\sum_{\xi\in\mathcal S_0}c_\xi\,P(\xi)\Bigr|_\ell\le\varepsilon\qquad\text{for every }P\in\mathbb Z[X_i:i\in I].$$ The subset $\mathcal S_0$ and the coefficients depend on $\varepsilon$ and not on $P$.
