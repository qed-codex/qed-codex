---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SemisimpleLevels/FlagPol.lean",
  "declarations": [
    "UpperTheory.V.Lev.flagPol"
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

## Weil characters supplied by a potentially semistable full flag

[Theorem PHT.0433](https://andrewodesky.com/rh/lean/UpperTheory.V.Lev.flagPol/)

Let $F$ be a number field with algebraic closure $\Omega$, let $\ell$ be prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, $n\ge0$, $M\ge1$, and $m_1,\ldots,m_n\in\mathbb Z$. Let $r:G_F\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ be continuous. Fix a finite prime $w$, a valuation subring $A\subset\Omega$ above $w$, a commutative topological $\mathbb Z_\ell$-algebra $O$, and an inducing local comparison bridge over $O$. Suppose $r|_{D_A}$ is potentially semistable for this bridge and the source's fixed period system.

Suppose $r|_{D_A}$ has a full stable flag with quotient characters $\kappa_i:D_A\to\overline{\mathbb Q}_\ell^\times$. Assume there are global characters $\chi_i:G_F\to\overline{\mathbb Q}_\ell^\times$, trivial on every automorphism fixing all $M$th roots of unity, with $$\kappa_i|_{I_A}=\chi_{\mathrm{cyc}}^{m_i}\chi_i|_{I_A}.$$ There are characters $\mu_i:W_A\to\mathbb C^\times$ such that $$\det(X-\operatorname{WD}(r)(s))=\prod_{i=1}^n(X-\mu_i(s))\qquad(s\in W_A).$$ For $s\in I_A$ fixing all $M$th roots of unity, every $\mu_i(s)=1$. If $$\mu_i(s)=(Nw)^{\deg s}\mu_j(s)\qquad\text{for all }s\in W_A,$$ then $\kappa_i=\kappa_j\chi_{\mathrm{cyc}}|_{D_A}$ or $\kappa_j=\kappa_i\chi_{\mathrm{cyc}}|_{D_A}$.
