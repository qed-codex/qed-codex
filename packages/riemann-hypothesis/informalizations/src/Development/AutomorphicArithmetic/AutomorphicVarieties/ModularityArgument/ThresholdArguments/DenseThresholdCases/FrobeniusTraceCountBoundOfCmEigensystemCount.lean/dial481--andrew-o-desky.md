---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FrobeniusTraceCountBoundOfCmEigensystemCount.lean",
  "declarations": [
    "UpperTheory.GalN.V.Win.N.frobenius_trace_count_bound_of_cm_eigensystem_count_alt"
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

## Polynomially many labels for inverse-Frobenius traces

[Theorem AGR.1173](https://andrewodesky.com/rh/lean/UpperTheory.GalN.V.Win.N.frobenius_trace_count_bound_of_cm_eigensystem_count_alt/)

Assume the source's uniform CM eigensystem counting hypothesis. For every CM field $K$, there are integers $c,A\ge0$ such that, whenever $e,N\ge1$, $p$ is prime, and $w\mid p$ is a finite place of $K$ with $p\nmid N\operatorname{disc}K$, there exist a finite set $S$ and labels $t:S\to\mathbb C$ satisfying, with $q=Nw$, $$\#S\le c\bigl(N(e+1)\bigr)^A,\qquad |t(s)|\le\sqrt q+2,\qquad q^et(s)\text{ is integral over }\mathbb Z.$$ For every field automorphism $\alpha$ of $\mathbb C$, some permutation $u$ of $S$ satisfies $t(u(s))=\alpha(t(s))$ for all $s$.

These same data work for every prime $\ell\ne2,p$, algebraic closure $\Omega$ of $K$, field isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, valuation ring of $\Omega$ over $w$, and Frobenius element $\sigma$ for it. Let $\mathcal R$ be the source's class of irreducible three-dimensional representations $\rho$ of $G_K$ whose cyclotomic twist $\rho\otimes\chi_\ell^{-1}$ is automorphic conjugate-self-dual, which satisfy the level-$N$ local conditions of weights $(e,0,-e)$ and the prescribed alternative local condition at every place above $\ell$. There is a map $\operatorname{cl}:\mathcal R\to S$ such that $$\operatorname{cl}(\rho)=\operatorname{cl}(\rho')\Longrightarrow\rho\simeq\rho',\qquad \operatorname{tr}\rho(\sigma^{-1})=\iota^{-1}(t(\operatorname{cl}(\rho))).$$
