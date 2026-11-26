---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalPseudoCoefficientExistenceUnitaryGroupStatement.lean",
  "declarations": [
    "GlobalTheory.T.localPseudoCoefficientExistence_unitaryGroup"
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

## A pseudo-coefficient with prescribed regular orbital integrals

[Theorem REP.0750](https://andrewodesky.com/rh/lean/GlobalTheory.T.localPseudoCoefficientExistence_unitaryGroup/)

Let $r$ be odd, choose signs $\epsilon_1,\ldots,\epsilon_r\in\{+1,-1\}$, and put $G=U(\operatorname{diag}\epsilon)$ and $K=U(\#\{\epsilon_i=1\})\times U(\#\{\epsilon_i=-1\})$. Let $\lambda\in\mathbb Z^r$ satisfy $$\lambda_i-\lambda_{i+1}\ge100r^4\qquad(1\le i<r).$$ Let $\pi$ be a strongly continuous unitary irreducible representation on a nonzero complex Hilbert space, with all matrix coefficients square integrable. Assume the lowest-type conditions below. For every Haar measure $\mu$ on $G$, there is a smooth compactly supported function $f$, finite under left and right $K$-translation, with $$\operatorname{tr}\pi(f)=1,\qquad\operatorname{tr}\tau(f)=0$$ for every strongly continuous irreducible unitary representation $\tau$ on a complex Hilbert space not unitarily equivalent to $\pi$; these operators have the stated traces.

For every regular semisimple $s\in G$ and every left and right invariant Haar measure $\nu$ on its centralizer $G_s$, the orbital integral exists. It is zero if $G_s$ is noncompact. If $G_s$ is compact and $s$ is conjugate to $\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_r})$, it is $$O_s(f)=\frac{\overline{\Theta_\lambda(\theta)}}{\nu(G_s)}.$$
