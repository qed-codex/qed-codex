---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/ExtDim.lean",
  "declarations": [
    "UpperTheory.Zero.LLC.extDim"
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

## Dimension and central character under Langlands extension

[Theorem REP.1689](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.extDim/)

Let $E$ be a number field, $\Omega/E$ an algebraic closure, $A$ a valuation ring of $\Omega$ above a finite place $w$, and $a:W_w\to E_w^\times$ a local Artin homomorphism. Let $r$ and $r_c$ assign complex Weil–Deligne parameters to irreducible smooth representations of all $\operatorname{GL}_n(E_w)$. Assume the source's cuspidal-parameter laws for $r$, and assume that $r_c$ extends $r$ by taking the direct sum of the parameters attached to the segments of any Langlands presentation.

For every irreducible $\pi$ of $\operatorname{GL}_n(E_w)$, the parameter $r_c(\pi)$ has dimension $n$, and there is a cuspidal support multiset $S$ for which $$\det(T-r_c(\pi)(\gamma))=\prod_{\tau\in S}\det(T-r(\tau)(\gamma))\qquad(\gamma\in W_w).$$ For every central character $\omega_\pi$, $$|\det r_c(\pi)(\gamma)|=|\omega_\pi(a(\gamma))|.$$ The determinants themselves are equal if $\pi$ has a cuspidal support whose members either have rank one or are character twists of representations with nonzero first principal-congruence invariants over a field continuously isomorphic to some $\mathbb Q_p$.
