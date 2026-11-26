---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ThetaTranslateLogNormParallelogramLaw.lean",
  "declarations": [
    "GlobalTheory.ThetaPar.par_holds"
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

## A parallelogram identity for logarithmic theta-translation constants

[Theorem PHT.1556](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaPar.par_holds/)

Fix the source's full arithmetic datum, a prime $p$, and a nonzero ideal $\mathfrak c$ of the designated imaginary quadratic field with $\gcd(N\mathfrak c,2dp)=1$, where $d$ is the datum's discriminant parameter, and a chosen twelfth root $\delta$ of its ideal-lattice discriminant. Let $\Lambda\subseteq\mathbb C$ be the resulting period lattice. Use the compatible $p$-adic Weierstrass and formal-group model of ([A translated theta series is a scalar times an integral unit series](https://andrewodesky.com/rh/lean/GlobalTheory.T.thetaTranslateSeries_eq_const_mul_integral_one_series/)), including its algebraic-number embedding in $\mathbb C_p$, change of variables, parameter and inverse formal logarithm. For $s\in\mathbb C$, let $x(s)=x_p(s)$, $\tau_s(T)$ and $c(s)=c_s$ be the normalized coordinate, theta-translation series and scalar defined there. Put $$L(s)=\begin{cases}0&s\in\Lambda,\\ \log|c(s)|_p&s\notin\Lambda.\end{cases}$$ Suppose that whenever $s\notin\Lambda$ is torsion of order prime to $p$ in $\mathbb C/\Lambda$, $|x(s)|_p\le1$ and $$\tau_s(T)=c(s)w_s(T),\qquad w_s(0)=1,\qquad |[T^j]w_s|_p\le1\quad(j\ge0).$$ If $P\in\mathbb C$ is killed modulo $\Lambda$ by some positive integer prime to $p$, and $Q\notin\Lambda$ is likewise of order prime to $p$, then $$L(P+Q)+L(P-Q)=2L(P)+2L(Q).$$
