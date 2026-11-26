---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean",
  "declarations": [
    "GlobalTheory.LocalRows.at_choice_alt"
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

## Off-diagonal bound and row bounds for pairs of geometric terms, assuming the Siegel-Weil formula

[Theorem THETA.1.1772](https://andrewodesky.com/rh/lean/GlobalTheory.LocalRows.at_choice_alt/)

Assume ([Hypothesis: the Siegel-Weil formula for unitary groups over a CM extension, for nondegenerate Fourier coefficients in the range M \> 2n](https://andrewodesky.com/rh/lean/HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent/)). Let $\mathcal A$ be a class of families and let $\sigma$ be a selection on $\mathcal A$, in the sense of ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)). Write $\mathcal A''$ for the second refinement of $\mathcal A$, defined in ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)), and $\sigma_{\rm sp}$ for the spectral selection of $\sigma$, restricted to the families in $\mathcal A''$. Then the following three assertions hold.

1. **Row bounds for pairs of terms.** Hypothesis (row bounds for pairs of terms along a selection) of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)) holds for $\mathcal A''$ and $\sigma_{\rm sp}$ with constant $3$.
2. **Off-diagonal bound.** For all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal A''$ there is $x_0$ such that at every member $(x,i)$ of $\mathrm{Fm}$ with $x\ge x_0$ and $x>x_1$ at which the family standing conditions with constant $3$ hold, every two distinct source words $u\ne u'$ of the datum $D(x,i)$ satisfy $$\bigl\|K^0_{u,u'}\bigr\|_{\rm HS}^{2}\ \le\ \bigl(1+b^{-6}\bigr)\,\frac{d_u\,d_{u'}}{D_*}.$$
3. **Lower bound for the primes of the sources.** For all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal A''$ there is $x_0$ such that at every member $(x,i)$ of $\mathrm{Fm}$ with $x\ge x_0$ at which the family standing conditions with constant $3$ hold, every source word $w$ of the datum $D(x,i)$ satisfies $$1\ \le\ T_w\left(\frac{2\pi}{\operatorname{rd}_E\,g_0g_1}\right)^{m-2}.$$

The family standing conditions, the primes $T_u$, the dimensions $d_u$, the real number $D_*$, the root discriminant $\operatorname{rd}_E$, the primes $g_0,g_1$, the integer $m$ and the number $b=\exp(x^{\varepsilon})$ formed from the size data of the member are those of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)). The operator $K^0_{u,u'}$ is the sum of term operators over the identity, generic and non-generic terms for $(u,u')$ of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)), formed with the automorphic setting and the completion of the spectral realization $\sigma_{\rm sp}(x,i)$, and $\|\cdot\|_{\rm HS}$ is the Hilbert–Schmidt norm.

The hypothesis in assertion 1 concerns two sets of ordered pairs $(a_1,a_2)$ of terms for $(u,u')$ with the same row label: the set $Q_{\ge2}$ of pairs with $G(a_1)\ne0$, $G(a_2)\ne0$ and $s_0(a_1,a_2)\ge2$, and the set $Q_1^{\rm gen}$ of pairs of generic terms with $s_0(a_1,a_2)=1$ for which the scalar predicate fails. For each of these two sets $Q$ it gives the bound $$\Gamma_1\sum_{(a_1,a_2)\in Q}\bigl|\langle v_{a_1},v_{a_2}\rangle\bigr|\ \le\ \exp\!\Bigl(-\tfrac13\,kf\log k\Bigr)\,\frac{\delta_u\,\delta_{u'}}{D_\star}$$ at every member $(x,i)$ with $x\ge x_0$ and $x>x_1$ and for every two source words $u,u'$ of $D(x,i)$ that satisfy the three conditions listed there. Here $\delta_u$, $\delta_{u'}$ and $D_\star$ are the dimensions of the column spaces and the real number that the same page attaches to the automorphic setting and the completion of $\sigma_{\rm sp}(x,i)$; the second of the three conditions contains the equalities $\delta_u=d_u$, $\delta_{u'}=d_{u'}$ and $D_\star=D_*$.
