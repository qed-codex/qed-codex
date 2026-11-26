---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/UnipotentIntegralsPureTensorVanishOfLocalStatement.lean",
  "declarations": [
    "GlobalTheory.T.unipotentIntegrals_pureTensor_vanish_of_local"
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

## A local vanishing condition kills all adelic unipotent integrals

[Theorem REP.0658](https://andrewodesky.com/rh/lean/GlobalTheory.T.unipotentIntegrals_pureTensor_vanish_of_local/)

Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)), a Hermitian space $V$, and an isotropic flag with unipotent group $N$. Let $f_\infty$ be an archimedean family in the archimedean test spaces specified below, and let $(f_v)$ be a finite-place test family, with the prescribed standard factors at almost every place. Let $f=f_\infty\otimes\bigotimes_v f_v$ be the resulting function on $U(V)(\mathbb A_F)$.

Suppose there is a finite place $v$ such that, for every Haar measure $dn_v$ on $N(F_v)$ and all $x_v,y_v\in U(V)(F_v)$, $$\int_{N(F_v)}f_v(x_vn_vy_v)\,dn_v=0.$$ Then, for every Haar measure $dn$ on $N(\mathbb A_F)$ and all $x,y\in U(V)(\mathbb A_F)$, the function $n\mapsto f(xny)$ is integrable and $$\int_{N(\mathbb A_F)}f(xny)\,dn=0.$$
