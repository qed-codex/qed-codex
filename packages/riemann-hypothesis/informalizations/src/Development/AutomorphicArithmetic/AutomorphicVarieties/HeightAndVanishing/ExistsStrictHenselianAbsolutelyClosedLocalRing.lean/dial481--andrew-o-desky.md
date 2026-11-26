---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/ExistsStrictHenselianAbsolutelyClosedLocalRing.lean",
  "declarations": [
    "UpperTheory.V.HV.omT"
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

## The finite-order lift of the cyclotomic character

[Theorem ANT.1243](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.omT/)

Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell$ prime, and $\mathcal O\subseteq\overline{\mathbb Q}_\ell$ a $\mathbb Z_\ell$-subalgebra which is a discrete valuation ring and finite as a $\mathbb Z_\ell$-module. Write $G=\operatorname{Gal}(\Omega/\mathbb Q)$, $\mathfrak m$ for the maximal ideal of $\mathcal O$, $\chi_\ell:G\to\mathcal O^\times$ for the cyclotomic character, and $\overline\chi_\ell:G\to(\mathbb Z/\ell\mathbb Z)^\times$ for its reduction. There is exactly one character $\omega:G\to\mathcal O^\times$ such that $$\omega^{\ell-1}=1,\qquad\omega(g)\equiv\chi_\ell(g)\pmod{\mathfrak m}\quad(g\in G).$$ Its kernel is open and equals both $\ker\overline\chi_\ell$ and the kernel of the action on $\ell$th roots of unity, and its order is $\ell-1$. If $\ell\ne2$, then $\omega(c)=-1$ for every complex conjugation $c$. For a valuation subring $A$ of $\Omega$ with inertia group $I_A$, if $|\ell|_A\not<1$ then $I_A\subseteq\ker\omega$; if $|\ell|_A<1$, then $I_A\subseteq\ker(\omega^j)$ implies $\ell-1\mid j$ for every $j\ge0$. Every character $\theta:G\to\mathcal O^\times$ trivial on $\ker\omega$ is $\omega^b$ for some $0\le b<\ell-1$.
