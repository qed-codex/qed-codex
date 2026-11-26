---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/ArchimedeanPrincipalSeries.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.ArchPI.exists_isPIProj_UJ"
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

## A nonzero projection with a polynomial identity in a unitary representation

[Theorem REP.1561](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.ArchPI.exists_isPIProj_UJ/)

Let $n\ge0$, let $\varepsilon_i\in\{\pm1\}$, and put $G=U(\operatorname{diag}(\varepsilon_i))$. Let $\rho$ be a strongly continuous representation of $G$ on a nonzero complex Hilbert space $H$, with every $\rho(g)$ an isometry. There is a nonzero bounded complex-linear operator $P$ such that $$P^2=P,\qquad \langle Pu,w\rangle=\langle u,Pw\rangle,$$ and every bounded operator commuting with all $\rho(g)$ commutes with $P$. Moreover, for some $M\ge0$ and every $g_1,\ldots,g_M\in G$, $$\sum_{\sigma\in S_M}\operatorname{sgn}(\sigma)\, P\rho(g_{\sigma(1)})P\rho(g_{\sigma(2)})P\cdots P\rho(g_{\sigma(M)})P=0.$$ For $M=0$ the product in this formula is $P$.
