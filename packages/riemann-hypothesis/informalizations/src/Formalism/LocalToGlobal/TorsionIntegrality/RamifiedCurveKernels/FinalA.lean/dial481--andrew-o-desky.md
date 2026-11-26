---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/RamifiedCurveKernels/FinalA.lean",
  "declarations": [
    "Formalism.L2.Th1.G.eigenSplit"
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

## Separating matrix entries by character values

[Theorem PHT.1078](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.G.eigenSplit/)

Let $K$ be an ultrametric normed field, $I,T,X$ sets, $\tau:I\to T$, $p:T\to T$, $B=(B_{ij})\in K^{I\times I}$, $\theta\in K^\times$, and $\chi,\chi':X\times T\to K$. Suppose $$|B_{ij}|\le1,\qquad |(\chi(x,\tau(i))-\chi'(x,\tau(j)))B_{ij}|\le|\theta|$$ for every $x,i,j$. Assume that whenever $\rho\ne p(\alpha)$, there is $x\in X$ with $|\chi(x,\alpha)-\chi'(x,\rho)|=1$. There is $Q\in K^{I\times I}$ with $|Q_{ij}|\le1$ and $$B_{ij}=\begin{cases}B_{ij}&\tau(j)=p(\tau(i)),\\0&\tau(j)\ne p(\tau(i))\end{cases}+\theta Q_{ij}.$$
