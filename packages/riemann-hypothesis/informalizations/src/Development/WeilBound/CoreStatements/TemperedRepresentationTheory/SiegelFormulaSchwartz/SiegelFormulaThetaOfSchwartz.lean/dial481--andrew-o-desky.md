---
{
  "module": "src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/SiegelFormulaSchwartz/SiegelFormulaThetaOfSchwartz.lean",
  "declarations": [
    "PositivityTheory.SiegelWeilFormulaUnitary.siegelFormula_theta_of_schwartz'"
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

## Siegel–Weil identity for smooth theta functions

[Theorem THETA.1554](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormulaUnitary.siegelFormula_theta_of_schwartz'/)

Assume the source's Siegel–Weil formula. Fix its full arithmetic theta datum with CM extension $E/F$, and Hermitian spaces $A,B$ of ranks $a,b$, with $$1\le a,\qquad 2a<b.$$ Let $2A$ denote the doubled space, $\psi$ an adelic additive character, $\chi:\mathbb A_E^\times\to S^1$, and $\omega$ an action for $(2A,B)$ satisfying the source's oriented Weil-datum conditions with splitting characters $(1,\chi)$. Let $f$ on the oriented oscillator space be continuous, smooth at infinity and invariant under a finite level of the Heisenberg action, with the prescribed rational quasi-periodicity. Choose additive Haar measure $\nu$ and a fundamental domain $\mathcal G$ of volume $1$ for $M_{b,a}(E)$ in $M_{b,a}(\mathbb A_E)$. Put $$\iota(y)=(y,-y),\qquad \Phi(g)=\int_{\mathcal G}(\omega(g,1)f)(\iota(y))\,d\nu(y).$$ Let $P\subseteq U(2A)$ be the Siegel parabolic and let $m$ be any Haar measure on $U(B)(\mathbb A_F)$. Then $\Phi$ is left $P(F)$-invariant, its coset sum converges at every $g$, and $$\sum_{\gamma\in P(F)\backslash U(2A)(F)}\Phi(\gamma g) =\operatorname{Avg}_{U(B)(F)\backslash U(B)(\mathbb A_F)}(\omega(g,h)f)(0).$$ The right side uses normalized averaging with respect to the quotient measure induced by $m$.
