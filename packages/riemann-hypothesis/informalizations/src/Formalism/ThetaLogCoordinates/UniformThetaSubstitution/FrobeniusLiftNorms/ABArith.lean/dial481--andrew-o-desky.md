---
{
  "module": "src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FrobeniusLiftNorms/ABArith.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.G7.factorialValuationLowerBound"
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

## A factorial valuation bound with logarithmic loss

[Theorem ANT.0759](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.factorialValuationLowerBound/)

For every prime $p$ and every integer $m\ge0$, $$v_p(m!)\ge\frac{m}{p-1}-\ell_p(m),\qquad \ell_p(m)=\begin{cases}0,&m=0,\\\lfloor\log_p m\rfloor+1,&m>0.\end{cases}$$ Here $v_p$ is the normalized $p$-adic valuation on nonzero integers.
