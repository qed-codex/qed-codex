---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/RowSeparationByRealFunctionalsOfChainStepsStatement.lean",
  "declarations": [
    "GlobalTheory.T.rowSeparation_by_realFunctionals_of_chain_steps"
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

## Detection of nonzero automorphic maps by theta periods

[Theorem THETA.1700](https://andrewodesky.com/rh/lean/GlobalTheory.T.rowSeparation_by_realFunctionals_of_chain_steps/)

Assume the source's six global principles: its size conditions imply the required cuspidal weight gaps; the auxiliary core spaces have the specified discrete-series models; all iterated row lifts are rapidly decreasing and their theta integrals converge; nonzero source maps have a nonzero initial core period on every nonzero smooth vector; core forms are spanned by forms reached by the prescribed lift paths; and nonzero core periods ascend along compatible chains to a nonzero final pairing.

For every $\varepsilon,C_F\in\mathbb R$ with $C_F\ge6510$, there is $x_0$ such that the following holds for every full arithmetic datum with scale $x\ge x_0$, exponent $\varepsilon$, and the complete prescribed size conditions. Fix any permitted family of level characters, its distinguished member, a compatible grid with constants $(1,C_F,b)$, its Weil actions, and quotient measures satisfying the full row-measure conditions. Let $M_0$ be any discrete-series model of the initial space whose Cartan matrices equal those of the grid. Let $t$ be a nonzero equivariant complex-linear map from its smooth vectors to automorphic functions, with the prescribed congruence level and scalar character one. For every nonzero smooth vector $w$, there exist a permitted real Schwartz parameter $\rho$, a linear functional $\xi$ on the final coefficient representation, a coefficient-valued automorphic form $\Psi$ of the final prescribed level, and finite theta data $\Phi$ such that $$\mathcal P_{\rho,\xi,\Psi,\Phi}(t(w))\ne0.$$ Here $\mathcal P$ is the prescribed final pairing of the iterated character-twisted theta lift with $\Psi$, evaluated using $\xi$.
