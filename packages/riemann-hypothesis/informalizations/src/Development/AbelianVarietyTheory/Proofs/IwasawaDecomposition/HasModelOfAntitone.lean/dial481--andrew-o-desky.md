---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasModelOfAntitone.lean",
  "declarations": [
    "GlobalTheory.CompactDS.hasModel_of_antitone"
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

## A finite matrix model for an integral dominant weight

[Theorem REP.0191](https://andrewodesky.com/rh/lean/GlobalTheory.CompactDS.hasModel_of_antitone/)

Let $N\ge0$ and $L_1\ge\cdots\ge L_N$ be integers. There are a finite index set $I$, a map $\rho:M_N(\mathbb C)\to M_I(\mathbb C)$, weights $\mu_i\in\mathbb R^N$ for $i\in I$, and $v\in\mathbb C^I\setminus\{0\}$ such that $$\rho(1)=1,\quad\rho(gh)=\rho(g)\rho(h),\quad\rho(g^*)=\rho(g)^*,$$ and every matrix entry of $\rho$ is continuous on $U(N)$. For $\theta\in\mathbb R^N$, writing $t_\theta=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_N})$, $$\rho(t_\theta)=\operatorname{diag}_{i\in I}(e^{i\mu_i\cdot\theta}),\qquad \rho(t_\theta)v=e^{iL\cdot\theta}v.$$ Whenever $(\rho(g)v)_i\ne0$, the difference $L-\mu_i$ is a nonnegative integral combination of the roots $e_a-e_b$ with $a<b$.

**Hermitian realization.** Let $n\ge0$ and let $\nu_1\ge\cdots\ge\nu_n$ be integers. There are a finite-dimensional complex inner product space $U$, operators $E_{ab}\in\operatorname{End}_{\mathbb C}U$ for $1\le a,b\le n$, and a nonzero $u\in U$ such that $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb},\qquad E_{ab}^*=E_{ba},$$ $$E_{aa}u=\nu_a u,\qquad E_{ab}u=0\quad(a<b).$$
