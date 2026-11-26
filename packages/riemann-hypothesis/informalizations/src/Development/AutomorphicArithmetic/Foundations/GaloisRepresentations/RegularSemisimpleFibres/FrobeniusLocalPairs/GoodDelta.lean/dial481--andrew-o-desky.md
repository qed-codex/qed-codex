---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/FrobeniusLocalPairs/GoodDelta.lean",
  "declarations": [
    "UpperTheory.Gal.InertialTypesAlt.L.goodDelta"
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

## An integral norm root commuting with the centralizer

[Theorem REP.1287](https://andrewodesky.com/rh/lean/UpperTheory.Gal.InertialTypesAlt.L.goodDelta/)

Let $k$ be a characteristic-zero nonarchimedean local field and $K/k$ a finite Galois extension of nonarchimedean local fields, with compatible valuations. Let $F_0\subseteq F_1$ be finite fields, let $d=[K:k]=[F_1:F_0]$, and fix surjective homomorphisms $r_k:\mathcal O_k\to F_0$, $r_K:\mathcal O_K\to F_1$. Suppose that $r_K$ restricts to $r_k$ through the given inclusions. Fix $s\in\operatorname{Gal}(K/k)$ and $\bar s\in\operatorname{Gal}(F_1/F_0)$ such that $r_K(sx)=\bar s(r_Kx)$ for $x\in\mathcal O_K$ and $\bar s(z)=z^{|F_0|}$.

Let $n\ge0$ and $\gamma\in\mathrm{GL}_n(k)$, with every coefficient of its characteristic polynomial in $\mathcal O_k$ and with $\det\gamma\in\mathcal O_k^\times$. There is $\delta\in\mathrm{GL}_n(K)$ such that $$\delta\,s(\delta)\cdots s^{d-1}(\delta)=\gamma,$$ $$x\gamma=\gamma x\Longrightarrow x\delta=\delta x\qquad(x\in\mathrm{GL}_n(K)),$$ and, for every $g\in\mathrm{GL}_n(K)$, $$g^{-1}\gamma g\in\mathrm{GL}_n(\mathcal O_K)\Longrightarrow g^{-1}\delta g\in\mathrm{GL}_n(\mathcal O_K).$$ Here $s$ acts on matrices entrywise and $\gamma$ on the right sides is extended from $k$ to $K$.
