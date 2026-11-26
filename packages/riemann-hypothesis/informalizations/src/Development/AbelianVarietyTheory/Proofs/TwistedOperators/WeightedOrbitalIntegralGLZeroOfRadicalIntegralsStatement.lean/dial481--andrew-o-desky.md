---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/WeightedOrbitalIntegralGLZeroOfRadicalIntegralsStatement.lean",
  "declarations": [
    "GlobalTheory.T.weightedOrbitalIntegral_GL_zero_of_radical_integrals"
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

## Vanishing of a weighted orbital integral from radical averages

[Theorem REP.0855](https://andrewodesky.com/rh/lean/GlobalTheory.T.weightedOrbitalIntegral_GL_zero_of_radical_integrals/)

Let $k$ be a nonarchimedean local field, $r\ge0$, $G=\operatorname{GL}_r(k)$ with its Borel sigma-algebra, and $dg$ a Haar measure. Let $\epsilon\in M_r(k)$ satisfy $\epsilon^2=\epsilon$, and put $$N=\{g\in G:\epsilon(g-I)(I-\epsilon)=g-I\}.$$ Let $f:G\to\mathbb C$ be continuous with compact support, and suppose that for every Haar measure $du$ on $N$ and all $x,y\in G$, $$\int_N f(xuy)\,du=0.$$ Let $\gamma\in G$ have separable characteristic polynomial and commute with $\epsilon$, and put $T=Z_G(\gamma)$. If $b:G\to\mathbb C$ is continuous and invariant under left translation by both $T$ and $N$, then, for every Haar measure $dt$ on $T$, the function $$Tx\longmapsto b(x)f(x^{-1}\gamma x)$$ is integrable on $T\backslash G$ and $$\int_{T\backslash G}b(x)f(x^{-1}\gamma x)\,d\dot x=0.$$
