---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelNormSqModerateGrowthLarge.lean",
  "declarations": [
    "GlobalTheory.Core.Rk.IP.normSq_theta_modGrowth_big"
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

## Moderate growth of the squared norm of a theta kernel

[Theorem THETA.0951](https://andrewodesky.com/rh/lean/GlobalTheory.Core.Rk.IP.normSq_theta_modGrowth_big/)

Assume the source's unitary Siegel–Weil and Siegel Eisenstein continuation packages. Fix its global arithmetic datum over $E/F$, Hermitian spaces $A,B$, an additive character $\psi$, a family of infinite embeddings $\theta$, splitting characters $\chi_A,\chi_B$, Cartan involutions $s_A,s_B$, an integer $t$, and a Cartan frame $c_A$ satisfying $$1\le\dim A,\quad1\le t,\quad\dim B=\dim A+t,\quad\dim A<t,\quad w(B)=0\text{ or }w(B)<t.$$ Here $w(B)$ is the Witt index, the assigned signatures of $A$ agree with its form, and $c_As_A=\Delta_Ac_A$ at infinity, with $\Delta_A$ the signature matrix. Choose a majorant $a\in\operatorname{GL}_{\dim A}(\mathbb A_E)$ normalized at every infinite place by $$a^*(G_As_A)a=1,$$ where $G_A$ is the Gram matrix in the chosen basis. Let $\omega$ be compatible Weil data for $(\psi,A,B,\chi_A,\chi_B)$, and let $\nu$ and $\mathcal F$ give the rational additive lattice in the oscillator space a measurable fundamental domain of volume one.

For any Haar measure $\mu$ on $U(B)(\mathbb A_F)$ and any theta test function $\Phi$ killed by every sufficiently long word of archimedean annihilation operators determined by $s_A,s_B$, the function $h\mapsto\Theta_\Phi(g,h)$ lies in $L^2(U(B)(F)\backslash U(B)(\mathbb A_F))$ for every $g$. Moreover there are $C\in\mathbb R$ and $N\ge0$ such that $$\left|\langle\Theta_\Phi(g,\cdot),\Theta_\Phi(g,\cdot)\rangle_{B,\mu}\right|\le C\,H_A(g)^N\qquad(g\in U(A)(\mathbb A_F)).$$
