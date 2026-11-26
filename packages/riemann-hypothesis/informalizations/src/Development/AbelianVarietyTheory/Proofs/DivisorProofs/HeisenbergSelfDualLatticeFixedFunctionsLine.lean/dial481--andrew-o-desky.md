---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeisenbergSelfDualLatticeFixedFunctionsLine.lean",
  "declarations": [
    "GlobalTheory.LatVacLine.vacuum_line"
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

## A one-dimensional Heisenberg eigenspace for a self-dual lattice

[Theorem THETA.1270](https://andrewodesky.com/rh/lean/GlobalTheory.LatVacLine.vacuum_line/)

Let $E/F$ be number fields with the admissible theta-triple conditions specified in ([Both lattice stabilizers fix an inert local vacuum](https://andrewodesky.com/rh/lean/GlobalTheory.T.inert_place_both_stabilisers_fix_vacuum/)): an $F$-linear endomorphism $\sigma$ of $E$, base data $B$ with additive character $\psi$, integers $a,a'\ge0$, Hermitian spaces $V,V'$ of ranks $a,a'$ and a skew-Hermitian space $W$ of rank $a+a'$, two splitting characters, and the two specified Weil representations. Fix a finite place $v$ of $F$ where the local additive character has annihilator exactly $\mathcal O_{F_v}$. Let $\Lambda$ be the tensor lattice in $M_{a,a+a'}(\mathbb A_E)$ supported at $v$, and assume $$z\in\Lambda\quad\Longleftrightarrow\quad\psi(B_{-1}(z,\gamma))=1\text{ for every }\gamma\in\Lambda$$ for every matrix $z$ supported at $v$. Here, with $J_V,J_W$ the two Gram matrices, $$B_t(x,y)=\operatorname{Tr}_{\mathbb A_E/\mathbb A_F}\!\left(t\sum_{i,j,k,l}x_{ij}(J_V)_{ik}(J_W)_{jl}\sigma(y_{kl})\right).$$ Choose $\theta\in\mathcal O_E$ with $\theta+\sigma(\theta)=1$. In the associated local Schrödinger model on the Schwartz–Bruhat functions on $F_v^{a(a+a')}$, let $\rho_\psi(\gamma)$ denote the Heisenberg operator in the specified Darboux coordinates. Suppose $\phi_0\ne0$ is Schwartz–Bruhat and $$\rho_\psi(\gamma)\phi_0=\psi\!\left(\tfrac12B_\theta(\gamma,\gamma)\right)\phi_0\qquad(\gamma\in\Lambda).$$ Every Schwartz–Bruhat $\phi$ satisfying the same eigenvalue equation is $c\phi_0$ for some $c\in\mathbb C$.
