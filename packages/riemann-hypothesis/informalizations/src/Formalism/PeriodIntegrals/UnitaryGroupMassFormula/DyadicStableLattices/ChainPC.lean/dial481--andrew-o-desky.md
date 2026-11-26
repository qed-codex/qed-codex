---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/DyadicStableLattices/ChainPC.lean",
  "declarations": [
    "PI.GoodTwo.ChainBetweenPairs.chain_core"
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

## An index-two lattice chain from a CM element of power-of-two norm

[Theorem ANT.1003](https://andrewodesky.com/rh/lean/PI.GoodTwo.ChainBetweenPairs.chain_core/)

Let $d\ge0$ satisfy $d\equiv7\pmod8$, put $\omega=(1+i\sqrt d)/2$, and let $\Lambda\subset\mathbb C$ be a period lattice stable under multiplication by $\omega$. Suppose $h\ge0$, $X,Y\in\mathbb Z$, $Y$ is odd, and $$X^2+XY+\frac{d+1}{4}Y^2=2^h.$$ Put $\pi=X+Y\omega$. There is a sequence of period lattices $(\Lambda_i)_{i\ge0}$ with $\Lambda_0=\Lambda$, each stable under $\omega$, such that $$\Lambda_i\subset\Lambda_{i+1},\qquad[\Lambda_{i+1}:\Lambda_i]=2\quad(0\le i<h),\qquad\Lambda_h=\pi^{-1}\Lambda.$$
