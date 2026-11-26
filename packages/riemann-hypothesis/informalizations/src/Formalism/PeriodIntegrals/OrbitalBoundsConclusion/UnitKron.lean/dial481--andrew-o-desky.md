---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnitKron.lean",
  "declarations": [
    "unit_kronecker"
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

## Finite order of an integral isometry of a definite form

[Theorem ANT.0429](https://andrewodesky.com/rh/lean/unit_kronecker/)

Let $E$ be a number field and $c:E\to E$ a ring homomorphism such that $$\tau(c(x))=\overline{\tau(x)}\qquad(x\in E,\ \tau:E\hookrightarrow\mathbb C).$$ Let $k\ge0$ and $J,\gamma\in M_k(E)$. Suppose for every embedding $\tau$, either $\tau(J)$ or $-\tau(J)$ is positive definite. Assume $$c(\gamma)^tJ\gamma=J,$$ and every coefficient of the characteristic polynomial of $\gamma$ is integral over $\mathbb Z$. Then $\gamma^n=1$ for some integer $n\ge1$.
