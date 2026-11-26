---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockCoinvariantsHighestWeightCyclicMultiplicityOStatement.lean",
  "declarations": [
    "GlobalTheory.T.fockCoinvariants_highestWeightCyclic_multiplicityOne"
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

## Cyclic highest-weight generation modulo Fock coinvariants

[Theorem REP.1387](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockCoinvariants_highestWeightCyclic_multiplicityOne/)

Let $P,Q,R,S\ge0$ and $x\in\mathbb C$. In the polynomial Fock model $\mathcal F$ for the pair of unitary signatures $(P,Q)$ and $(R,S)$ defined in ([Commuting Lie actions with rational weights in a polynomial model](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockActions_lie_rationalWeights_commute/)), write $\rho_1,\rho_2$ for the two commuting complexified Lie algebra actions. Put $$C=\operatorname{span}_{\mathbb C}\{\rho_1(X)f-x\operatorname{tr}(X)f:X\in\mathfrak{gl}_{P+Q}(\mathbb C),\ f\in\mathcal F\}.$$ There are a rational weight $\mu$ for $\mathfrak{gl}_{R+S}$ and a vector $v\in\mathcal F$ of highest weight $\mu$ for the compact blocks of $\rho_2$ such that $$U(\mathfrak{gl}_{R+S})v+C=\mathcal F,\qquad\mathcal F^{\mathrm{hw}}_\mu\subseteq\mathbb Cv+C.$$ Here $\mathcal F^{\mathrm{hw}}_\mu$ is the space of vectors of weight $\mu$ annihilated by $\rho_2(E_{ij})$ for $i<j$ within either of the two blocks of sizes $R,S$. The quotient $\mathcal F/C$ and the chosen vector $v$ are allowed to be zero.
