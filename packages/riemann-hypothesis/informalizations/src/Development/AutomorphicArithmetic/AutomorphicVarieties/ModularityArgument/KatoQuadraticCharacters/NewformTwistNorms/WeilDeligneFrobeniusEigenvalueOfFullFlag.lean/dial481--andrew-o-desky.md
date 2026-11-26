---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/NewformTwistNorms/WeilDeligneFrobeniusEigenvalueOfFullFlag.lean",
  "declarations": [
    "GlobalTheory.T.weilDeligne_frobenius_eigenvalue_of_full_flag"
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

## Frobenius eigenvalues from a local full flag

[Theorem PHT.1250](https://andrewodesky.com/rh/lean/GlobalTheory.T.weilDeligne_frobenius_eigenvalue_of_full_flag/)

Let $F$ be a number field, $\Omega$ an algebraic closure, $\ell$ prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism, $n\ge0$, $M\ge1$, and $m_1,\ldots,m_n\in\mathbb Z$. Let $r:\operatorname{Gal}(\Omega/F)\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ be continuous. Choose a finite prime $w$, a valuation subring $A$ above $w$, and its decomposition group $D_A$. Choose a commutative topological $\mathbb Z_\ell$-algebra $\mathcal O$, a local comparison bridge for $D_A$ over $\mathcal O$ inducing the valuation ring $A$ in the sense specified in ([A Fontaine parameter is independent of the local comparison datum](https://andrewodesky.com/rh/lean/GlobalTheory.T.fontaineParameter_independent_of_localEmbedding/)), and suppose $r|_{D_A}$ is potentially semistable for this bridge and the period-ring system of ([Crystallinity of a codimension-one extension and a period coboundary](https://andrewodesky.com/rh/lean/GlobalTheory.CrysExtCrit.coboundary_iff_isCrys/)). Denote the resulting complex Weil–Deligne parameter by $\operatorname{WD}(r)$.

Suppose $r|_{D_A}$ has a full stable flag with character quotients $\kappa_i:D_A\to\overline{\mathbb Q}_\ell^\times$. Assume there are global characters $\chi_i:\operatorname{Gal}(\Omega/F)\to\overline{\mathbb Q}_\ell^\times$, trivial on every automorphism fixing all $M$th roots of unity, such that $\kappa_i|_{I_A}=\chi_{\mathrm{cyc}}^{m_i}\chi_i|_{I_A}$. For every Weil-group element $\varphi$ of degree one, and every $1\le i\le n$, $$(Nw)^{m_i}\,\iota\!\left(\kappa_i(\varphi)\chi_{\mathrm{cyc}}(\varphi)^{-m_i}\right)$$ is a root of the characteristic polynomial of $\operatorname{WD}(r)(\varphi)$.
