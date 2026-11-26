---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/ExponentialNegativity/SqIntCritHolds.lean",
  "declarations": [
    "PositivityTheory.Rg.Rs.sqIntCrit_holds"
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

## Square integrability from negative constant-term exponents

[Theorem REP.1203](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Rs.sqIntCrit_holds/)

Let $E$ be a totally complex number field, let $N\ge0$, and let $\phi$ be a smooth automorphic form on $\mathrm{GL}_N(\mathbb A_E)$ invariant under the real split central subgroup. For $0<r<N$, let $F_r$ be its constant term along the standard parabolic of type $(r,N-r)$. Let $a_r(t)$ have archimedean component $\operatorname{diag}(e^tI_r,I_{N-r})$ at every infinite place and trivial finite component. Define $\mathcal E_r(\phi)$ to consist of the $c\in\mathbb C$ for which the complex span of the functions $g\mapsto F_r(a_r(t)g)$ contains a nonzero $F$ satisfying $$F(a_r(t)g)=e^{ct}F(g)\quad(t\in\mathbb R).$$ If $$\frac{\Re c}{[E:\mathbb Q]}-\frac{r(N-r)}2<0\qquad(0<r<N,\ c\in\mathcal E_r(\phi)),$$ then $\phi$ is square integrable modulo the rational points and the real split central subgroup.
