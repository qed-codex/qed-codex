---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/PositiveDefiniteness/PositiveDefiniteSecond.lean",
  "declarations": [
    "PI.DefPosDefWork.positive_definite_second"
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

## Definiteness at rational vectors gives definiteness at complex embeddings

[Theorem ANT.0529](https://andrewodesky.com/rh/lean/PI.DefPosDefWork.positive_definite_second/)

Let $F$ be a totally real number field and $E$ a number field over $F$. Let $\sigma:E\to E$ be an $F$-algebra homomorphism such that $$\tau(\sigma(x))=\overline{\tau(x)}\qquad(x\in E,\ \tau:E\hookrightarrow\mathbb C).$$ Let $k>0$ and $J\in M_k(E)$ satisfy $\sigma(J)^t=J$. Put $h(x,y)=\sigma(x)^tJy$. Assume that for every real embedding $\iota:F\hookrightarrow\mathbb R$, one of the following holds uniformly over $0\ne x\in E^k$: $h(x,x)$ is the image of some $a\in F$ with $\iota(a)>0$; or $h(x,x)$ is the image of some $a\in F$ with $\iota(a)<0$. Then, for every $\tau:E\hookrightarrow\mathbb C$, $$\tau(J)\text{ is positive definite}\quad\text{or}\quad-\tau(J)\text{ is positive definite}.$$
