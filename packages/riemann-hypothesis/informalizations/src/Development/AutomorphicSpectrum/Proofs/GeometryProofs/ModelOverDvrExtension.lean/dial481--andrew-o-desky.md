---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/ModelOverDvrExtension.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Num.model_baseChange_algebraic"
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

## Algebraic base change of a multihomogeneous point ideal

[Theorem AG.0279](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Num.model_baseChange_algebraic/)

Let $O$ be a discrete valuation domain, $\Omega$ a characteristic-zero field containing $O$, and suppose $O$ is integrally closed in $\Omega$. Let $K$ be a finite set, $J_k$ finite coordinate sets, $y=(y_{k,j})\in\Omega^{\bigsqcup_kJ_k}$, and $d\ge0$. Define $$P_O(y)=\ker\bigl(O[X_{k,j}]\longrightarrow\Omega[T_k:k\in K],\ X_{k,j}\mapsto y_{k,j}T_k\bigr).$$ Suppose $P_O(y)$ is a relevant multihomogeneous prime, its intersection with $O$ is zero, and $$\dim O[X]/P_O(y)=d+1+|K|.$$ Let $O'$ be a discrete valuation domain algebraic over $O$ with local structure homomorphism $O\to O'$. Let $\Omega'$ be a field containing both $\Omega$ and $O'$, with compatible $O$-algebra structures and injective map $O'\to\Omega'$. Then $$P_{O'}(y)=P_O(y)\,O'[X],$$ and $P_{O'}(y)$ has the same three properties, including dimension $d+1+|K|$.
