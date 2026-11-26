---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFramesFockMapPolynomialLieActionsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_frames_fockMap_polynomial_lie_actions"
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

## Polynomial Lie actions in the archimedean Weil model

[Theorem THETA.1680](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_frames_fockMap_polynomial_lie_actions/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$. Let $X,W$ have dimensions $n,d\ge0$ with nonsingular matrices $J_X,J_W$ satisfying $\sigma(J_X^t)=J_X$ and $\sigma(J_W^t)=-J_W$. Fix the source's Schrödinger model $M$, a standard adelic additive character $\psi$, circle-valued splitting characters $\chi_X,\chi_W$, and a Weil representation $\omega$ in that model. Standard means that $\psi$ is continuous, trivial on $F$, and has the prescribed archimedean exponential $e^{-2\pi i\operatorname{Tr}_{F\otimes\mathbb R/\mathbb R}(x)}$. Choose embeddings $\tau_w:E\to\mathbb C$ above each infinite place of $F$, and assume the prescribed involutions of $X$ and $W$ are Cartan involutions for $\tau_w(J_X)$ and $i\tau_w(J_W)$.

There exist signatures $(P_w,Q_w)$ and $(R_w,S_w)$, signature frames $A_w,C_w$, constants $c_w,c'_w\in\mathbb C$, and an injective complex-linear map $$\Phi:\bigotimes_{w\mid\infty}\mathcal P_{P_w,Q_w,R_w,S_w}\longrightarrow\mathcal S_\infty(F^{nd})$$ whose image is exactly the polynomial subspace of $M$ for $\psi$ and $\tau$. The space $\mathcal P_{p,q,r,s}$ is the polynomial Fock space for signatures $(p,q)$ and $(r,s)$; the frames reduce the two forms to their signature matrices, using $J_X$ and $iJ_W$ respectively. For every permitted real one-parameter subgroup with framed infinitesimal generators $Y_w$, differentiation of the $X$-action gives $$d\omega_X(Y)\Phi(T)=\Phi\!\left(\sum_w\bigl(\mathcal L_{X,w}(Y_w)+c_w\operatorname{tr}(Y_w)\bigr)T\right),$$ and the $W$-action satisfies the same formula with $\mathcal L_{W,w}$ and $c'_w$. The operators $\mathcal L_{X,w},\mathcal L_{W,w}$ are the polynomial oscillator Lie actions of ([Commuting Lie actions with rational weights in a polynomial model](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockActions_lie_rationalWeights_commute/)) on the indicated Fock factors.
