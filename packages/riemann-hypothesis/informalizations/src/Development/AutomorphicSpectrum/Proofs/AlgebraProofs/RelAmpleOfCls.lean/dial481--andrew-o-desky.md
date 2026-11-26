---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/RelAmpleOfCls.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Hypotheses₂.Zarhin.SymB.symmetricBundle"
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

## A symmetric line bundle representing a principal polarization

[Theorem AV.1729](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.Zarhin.SymB.symmetricBundle/)

Assume the source's dual-abelian-scheme and theorem-of-the-cube packages. Let $C$ be an algebraically closed field, $v:C\to\mathbb R_{\ge0}$ a valuation, and $R$ a commutative ring with an injective map $R\to C$ identifying $R$ with $\{x\in C:v(x)\le1\}$. Let $A/\operatorname{Spec}R$ be an abelian scheme and $c\in\operatorname{Pic}(A\times_R A)$ a class giving a principal polarization in the sense stated in the conventions.

There is a relatively ample line bundle $L$ on $A$, trivialized along the identity section and symmetric locally over the base, such that $$c=[m^*L\otimes p_1^*L^{-1}\otimes p_2^*L^{-1}],$$ where $m$ is addition and $p_1,p_2$ are the projections. Its translation kernel is trivial: after any affine base change $T\to\operatorname{Spec}R$, if $x\in A(T)$ has $t_x^*L\otimes L^{-1}$ trivial locally on $T$, then $x=0$.
